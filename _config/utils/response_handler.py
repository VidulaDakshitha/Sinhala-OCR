from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse
import json
import decimal
# from onepay_config.utils import logger
from datetime import date, datetime


def response_formatter(response):
    if response['success']:
        status = "200"
    else:
        status = "400"

    return HttpResponse(
        json.dumps(response), status=status, content_type="application/json",
    )


def custom_response_formatter(response, status, is_log=True):
    # logger.log_info("USER REGISTER - POST - " + str(response))

    return HttpResponse(
        json.dumps(response,cls=DjangoJSONEncoder), status=status, content_type="application/json",
    )

def decimal_default(obj):
    if isinstance(obj, decimal.Decimal):
        return float(obj)
    raise TypeError


def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError ("Type %s not serializable" % type(obj))