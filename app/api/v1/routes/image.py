import logging
from typing import List

from fastapi import File, UploadFile
from pydantic import UUID4
from app.api.v1.routes import utils
from app import crud
from app.core.base_classes.router_base import RouterBase
from app.crud.image import ImageCrud
from app.db.models import Event, Image
from app.db.base import SessionDep
from app.schemas import table_models

router = RouterBase(
    crud=ImageCrud(Image),
    create_model=table_models.ImageCreate,
    read_model=table_models.ImageRead,
    update_model=table_models.ImageUpdate,
    filter_model=table_models.ImageFilter,
).router


@router.post("/toggle-cover/{image_id}")
async def make_cover(
    image_id: UUID4,
    session: SessionDep,
) -> table_models.ImageRead:

    image_record: Image = crud.image.crud.get(session=session , id=image_id)

    image_update_obj = dict(
        is_cover = not image_record.is_cover
    )

    return crud.image.crud.update(
        session=session,
        id=image_id,
        obj=image_update_obj
        )


@router.post("/link")
async def link_image(
    # image_info: table_models.ImageCreate,
    object_key: str,
    bucket_name: str,
    session: SessionDep,
    image: UploadFile = File(...),
) -> table_models.ImageRead:

    """
        Link an image stored in AWS S3 with users by matching faces and creating connections.

        1. Create new image record in the database
        2. Encode the faces in the image from the given url
        3. Query for matching users in the database and create connections to the new image record
    """

    image_info = table_models.ImageCreate(
        object_key=object_key,
        bucket_name=bucket_name,
    )

    # # 1. Write image to db
    image_record: Image = crud.image.crud.create(obj_in=image_info.model_dump() , session=session)

    # 2. Link the image to the correct event
    # get the event 
    object_event : Event = crud.event.crud.get_event_from_object_key(session=session , object_key=image_info.object_key)
    # link the image and event
    crud.event.crud.link_image_event(session=session , event_id=object_event.id , image_id=image_record.id)

    # 3. Get image encodings
    encodings = utils.encode_image_from_path(image=image)

    # 4. Query db to get all users matching to encoding and write connections
    for encoded_face in encodings:
        crud.user.crud.get_matching_user(
            face_encoding=encoded_face , 
            image_id=image_record.id , 
            session=session
            )

    # Return the new image record
    return image_record
