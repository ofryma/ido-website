import logging
from uuid import UUID
from fastapi import APIRouter, HTTPException, logger, status, Cookie
from typing import Optional, Union
import base64
import json
import os
import asyncio
from pydantic import UUID4

from app.auth.core.validator import BearerTokenDep
from app.core.base_classes.crud_base import CRUDBase
from app.core.base_classes.router_base import RouterBase
from app.core.s3_manage import s3_manager
from app.db.base import SessionDep
from app.db.models import Client
from app.auth.auth import auth_broker
from app.schemas.responses import S3TokenResponse
from app.schemas.table_models import ClientCreate, ClientRead, ClientUpdate
from app.crud.client import client_crud
from app.core.messaging.messaging_broker import messaging_broker

router = RouterBase(
    crud=client_crud,
    create_model=ClientCreate,
    read_model=ClientRead,
    update_model=ClientUpdate,
).router


@router.post("/whoami")
async def client_whoami(
    session: SessionDep,
    access_token: BearerTokenDep
) -> ClientRead:
    
    """
    Retrieves client information using the JWT token stored in cookies.
    If the client does not exist, it creates a new record and an S3 folder.
    """
    try:
        logging.info("Searching user information from token")
        user_info = auth_broker.get_user_sub(access_token=access_token)
    except Exception as e:
        raise HTTPException(status_code=500 , detail={"message" : f"Error: find user sub info {e}"})

    client_create = ClientCreate(
        username=user_info.username,
        auth_provider_id=user_info.user_sub
    )

    try:
        client: Client = client_crud.filter_by_params(
            session=session , 
            queryCmd="first" , 
            **client_create.model_dump()
        )
        
        if client is None:
            client: Client = client_crud.create(session=session , obj_in=client_create.model_dump())

        if client is None: 
            client = client_crud.create(session=session, obj_in=client_create.model_dump())
            asyncio.create_task(messaging_broker.send(f"🎉 New client created: {client.username}"))
    except Exception as e:
        raise HTTPException(status_code=500 , detail={"message" : f"Error: creating client {e}"})
    try:
        logging.debug(f"Creating folder for client {client.id} , [{str(client.id)}]")
        # Create an S3 folder for the new client
        s3_manager.creat_client_folder(str(client.id))
        
        return client
    except Exception as e:
        raise HTTPException(status_code=500 , detail={"message" : f"Error: creating client folder {e}"})
    


@router.post("/get-s3-token")
async def get_s3_token(
    session: SessionDep,
    access_token: BearerTokenDep,
) -> S3TokenResponse:
    """
    API endpoint that returns a temporary S3 token for a specific user.
    """
    
    user_info = auth_broker.get_user_sub(access_token=access_token)

    client_create = ClientCreate(
        username=user_info.username,
        auth_provider_id=user_info.user_sub
    )

    try:
        
        # Fetch client from database
        client: Client = client_crud.filter_by_params(session=session, queryCmd="first", **client_create.model_dump())

        if client is None:
            raise HTTPException(status_code=404, detail="Client not found")

        # return s3_manager.get_s3_upload_token(str(client.id))
        return s3_manager.get_s3_assume_tole(str(client.id))

    except Exception as e:
        logging.error(f"Error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

