from django.http import HttpResponse
from django.core.serializers.json import DjangoJSONEncoder
import json
import decimal
from _config.encription_handler import request_response_encriptor


def custom_response_formatter(response, status, is_encryption=False, is_log=False):
    if is_log:
        print('RESPONSE', str(response))

    if is_encryption:
        return HttpResponse(
            request_response_encriptor.encrypt_request(response), status=status, content_type="text/plain",
        )
    else:
        return HttpResponse(
            json.dumps(response,cls=DjangoJSONEncoder), status=status, content_type="application/json",
        )


def decimal_response_formatter(response, status, is_encryption=False, is_log=False):
    if is_log:
        print('RESPONSE', str(response))

    if is_encryption:
        return HttpResponse(
            request_response_encriptor.encrypt_request(response), status=status, content_type="text/plain",
        )
    else:
        return HttpResponse(
            json.dumps(response, default=decimal_default), status=status, content_type="application/json",
        )


def decimal_default(obj):
    if isinstance(obj, decimal.Decimal):
        return float(obj)
    raise TypeError


