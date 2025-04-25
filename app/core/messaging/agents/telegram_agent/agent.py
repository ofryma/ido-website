import os
from typing import Final

from telegram import Bot

from app.core.messaging.agents.base_agent import BaseMessagingAgent
from app.core.messaging.schemas.requests import MessageResponse

class TelegramAgent(BaseMessagingAgent):

    def __init__(self):

        self.token: Final = os.environ.get('TELEGRAM_TOKEN')
        self.group_id: Final = os.environ.get('TELEGRAM_GROUP_ID')
        
        super().__init__()

    async def send_message(self, message) -> MessageResponse:

        bot = Bot(token=self.token)
        
        # Send the message to the specified chat ID (group)
        response = await bot.send_message(chat_id=self.group_id, text=message.text)
        
        # Close the bot instance
        await bot.close()
    
        return MessageResponse(
            message="Message sent successfuly",
            metadata=response
        )
    