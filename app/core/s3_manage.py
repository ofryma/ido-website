from datetime import datetime, timedelta
import json
import logging
import os
import boto3
from pydantic import UUID4
from ..schemas.responses import S3TokenResponse
from app.core.config import settings


class S3Manager:
    def __init__(self):

        self.bucket_name = os.getenv("S3_BUCKET_NAME")
        self.region = os.getenv("AWS_DEFAULT_REGION", "us-east-2")
        self.s3 = boto3.client(
            "s3",
            aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
            aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
            region_name=self.region,
        )
        self.sts = boto3.client("sts")

    def _check_folder_exists(self, folder_name: str) -> bool:
        """
        Checks if an S3 folder exists. If `subfolder` is provided, checks for a nested folder.
        """
        return False
        response = self.s3.list_objects_v2(Bucket=self.bucket_name, Prefix=folder_name, MaxKeys=1)
        return "Contents" in response

    def _create_folder(self, folder_name: str):
        """
        Creates an S3 folder if it does not exist. If `subfolder` is provided, creates a nested folder.
        """

        logging.debug("Checking folder suffix")
        if not folder_name.endswith("/"): 
            logging.debug("Adding backslash" , f"{folder_name}/")
            folder_name = f"{folder_name}/"


        logging.debug("Check if folder already exists in bucket")
        if not self._check_folder_exists(folder_name):
            logging.debug("Creating folder in bucket")
            self.s3.put_object(Bucket=self.bucket_name, Key=folder_name)

    def _delete_folder(self, client_id: str, subfolder: str = None):
        """
        Deletes an S3 folder and all objects inside it. If `subfolder` is provided, deletes the nested folder.
        """
        prefix = f"{client_id}/"
        if subfolder:
            prefix += f"{subfolder}/"

        objects = self.s3.list_objects_v2(Bucket=self.bucket_name, Prefix=prefix)
        if "Contents" in objects:
            delete_objects = {"Objects": [{"Key": obj["Key"]} for obj in objects["Contents"]]}
            self.s3.delete_objects(Bucket=self.bucket_name, Delete=delete_objects)


    def get_s3_assume_tole(self, client_id: str) -> S3TokenResponse:

        # Replace with your role ARN
        ROLE_ARN = f"arn:aws:iam::{settings.aws_account_id}:role/{settings.s3_assume_role_name}"
        SESSION_NAME = "TemporarySession"

        # Initialize STS client
        sts_client = boto3.client("sts")

        # Assume the role
        response = sts_client.assume_role(
            RoleArn=ROLE_ARN,
            RoleSessionName=SESSION_NAME
        )

        # Extract temporary credentials
        credentials = response["Credentials"]

        return S3TokenResponse(
            access_key_id=credentials["AccessKeyId"],
            secret_access_key=credentials["SecretAccessKey"],
            session_token=credentials["SessionToken"],
            bucket=self.bucket_name,
            expires_at=datetime.utcnow() + timedelta(seconds=settings.s3_temp_session_time),
            allowed_prefix=client_id,
            region=self.region
        )

    def get_s3_upload_token(self, client_id: str) -> S3TokenResponse:
        """
        Generates a temporary token for S3 access for a specific user.
        """
        session_name = f"user-{str(client_id)[:8]}" 

        policy = {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Effect": "Allow",
                    "Action": [
                        "s3:ListBucket"
                    ],
                    "Resource": f"arn:aws:s3:::{self.bucket_name}"
                },
                {
                    "Effect": "Allow",
                    "Action": "s3:*",
                    "Resource": [
                        f"arn:aws:s3:::{self.bucket_name}/{str(client_id)}/*"
                    ]
                }
            ]
        }


        response = self.sts.get_federation_token(
            Name=session_name,
            Policy=json.dumps(policy),
            DurationSeconds=settings.s3_temp_session_time
        )

        return S3TokenResponse(
            access_key_id=response["Credentials"]["AccessKeyId"],
            secret_access_key=response["Credentials"]["SecretAccessKey"],
            session_token=response["Credentials"]["SessionToken"],
            bucket=self.bucket_name,
            expires_at=datetime.utcnow() + timedelta(seconds=settings.s3_temp_session_time),
            allowed_prefix=client_id,
            region=self.region,
        )
    
class S3ClientManager(S3Manager):

    
    def creat_client_folder(self , client_id: UUID4):
        logging.debug("Recived client id" , client_id)
        folder_name = str(client_id)

        logging.debug("Setting folder name" , folder_name)

        return self._create_folder(folder_name)
        

    def create_event_folder(self , client_id: UUID4 , event_name: str):
        """
        """

        folder_name = "/".join([str(client_id) , event_name])

        return self._create_folder(folder_name)


s3_manager = S3ClientManager() 