import os
from typing import Annotated

from fastapi import Depends, HTTPException, Request , status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from app.auth.core.agents.base_agent import BasicResponse
from app.auth.core.broker import COOKIE_KEY_NAME, auth_broker


class TokenValidator(HTTPBearer):

    async def __call__(self, request: Request) -> str:

        if os.environ.get("DEV_ENV") == "development":
            return "dev.access.token"

        access_token = None

        # Try to recive the access token from cookies of the request
        access_token: str = request.cookies.get(COOKIE_KEY_NAME.ACCESS_TOKEN.value)

        if access_token is None:
            credentials = await super().__call__(request)
            access_token: str = credentials.credentials

        auth_broker.validate_access_token(access_token=access_token)

        return access_token

security = TokenValidator()

BearerTokenDep = Annotated[str, Depends(security)]