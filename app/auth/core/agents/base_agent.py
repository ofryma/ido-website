
from typing import Optional
from pydantic import BaseModel



class BasicResponse(BaseModel):

    ok: bool
    message: Optional[str]
    metadata: Optional[dict]

class LoginAuthResponse(BasicResponse):

    access_token: str
    refresh_token: str


class UserSub(BaseModel):

    username: str
    user_sub: str

class BaseAuthAgent():

    def __init__(self):
        pass

    def login(self , username: str , password: str) -> LoginAuthResponse:
        pass

    def signup(self, username: str , password: str , email: str) -> BasicResponse:
        pass

    def confirm_signup(self , username: str , confirmation_code: str) -> BasicResponse:
        pass

    def forgot_password_request(self , email: str) -> BasicResponse:
        pass

    def verify_forgot_password(self, username: str, verification_code: str, new_password: str) -> BasicResponse:
        pass

    def delete_account(self, access_token: str) -> BasicResponse:
        pass

    def change_password_request(self, access_token: str, previous_password: str, proposed_password: str) -> BasicResponse:
        pass

    def validate_access_token(self, access_token: str) -> BasicResponse:
        pass

    def get_user_sub(self , access_token: str) -> UserSub:
        pass