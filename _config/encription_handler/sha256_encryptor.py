<<<<<<< HEAD
from hashlib import sha256


def encrypt_string(hash_string):
    hash_string=remove_spaces(hash_string)

    sha_signature = sha256(hash_string.encode('utf-8')).hexdigest()
    return sha_signature


def remove_spaces(string):
    key = "9I5C1187AE98266CF5E66"
    sequence = str(string)+key

    sequence=sequence.replace(" ", "")
    sequence = sequence.replace("\'", "\"")
    return sequence


# hash_string = 'confidential data'
# hash_string=remove_spaces(hash_string)
# sha_signature = encrypt_string(hash_string)
# print(sha_signature)
=======
from hashlib import sha256


def encrypt_string(hash_string):
    hash_string=remove_spaces(hash_string)

    sha_signature = sha256(hash_string.encode('utf-8')).hexdigest()
    return sha_signature


def remove_spaces(string):
    key = "9I5C1187AE98266CF5E66"
    sequence = str(string)+key

    sequence=sequence.replace(" ", "")
    sequence = sequence.replace("\'", "\"")
    return sequence


# hash_string = 'confidential data'
# hash_string=remove_spaces(hash_string)
# sha_signature = encrypt_string(hash_string)
# print(sha_signature)
>>>>>>> 6fdea339c7f895bce85ebd2b0f591197f7649f4d
