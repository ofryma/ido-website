from fastapi import FastAPI

from app.api.v1 import router as router_v1
from app.core.config import settings

api = FastAPI(
    title=f"{settings.app_homepage.capitalize()} API",
)

api.mount(path="/v1" , app=router_v1.router)