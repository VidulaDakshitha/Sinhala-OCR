import datetime
import dateutil.parser

def get_today_date():
    today = datetime.datetime.today()
    return str(today.year)+'-'+str(today.month)+'-'+str(today.day)


def get_timestamp():
    ts = datetime.datetime.now().timestamp()
    return str(ts)


def get_formatted_current_time():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

def get_token_expire_date():
    current_datetime = get_formatted_current_time()
    current_date_time=dateutil.parser.parse(current_datetime)
    expired_time = current_date_time + datetime.timedelta(days=30,hours=0,minutes=0,seconds=0)
    return expired_time.strftime("%Y-%m-%d %H:%M")

