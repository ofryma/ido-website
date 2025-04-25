from datetime import datetime
from pydantic import BaseModel

class BaseResponse(BaseModel):

    message: str


class DeleteRecordResponse(BaseResponse):
    pass

class S3TokenResponse(BaseModel):
    access_key_id: str
    secret_access_key: str
    session_token: str
    region: str
    bucket: str
    allowed_prefix: str
    expires_at: datetime