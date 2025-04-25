import asyncio
from fastapi import APIRouter, HTTPException , status
from pydantic import UUID4

from app.auth.core.validator import BearerTokenDep
from app.core.messaging.messaging_broker import messaging_broker
from app.db.base import SessionDep
from app.crud.event import crud as event_crud
from app.db.models import Client, Event
from app.schemas.table_models import ClientCreate, EventCreate, EventRead, EventUpdate
from app.core.base_classes.router_base import RouterBase
from app.auth.auth import auth_broker
from app.crud.client import client_crud
from app.core.s3_manage import s3_manager


class EventRouter(RouterBase):

    def _setup_router(self):

        @self.router.post("")
        async def create_one(
            data: EventCreate,  # Fixed type annotation # type: ignore
            session: SessionDep,
            access_token: BearerTokenDep
        ) -> EventRead : # type: ignore
            """
            Create a single record.
            """

            user_info = auth_broker.get_user_sub(access_token=access_token)

            client_create = ClientCreate(
                username=user_info.username,
                auth_provider_id=user_info.user_sub
            )
            client: Client = client_crud.filter_by_params(session=session , queryCmd="first" , **client_create.model_dump())
            data.client_id = client.id
            event : Event = self.crud.create(session=session, obj_in=data.model_dump())
            s3_manager.create_event_folder(client_id=data.client_id , event_name=event.name)
            
            asyncio.create_task(messaging_broker.send(f"📸 {client_create.username} created new event: {event.name}"))

            return event


        return super()._setup_router()

# Use RouterBase for standard CRUD operations
router = EventRouter(
    crud=event_crud,
    create_model=EventCreate,
    read_model=EventRead,
    update_model=EventUpdate,
).router


# @router.post("/{event_id}/link-user/{user_id}", response_model=EventRead)
# async def link_user_to_event(event_id: UUID4, user_id: UUID4, session: SessionDep):
#     """
#     Link a user to an event.
#     """
#     return event_crud.link_user_event(session=session, event_id=event_id, user_id=user_id)


# @router.post("/{event_id}/link-image/{image_id}", response_model=EventRead)
# async def link_image_to_event(event_id: UUID4, image_id: UUID4, session: SessionDep):
#     """
#     Link an image to an event.
#     """
#     return event_crud.link_image_event(session=session, event_id=event_id, image_id=image_id)
