from app.core.messaging.schemas.requests import MessageRequest


class BaseMessagingAgent:

    def __init__(self):
        pass

    def send_message(self , message: MessageRequest):
        pass