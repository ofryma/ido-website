import asyncio
from fastapi import APIRouter, HTTPException
from app.core.messaging import messaging_broker
from app.core.messaging.schemas.requests import MessageRequest , MessageResponse

router = APIRouter()

# @router.post('/send')
# async def send_single_message_to_group(
#     message: MessageRequest
# ):

#     asyncio.create_task(messaging_broker.messaging_broker.send(message))


