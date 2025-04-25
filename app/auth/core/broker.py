from enum import Enum
from typing import Literal, Optional

from fastapi import Request, Response , status , HTTPException

from app.auth.core.agents.base_agent import BasicResponse, LoginAuthResponse, UserSub
from app.auth.core.agents.cognito.cognito_agent import CognitoAuthAgent


class COOKIE_KEY_NAME(Enum):

    ACCESS_TOKEN: str =  "access_token"
    REFRESH_TOKEN: str = "refresh_token"

class AuthBroker:

    def __init__(self , agent_type: Literal["cognito"]):
        if agent_type == "cognito":
            self.auth_agent = CognitoAuthAgent()

    def login(self , username: str , password: str) -> LoginAuthResponse:
        return self.auth_agent.login(username , password)
    
    def signup(self , username: str , password: str , email: str) -> BasicResponse:
        return self.auth_agent.signup(username , password , email)

    def confirm_signup(self, username: str , confirmation_code: str) -> BasicResponse:

        return self.auth_agent.confirm_signup(username , confirmation_code)

    def forgot_password_request(self , email: str) -> BasicResponse:
        return self.auth_agent.forgot_password_request(email)

    def verify_forgot_password(self, username: str , verification_code: str , new_password: str) -> BasicResponse:
        return self.auth_agent.verify_forgot_password(username , verification_code , new_password)

    def delete_account(self , access_token) -> BasicResponse:
        return self.auth_agent.delete_account(access_token)

    def change_password_request(self, access_token: str, previous_password: str, proposed_password: str) -> BasicResponse:
        return self.auth_agent.change_password_request(access_token, previous_password, proposed_password)

    def validate_access_token(self, access_token: str):
        return self.auth_agent.validate_access_token(access_token)
    
    def set_token_cookies(self, response: Response, loginResponse: LoginAuthResponse):

        response.set_cookie(COOKIE_KEY_NAME.ACCESS_TOKEN.value , loginResponse.access_token)
        response.set_cookie(COOKIE_KEY_NAME.REFRESH_TOKEN.value , loginResponse.refresh_token)


    def remove_token_cookies(self , response: Response) -> Response:

        response.delete_cookie(COOKIE_KEY_NAME.ACCESS_TOKEN.value)
        response.delete_cookie(COOKIE_KEY_NAME.REFRESH_TOKEN.value)

        return response

    def get_user_sub(self , access_token: str) -> UserSub:
        
        return self.auth_agent.get_user_sub(access_token)

auth_broker = AuthBroker(agent_type="cognito")

