import logging
from typing import List

from fastapi import HTTPException
from pydantic import UUID4
from sqlalchemy.orm import Session

from app.core.base_classes.crud_base import CRUDBase
from app.db.models import Image , User ,UserImage
from app.core.reko.rekognition_utils import encode_multi_face_image
from app.core.config import settings

class UserCrud(CRUDBase):


    def get_by_encoding(self , session: Session, face_encoding: List[float], distance: float = settings.match_face_distance , * , ext_session = None) -> User:
            
        # Perform a query to find matching users based on face encoding similarity
        return session.query(User).filter(User.face_identification_info.l2_distance(face_encoding) <= distance).first()


    def get_matching_user(self , session: Session , face_encoding: List[float] , image_id: UUID4 , distance: float = settings.match_face_distance):


        try:
            # Get the image record for the current image
            image_record = session.query(Image).filter(Image.id == image_id).scalar()
        except Exception as e:
            msg = f"Error: server failed in fetching image record;"
            logging.error(msg)
            raise HTTPException(status_code=500 , detail={"message": msg,"error": f"{e}" })
        
        try:
            # Perform a query to find matching users based on face encoding similarity
            matched_user = self.get_by_encoding(
                session=session, 
                face_encoding=face_encoding , 
                distance=distance , 
                ext_session=session
                )

        except Exception as e:
            session.rollback()
            msg = f"There was an error in searching the user's according to encoding"
            logging.error(msg)
            raise HTTPException(status_code=500 , detail={"message": msg ,"error": f"{e}" })
        
        if matched_user is None:

            try:
                # Create new user
                new_user = User(face_identification_info = face_encoding)
                session.add(new_user)      
                # Commit the changes to the database
                session.commit()
                session.refresh(new_user)
                matched_user = new_user
            except Exception as e:
                session.rollback()
                msg = f"There was an error creating a new user"
                logging.error(msg)
                raise HTTPException(status_code=500 , detail={"message": msg ,"error": f"{e}" })
        try:
            # Add a connection of the user and the image
            matched_user.images.append(image_record)
            session.commit()
        except Exception as e:
            session.rollback()
            msg = f"There was an error in adding user's encoding to image {image_id}"
            logging.error(msg)
            raise HTTPException(status_code=500 , detail={"message": msg ,"error": f"{e}" })


crud = UserCrud(User)