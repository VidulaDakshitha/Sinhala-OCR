<<<<<<< HEAD
import datetime


def get_unique_ascii():
    timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')
    hexadecimals = hex(int(timestamp))
    unique_id = hexadecimals[2:]
    return str(unique_id)


def get_formatted_current_time():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
=======
import datetime


def get_unique_ascii():
    timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')
    hexadecimals = hex(int(timestamp))
    unique_id = hexadecimals[2:]
    return str(unique_id)


def get_formatted_current_time():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
>>>>>>> 6fdea339c7f895bce85ebd2b0f591197f7649f4d
