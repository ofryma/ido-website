import logging
import subprocess
import base64
from io import BytesIO
import os
from uuid import uuid4
from datetime import datetime


def run_alembic_upgrade():
    try:
        # Running Alembic upgrade command using subprocess
        subprocess.run(["alembic", "upgrade", "head"], check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"Alembic upgrade failed: {e}")

