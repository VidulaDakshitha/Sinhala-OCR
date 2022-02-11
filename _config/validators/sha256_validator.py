
import hashlib
import json


def json_validator(json_obj, hash_value):
    try:
        request_str = str(json_obj)
        print(request_str)
        request_str = request_str.replace("\'", "\"")
        request_str = request_str.replace(" ", "")
        print(request_str)
        request_hash = hashlib.sha256(request_str.encode("utf-8")).hexdigest()
        print(request_hash, 'request_hash')
        print(hash_value, 'hash_value')

        if request_hash == hash_value:
            return True
        else:
            return False

    except Exception as ex:
        print('Error: SHA256_Validator: ', ex)
        return False


def json_validator_with_salt(json_obj, hash_value, salt):
    try:
        request_str = str(json_obj)
        print(request_str)
        request_str = request_str.replace("\'", "\"")
        request_str = request_str.replace(" ", "")
        print(request_str)
        request_hash = hashlib.sha256(request_str.encode("utf-8") + salt.encode("utf-8")).hexdigest()

        print('REQUEST HASH', request_hash)

        if request_hash == hash_value:
            return True
        else:
            return False

    except Exception as ex:
        print('Error: SHA256_Validator: ', ex)
        return False


def json_to_sha256(json_obj):
    try:
        request_str = str(json_obj)
        request_str = request_str.replace("\'", "\"")
        request_str = request_str.replace(" ", "")

        request_hash = hashlib.sha256(request_str.encode("utf-8")).hexdigest()

        return request_hash
    except Exception as ex:
        print('Error: SHA256_generator: ', ex)
        return ""


def json_to_sha256_with_salt(json_obj, salt):
    try:
        request_str = str(json_obj)
        request_str = request_str.replace("\'", "\"")
        request_str = request_str.replace(" ", "")

        request_hash = hashlib.sha256(request_str.encode("utf-8") + salt.encode("utf-8")).hexdigest()

        return request_hash
    except Exception as ex:
        print('Error: SHA256_generator: ', ex)
        return ""

def valid(data,num):

    if data == "sample":
        arr_test=["test1","test1","test1","test1","test1","test1","test1","test1","test1","test1","test1"]
        return arr_test[num]
    elif data == "sample3":
        arr_test2=["අයදුම්කරුගේ නම සහ ලිපිනය","සම්පූර්ණ නම","ස්ථාවර දුරකථන අංකය ","ස්ත්‍රි පුරුෂභාවය","විභාගයේ නම","වර්ශය","විභාග අංකය","භාශාව","විභාග ස්ථානය","විභාග ස්ථාන අංකය","යැවිය යූතු ලිපිනය"]
        return arr_test2[num]
