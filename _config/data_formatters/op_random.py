
import binascii
import os


def generate_random_key():
    return binascii.hexlify(os.urandom(40)).decode()
