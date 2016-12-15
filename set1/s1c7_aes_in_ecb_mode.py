#!/usr/bin/python3
import binascii
import base64
from Crypto.Cipher import AES


if __name__ == '__main__':
    msg = base64.b64decode(open('7.txt', 'r').read())
    key = b'YELLOW SUBMARINE'
    codec = AES.new(key, AES.MODE_ECB)
    print(codec.decrypt(msg))
