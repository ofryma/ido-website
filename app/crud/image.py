import logging
from typing import Literal
from uuid import uuid4

from sqlalchemy import select
from sqlalchemy.orm import Session , Query

from app.core.base_classes.crud_base import CRUDBase
from app.db.models import EventImage, Image, UserImage
from app.core.reko.rekognition_utils import encode_multi_face_image

class ImageCrud(CRUDBase):

    def process_image(self , session: Session , image_path: str) -> None:

        try:

            # Encode faces in the image
            face_encodings = encode_multi_face_image(image_path)
            if face_encodings is None:
                logging.error("Failed to encode face encodings. Image processing aborted.")
                return

            # For each face encoding in the image
            for face_encoding in face_encodings:
                # Convert face_encoding to list of floats
                face_encoding = [float(value) for value in face_encoding]

                # Generate unique id for the image
                image_id = str(uuid4().int & ((1 << 32) - 1))[:5]

                # Create new image record
                new_image = Image(url=image_path, vector=face_encoding)
                session.add(new_image)
                session.commit()

            logging.debug("Image processed successfully.")

        except Exception as e:
            logging.error(f"An error occurred during image processing: {e}")

        finally:
            session.close()

    def _image_for_user_filter(self , query: Query , **kwargs) -> Query:

        """
        This method will extend a given query with a new sub query.

        The sub query here will return a list of image ids for a given user id
        and the extended query will have a condion for all the images with an id in this list

        The user id must be sent as a `user_id` parameter
        """

        if kwargs.get("user_id"):
            
            subquery = (
                select(UserImage.image_id)
                .where(UserImage.user_id == kwargs.get("user_id"))
            )

            query = query.filter(Image.id.in_(subquery))

        return query
    
    def _image_for_event_filter(self , query: Query , **kwargs) -> Query:

        """
        This method will extend a given query with a new sub query.

        The sub query here will return a list of image ids for a given event id
        and the extended query will have a condion for all the images with an id in this list

        The user id must be sent as a `event_id` parameter
        """

        if kwargs.get("event_id"):

            subquery = (
                select(EventImage.image_id)
                .where(EventImage.event_id == kwargs.get("event_id"))
            )

            query = query.filter(Image.id.in_(subquery))

        return query

    
    def filter_by_params(self, session, queryCmd: Literal['all', 'first'] = "all", **kwargs):

        return super().filter_by_params(
            session, 
            queryCmd , 
            filter_methods=[
                self._image_for_event_filter,
                self._image_for_user_filter,
            ], 
            **kwargs
        )

crud = ImageCrud(Image)