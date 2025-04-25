from typing import Annotated, List , Optional
from datetime import datetime

from pydantic import AfterValidator, BaseModel, Field, ValidationError , UUID4, model_validator
import json
import base64
import boto3

from app.core.config import settings

class BaseTableRead(BaseModel):

    id: UUID4
    created_at: datetime
    updated_at: datetime
    deleted: bool


def presigned_url(object_key: str , bucket_name: str) -> str:
    
    # Generate the pre-signed URL
    session = boto3.session.Session()
    s3_client = session.client(
        's3', 
        region_name=settings.s3_bucket_region, 
        config=boto3.session.Config(signature_version='s3v4')
        )


    try:
        presigned_url = s3_client.generate_presigned_url(
            'get_object',
            Params={
                'Bucket': bucket_name, 
                'Key': object_key
            },
            ExpiresIn=settings.s3_presigned_url_exp_time
        )

        return presigned_url
    except Exception as e:
        raise ValidationError(f"Failed to generate pre-signed URL: {e}")


def validate_score(v: Optional[float] = None) -> float:

    if v is None:
        return 0.0

ScoreFloat = Annotated[Optional[float] , AfterValidator(validate_score)]


class ImageBase(BaseModel):
    
    object_key: str
    bucket_name: str
    is_cover: Optional[bool] = None
        
class ImageRead(ImageBase , BaseTableRead):

    url: Optional[str] = None
    highlight_score: ScoreFloat

    @model_validator(mode="after")
    def generate_presigned_url_for_object(self):
        self.url = presigned_url(object_key=self.object_key , bucket_name=self.bucket_name)
        return self
    
class ImageCreate(ImageBase):
    pass
class ImageUpdate(ImageBase):
    pass

class ImageFilter(ImageBase):

    object_key: Optional[str] = Field(None, example="client-id/event-name/object-file-name")
    bucket_name: Optional[str] = Field(None, example="yoour-bucket-name")
    user_id: Optional[UUID4] = Field(None, example="123e4567-e89b-12d3-a456-426614174000")
    event_id: Optional[UUID4] = Field(None, example="987e6543-b21a-34c2-a123-123456789abc")



def decode_from_base64(base64_data):
    decoded_bytes = base64.b64decode(base64_data)
    decoded_json = json.loads(decoded_bytes.decode())
    return decoded_json

class UserBase(BaseModel):

    full_name: Optional[str] = Field(None, example="John Doe")
    phone_number: Optional[str] = Field(None, example="+9720501234987")

    def encode_to_base64(self):

        return base64.b64encode(self.model_dump_json().encode()).decode()


class UserRead(UserBase , BaseTableRead):
     
    id: UUID4
    # face_identification_info: List[float]
    images: List[ImageBase]

class UserCreate(UserBase):

    face_identification_info: Optional[List[float]] = None

class UserUpdate(UserBase):

    full_name: str
    phone_number: str

class EventBase(BaseModel):
    
    name: str
    client_id: Optional[UUID4] = Field(None, example="987e6543-b21a-34c2-a123-123456789abc")

class EventRead(EventBase , BaseTableRead):
    pass


class EventReadExtend(EventRead):

    users: List[UserBase]
    images: List[ImageBase]
    

class EventCreate(EventBase):
    pass    

class EventUpdate(EventBase):
    pass


class ClientBase(BaseModel):

    username: str
    auth_provider_id: UUID4


class ClientRead(ClientBase, BaseTableRead):
    events: Optional[List[EventRead]] = []


class ClientCreate(BaseModel):
    
    username: Optional[str] = Field(None, example="John Doe")
    auth_provider_id: UUID4

class ClientUpdate(ClientBase):
    pass