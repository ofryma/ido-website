import os

import boto3
from botocore.exceptions import BotoCoreError, ClientError
from fastapi import HTTPException , status
from app.auth.core.agents.base_agent import BaseAuthAgent, BasicResponse, LoginAuthResponse, UserSub

class CognitoAuthAgent(BaseAuthAgent):
    def __init__(
            self, 
            user_pool_id: str = os.environ.get("COGNITO_USERPOOL_ID"), 
            client_id: str = os.environ.get("COGNITO_CLIENT_ID"),
            region: str = os.environ.get("COGNITO_REGION"), 
        ):
        self.client = boto3.client("cognito-idp", region_name=region)
        self.user_pool_id = user_pool_id
        self.client_id = client_id

    def login(self, username: str, password: str) -> LoginAuthResponse:
        try:
            response = self.client.initiate_auth(
                ClientId=self.client_id,
                AuthFlow="USER_PASSWORD_AUTH",
                AuthParameters={
                    "USERNAME": username,
                    "PASSWORD": password,
                },
            )
        
            return LoginAuthResponse(
                ok = True,
                message="Succussful login",
                access_token=response.get("AuthenticationResult").get("AccessToken"),
                refresh_token=response.get("AuthenticationResult").get("RefreshToken"),
                metadata=dict(response)
            )
        except (BotoCoreError, ClientError) as e:
            return {"error": str(e)}

    def signup(self, username: str, password: str, email: str) -> BasicResponse:
        try:
            response = self.client.sign_up(
                ClientId=self.client_id,
                Username=username,
                Password=password,
                UserAttributes=[
                    {"Name": "email", "Value": email},
                ],
            )
            
            return BasicResponse(
                ok = True,
                message="Successful signup, please continue to signup confirmation",
                metadata=dict(response)
            )

        except (BotoCoreError, ClientError) as e:
            return {"error": str(e)}

    def confirm_signup(self, username: str, confirmation_code: str) -> BasicResponse:
        try:
            response = self.client.confirm_sign_up(
                ClientId=self.client_id,
                Username=username,
                ConfirmationCode=confirmation_code,
            )

            return BasicResponse(
                ok = True,
                message="Successful signup confirmation",
                metadata=dict(response)
            )

        except (BotoCoreError, ClientError) as e:
            return {"error": str(e)}

    def forgot_password_request(self, email: str) -> BasicResponse:
        try:
            response = self.client.forgot_password(
                ClientId=self.client_id,
                Username=email,
            )
            
            destination = response.get("CodeDeliveryDetails").get("Destination")
            attribute_name = response.get("CodeDeliveryDetails").get("AttributeName")

        
            return BasicResponse(
                ok = True,
                message=f"A message was sent to {destination} via {attribute_name}",
                metadata=dict(response)
            )
        except (BotoCoreError, ClientError) as e:
            return {"error": str(e)}

    def verify_forgot_password(self, username: str, verification_code: str, new_password: str) -> BasicResponse:
        try:
            response = self.client.confirm_forgot_password(
                ClientId=self.client_id,
                Username=username,
                ConfirmationCode=verification_code,
                Password=new_password,
            )

            status_code = response.get("ResponseMetadata").get("HTTPStatusCode")
            if status_code == 200:
                return BasicResponse(
                    ok = True,
                    message=f"Password changed successfully",
                    metadata=dict(response)
                )
            else:
                raise HTTPException(status_code=status_code , detail=response)

            
        except (BotoCoreError, ClientError) as e:
            return {"error": str(e)}

    def change_password_request(self, access_token: str, previous_password: str, proposed_password: str) -> BasicResponse:
        try:
            response = self.client.change_password(
                PreviousPassword=previous_password,
                ProposedPassword=proposed_password,
                AccessToken=access_token,
            )

            destination = response.get("CodeDeliveryDetails").get("Destination")
            attribute_name = response.get("CodeDeliveryDetails").get("AttributeName")
            
            return BasicResponse(
                message=f"A message was sent to {destination} via {attribute_name}",
                metadata=dict(response)
            )
        except (BotoCoreError, ClientError) as e:
            return {"error": str(e)}

    def delete_account(self, access_token: str) -> BasicResponse:
        try:
            response = self.client.delete_user(
                AccessToken=access_token,
            )
            
            return BasicResponse(
                ok = True,
                message=f"Account deleted successflly",
                metadata=dict(response)
            )
        
        except (BotoCoreError, ClientError) as e:
            return {"error": str(e)}
        
    def validate_access_token(self, access_token: str) -> BasicResponse:
        try:
            response = self.client.get_user(
                AccessToken=access_token,
            )

            return BasicResponse(
                ok = True,
                message="Token is valid",
                metadata=dict(response)
            )

        except (BotoCoreError, ClientError) as e:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN , detail="Invalid token")
        
    def get_user_sub(self , access_token: str) -> UserSub:

        validation_response = self.validate_access_token(access_token)

        username=validation_response.metadata.get("Username")
        user_sub = None
        for attr in validation_response.metadata.get("UserAttributes"):
            if attr.get("Name") == "sub":
                user_sub = attr.get("Value")
                break

        return UserSub(
            username=username,
            user_sub=user_sub,
        )