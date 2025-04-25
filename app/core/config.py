import logging
import os

from pydantic import BaseModel

LOGGING_LEVEL: int = int(os.environ.get("LOGGING_LEVEL")) if os.environ.get("LOGGING_LEVEL") else logging.INFO

logging.basicConfig(level=LOGGING_LEVEL)

class Settings(BaseModel):
    
    app_homepage: str = os.environ.get("APP_HOMEPAGE" , "")

    aws_account_id: str = ""


settings = Settings()