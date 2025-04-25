import os

from fastapi import APIRouter, Request, Response
from fastapi import File, UploadFile
from pydantic import UUID4

from app import crud
from app.core.base_classes.router_base import RouterBase
from app.crud.user import UserCrud
from app.db.base import SessionDep
from app.db.models import User
from app.schemas import table_models
from app.api.v1.routes import utils


try:
    from dotenv import load_dotenv
    load_dotenv()
except:
    pass

router = RouterBase(
    crud=UserCrud(User),
    create_model=table_models.UserCreate,
    read_model=table_models.UserRead,
    update_model=table_models.UserUpdate,
).router


# @router.get("/{id}")
# async def get_user_by_id(
#     id: UUID4
# ) -> table_models.UserRead:
    
#     return crud.user.crud.get(id=id)

# @router.delete("/{id}")
# async def delete_user_by_id(
#     id: UUID4
# ):
    
#     return crud.user.crud.delete(id=id)

@router.post("/create-from-image")
async def create_user(
    full_name: str,
    phone_number: str,
    session: SessionDep,
    response: Response,
    image: UploadFile = File(...),
) -> table_models.UserRead:

    """
    Create a new user by extracting face from an image provided in the AWS S3 event.

    Args:
        object_key (str): Object key of the image in S3.
        bucket_name (str): Name of the S3 bucket.
        user_info (UserCreate): Information about the user.
        image (UploadFile): Uploaded image file.

    Returns:
        UserRead: A message indicating the success of user creation along with user details.
    """

    new_user = table_models.UserCreate(
        full_name=full_name,
        phone_number=phone_number
    )

    encodings = utils.encode_image_from_path(image=image , limit=1)

    if len(encodings):
        new_user.face_identification_info = list(encodings[0])

    possible_match = crud.user.crud.get_by_encoding(session=session, face_encoding=new_user.face_identification_info)

    if possible_match is None:
        # Save new user to db and return user record
        user : User =  crud.user.crud.create(session=session, obj_in=new_user.model_dump())
    else:
        user : User =  crud.user.crud.update(session=session, id=possible_match.id , obj=new_user.model_dump())
    
    response.set_cookie("guest" , value=str(user.id))

    return user


@router.get("/guest/whoami")
async def check_registered_guest(
    request: Request,
    session: SessionDep,
) -> table_models.UserRead:

    guest_user_id = request.cookies.get("guest")
    
    if guest_user_id:

        guest: User = crud.user.crud.get(session=session , id=guest_user_id)

    return guest

