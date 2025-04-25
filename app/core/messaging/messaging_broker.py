from enum import Enum
import logging
import os
from typing import Optional, Union

from app.core.messaging.agents.base_agent import BaseMessagingAgent
from app.core.messaging.agents.telegram_agent.agent import TelegramAgent
from app.core.messaging.schemas.requests import MessageRequest, MessageResponse
from app.core.config import settings

class MessagingAgents(Enum):

    TELEGRAM = "telegram"


class MessagingBroker:

    def __init__(self , agent: str = os.environ.get("MESSAGING_AGENT")):
        
        if os.environ.get("SEND_MESSAGING" , "0") == "1":
            if agent == MessagingAgents.TELEGRAM.value:
                self.agent = TelegramAgent()
            else:
                self.agent = BaseMessagingAgent()
        else:
            logging.warning("Skipping messaging option, if you want to set messaging from api -> set the SEND_MESSAGING=1 and the MESSAGING_AGENT environment variables")
            self.agent = BaseMessagingAgent()

    async def send(self , message: Union[MessageRequest ,str]):

        if type(message) == str:
            message = MessageRequest(
                text=message
            )

        await self.agent.send_message(message=message)


messaging_broker = MessagingBroker()