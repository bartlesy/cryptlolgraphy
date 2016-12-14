#!/usr/bin/python3
import binascii
import base64
import itertools
from hamming_dist import hamming_dist, str_2_bin
from s1c4_detect_single_char_xor import read_file
from s1c5_rep_key_xor import rep_xor
from s1c2_fixed_xor import fixed_xor
from s1c3_crack_single_byte_xor import hax_the_gibson


def get_byte_blocks(in_bytes, keysize):
    blocks = []
    for start, stop in zip(range(0, len(in_bytes), keysize),
                           range(keysize, len(in_bytes), keysize)):
        blocks.append(in_bytes[start:stop])
    return blocks


def find_best_keysize(in_bytes, lb=2, ub=40, scorer=hamming_dist):
    ub = ub + 1
    res = {}
    for k in range(lb, ub):
        blocks = get_byte_blocks(in_bytes, k)
        pairs = list(itertools.combinations(blocks, 2))[:10]
        res[k] = sum((scorer(*pair) / k for pair in pairs)) / 10
    return min(res, key=res.get)


def find_key(blocks, keysize):
    key = b''
    for k in range(keysize):
        k_bytes = bytearray([block[k] for block in blocks])
        key += bytes([hax_the_gibson(k_bytes)[0]])
    return key


if __name__ == '__main__':
    fp = './6.txt'

    in_bytes = base64.b64decode(open(fp, 'r').read())

    keysize = find_best_keysize(in_bytes)
    blocks = get_byte_blocks(in_bytes, keysize)
    key = find_key(blocks, keysize)
    print('Key is {}'.format(key)) # byte object of key

    message = bytes.fromhex(rep_xor(in_bytes, key).decode())
    print('Message: {}'.format(message))

