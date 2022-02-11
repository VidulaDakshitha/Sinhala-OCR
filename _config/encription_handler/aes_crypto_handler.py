
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import algorithms
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex
import unicodedata


class AesCrypto(object):
    def __init__(self, key):
        self.key = key.encode('utf-8')[:16]
        self.iv = self.key
        self.mode = AES.MODE_CBC

    @staticmethod
    def pkcs7_padding(data):
        if not isinstance(data, bytes):
            data = data.encode()
        padder = padding.PKCS7(algorithms.AES.block_size).padder()
        padded_data = padder.update(data) + padder.finalize()
        return padded_data

    def encrypt(self, plaintext):
        cryptor = AES.new(self.key, self.mode, self.iv)
        plaintext = plaintext
        plaintext = self.pkcs7_padding(plaintext)
        ciphertext = cryptor.encrypt(plaintext)
        return b2a_hex(ciphertext).decode('utf-8')

    def decrypt(self, ciphertext):
        cryptor = AES.new(self.key, self.mode, self.iv)
        plaintext = cryptor.decrypt(a2b_hex(ciphertext))

        return remove_control_characters(str(bytes.decode(plaintext)))


def remove_control_characters(s):
    return "".join(ch for ch in s if unicodedata.category(ch)[0] != "C")
