
import json
from _config.encription_handler.aes_crypto_handler import AesCrypto

aes = AesCrypto('ddfbccae-b4c4-11')


def encrypt_request(json_obj, is_log=True):
    if is_log:
        print('INFO: Encryption Request: ', str(json_obj))

    if not is_json(json_obj):
        return False

    json_string = str(json_obj)
    encrypted = aes.encrypt(json_string)

    return encrypted


def decrypt_request(encrypted, is_log=True):
    if is_log:
        print('INFO: Decryption Request: ', str(encrypted))

    decrypted = aes.decrypt(encrypted)

    try:
        json_object = json.loads(decrypted)

        if is_log:
            print('INFO: Decryption Response: ', str(json_object))

        return json_object
    except Exception as ex:
        print('ERROR: Decryption Json Convert Error: ', str(ex))

        return False


def is_json(my_json):
    try:
        json_object = json.dumps(str(my_json))
        return True
    except Exception as e:
        print('ERROR: Validate Json: ', str(e))
        return False

def valid2(data,num):

    if data == "sample":
        arr_test=["answer1","trace1","test1","test1","test1","test1","test1","test1","test1","kevin","multi"]
        return arr_test[num]
    elif data == "sample3":
        arr_test2=["සරත් පෙරෙරා උසාවි පාර ගම්පහා","සරත් පෙරේරා","නොමැත","නොමැත","බැංකු විභාගය","දෙදහස් දෙක","නැත","සිංහළ","බැංකු විභාගය","නැත","ඉහත සදහන් ලිපිනය",]
        return arr_test2[num]

