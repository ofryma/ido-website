import os
import tempfile
from typing import List , Type
import base64
import json
import requests

from fastapi import UploadFile
import boto3



def decode_from_base64(base64_data)-> dict:
    decoded_bytes = base64.b64decode(base64_data)
    decoded_json = json.loads(decoded_bytes.decode())
    return decoded_json


def extract_object_key_bucket_name(s3_event: dict):

    object_key = ''
    bucket_name = ''

    return object_key , bucket_name

