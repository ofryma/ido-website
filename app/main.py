from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum  # AWS Lambda handler

from app.core.config import settings

# Ido Website


app = FastAPI(
    title=f"{settings.app_homepage.capitalize()} API",
    version="0.0.1",
    description="",
)


@app.on_event("startup")
def startup_event():
    
    # # Updating schema with alembic
    # util.run_alembic_upgrade()

    pass


# CORS (Cross-Origin Resource Sharing) configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows access from all origins
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],  # Allows specified methods
    allow_headers=["*"],  # Allows all headers
)


# Hosting React application
BUILD_DIR = "app/public"

app.mount(f"/{settings.app_homepage}", StaticFiles(directory=BUILD_DIR , html=True), name=f"{settings.app_homepage}")

@app.get("/")
async def home_page():

    with open(f"{BUILD_DIR}/index.html" , "r") as f:
        content = f.read()

    return HTMLResponse(content=content)

# Lambda handler
handler = Mangum(app)
