#!/usr/bin/python3
from itertools import cycle
import binascii


def rep_xor(in_txt, key=b'ICE'):
    if isinstance(in_txt, str):
        in_bytes = bytes(in_txt, 'utf-8')
    else:
        in_bytes = in_txt
    res = bytearray([b1 ^ b2 for b1, b2 in zip(in_bytes, cycle(key))])
    return binascii.hexlify(res)

if __name__ == '__main__':
    test_str = "Burning 'em, if you ain't quick and nimble" + \
        " I go crazy when I hear a cymbal"
    print(test_str)
    print(rep_xor(test_str, b'ICE'))
