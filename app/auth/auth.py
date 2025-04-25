import logging
from typing import Annotated
from fastapi import FastAPI , APIRouter, Response , Cookie
from fastapi.responses import HTMLResponse , JSONResponse

from app.auth.core.agents.base_agent import BasicResponse, LoginAuthResponse
from app.auth.core.broker import auth_broker
from app.auth.core.validator import BearerTokenDep

# Define auth module routers

auth_router = APIRouter()

@auth_router.post("/login")
async def login(
    username: str,
    password: str,
    response: Response,
) -> LoginAuthResponse:
    
    loginResponse = auth_broker.login(
        username=username,
        password=password
        )
    
    auth_broker.set_token_cookies(response=response , loginResponse=loginResponse)

    return loginResponse

@auth_router.post("/logout")
async def logout():
    
    return auth_broker.remove_token_cookies(JSONResponse({"message": "logout"}))
    

@auth_router.post("/signup")
async def signup(
    username: str,
    password: str,
    email: str,
) -> BasicResponse:
    return auth_broker.signup(
        username=username,
        password=password,
        email=email,
        )

@auth_router.post("/confirm-signup")
async def confirm_signup(
    username: str,
    confirmation_code: str
) -> BasicResponse:
    
    return auth_broker.confirm_signup(username , confirmation_code)


@auth_router.post("/forgot-password")
async def forgot_password(
    email: str
) -> BasicResponse:
    return auth_broker.forgot_password_request(email)


@auth_router.post("/verify-forgot-password")
async def verify_forgot_password(
    username: str,
    verification_code: str,
    new_password: str
) -> BasicResponse:
    return auth_broker.verify_forgot_password(username , verification_code , new_password)

@auth_router.post("/change-password")
async def change_password(
    access_token: str,
    previous_password: str,
    proposed_password: str,
) -> BasicResponse:
    
    return auth_broker.change_password_request(access_token , previous_password, proposed_password)


@auth_router.post("/delete-account")
async def delete_account(
    access_token: BearerTokenDep,
) -> BasicResponse:
    
    # TODO: Add logout functionality to remove cookies
    return auth_broker.delete_account(access_token)

@auth_router.post("/validate-token")
async def validate_access_token(
    access_token: BearerTokenDep,
) -> BasicResponse:

    return auth_broker.validate_access_token(access_token)

@auth_router.get("/protected")
async def protected_route(
    access_token: BearerTokenDep
):
    
    logging.debug(access_token)

    return access_token

# Define auth module app

auth = FastAPI(
    title="Auth Module",
)

auth.include_router(router=auth_router)