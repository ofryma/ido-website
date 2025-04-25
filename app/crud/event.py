from fastapi import HTTPException , status
from pydantic import UUID4
from sqlalchemy.orm import Session

from app.core.base_classes.crud_base import CRUDBase
from app.crud import user as user_crud
from app.crud import image as image_crud
from app.db.models import Event, EventImage, Image, User, UserEvent
from app.schemas.table_models import EventBase


class EventCrud(CRUDBase):

    def link_user_event(self , session: Session , event_id: UUID4 , user_id: UUID4):

        user: User = user_crud.crud.get(session=session , id=user_id)
        event: Event = self.get(session=session , id=event_id)

        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail=f"User with id {user_id} not found")
        if not event:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail=f"Event with id {event_id} not found")


        
        session.add(
        UserEvent(
            user_id = user_id,
            event_id = event_id
        )
        )

        session.commit()

        return self.get(session=session , id=event_id)  # Return the updated event
        
    def link_image_event(self , session: Session , event_id: UUID4 , image_id: UUID4):


        image: Image = image_crud.crud.get(session=session , id=image_id)
        event: Event = self.get(session=session , id=event_id)

        if not image:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail=f"Image with id {image_id} not found")
        if not event:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail=f"Event with id {event_id} not found")

        session.add(
        EventImage(
            image_id = image_id,
            event_id = event_id
        )
        )

        session.commit()

        return self.get(session=session , id=event_id)  # Return the updated event
    
    
    def get_event_from_object_key(self, session : Session , object_key: str) -> Event:
        
        # Extract event name and client id from the object key (s3 object key use "/")
        object_key_path_list = object_key.split("/")

        client_id = object_key_path_list[0] # the client id is the first folder in the path
        event_name = object_key_path_list[1] # the event name is the second folder in the path

        event_filter = EventBase(
            name=event_name,
            client_id=client_id
        )

        # Find the related event
        event : Event = self.filter_by_params(session=session , queryCmd="first" , **event_filter.model_dump())

        # If the event is not exists, create a new record for it
        if event is None:
            event: Event = self.create(session=session , obj_in=event_filter.model_dump())

        return event






crud = EventCrud(Event)