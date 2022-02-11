import boto3
from .date_time import get_timestamp
import base64
from django.core.files.base import ContentFile
import botocore
from botocore.client import Config
import io
from PIL import Image
from io import BytesIO
import numpy as np

import json
aws_access_key_id = ''
aws_secret_access_key = ''
aws_bucket_name = ''


def upload_image(file):
    filename = get_timestamp() + '.' + file.name.split('.')[-1]

    try:
        s3 = boto3.resource('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
        bucket = s3.Bucket(aws_bucket_name)
        bucket.put_object(Key=filename, Body=file, ACL='public-read')

        return {
            "success": True,
            "description": 'Image Uploaded',
            "data": {
                "filename": filename
            }
        }

    except Exception as ex:
        return {
            "success": False,
            "description": str(ex)
        }


def base64upload(img_data, customized_path=''):
    try:
        format, img_str = img_data.split(';base64,')
        ext = format.split('/')[-1]
        filename = get_timestamp() + '.' +ext

        data = ContentFile(base64.b64decode(img_str), name='temp.' + ext)
        s3 = boto3.resource('s3', aws_access_key_id=aws_access_key_id,
                            aws_secret_access_key=aws_secret_access_key)
        bucket = s3.Bucket(aws_bucket_name)
        bucket.put_object(Key=customized_path + filename, Body=data, ACL='public-read')

        return {
            "success": True,
            "description": 'Image Uploaded',
            "data": {
                "filename": customized_path + filename
            }
        }

    except Exception as ex:
        return {
            "success": False,
            "description": str(ex)
        }


def get_image(file):
    try:
        session = boto3.Session(aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_access_key_id)
        s3 = session.client('s3', config=Config(s3={'addressing_style': 'path'}), region_name='ap-southeast-1')
        url = s3.generate_presigned_url(ClientMethod='get_object', Params={'Bucket': aws_bucket_name, 'Key': file},
                                        ExpiresIn=10000)
        return {'url': url.split("?")[0]}
    except Exception as ex:
        return {'url': ''}


def get_image_base64(file):
    try:
        s3 = boto3.resource('s3', config=Config(signature_version='s3v4'),  aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
        bucket = s3.Bucket(aws_bucket_name)
        object = bucket.Object(file)
        response = object.get()
        file_stream = response['Body']
        im = Image.open(file_stream)

        in_mem_file = io.BytesIO()
        im.save(in_mem_file, format=im.format)
        in_mem_file.seek(0)
        img_bytes = in_mem_file.read()

        base64_encoded_result_bytes = base64.b64encode(img_bytes)
        base64_encoded_result_str = base64_encoded_result_bytes.decode('ascii')
        print(base64_encoded_result_str)
        return {
                "success": True,
                "description": 'Image found',
                "image": base64_encoded_result_str
            }

    except Exception as ex:
        return {
                "success": False,
                "description": 'Image not found' + str(ex),
            }


