from fastapi import FastAPI

from app.api.v1.routes import (
    translation,
    # image,
    # user,
    # events,
    # client,
    # messaging,
)

router = FastAPI(
    title=f"API V1"
)

# Include the various feature routers
router.include_router(translation.router, tags=["translation"])
# router.include_router(messaging.router, tags=["messaging"])
# router.include_router(user.router, tags=["user"])
# router.include_router(image.router, tags=["image"])
# router.include_router(events.router, tags=["event"])
# router.include_router(client.router, tags=["client"])
