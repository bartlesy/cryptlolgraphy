#!/usr/bin/python3
import binascii
import base64
from hamming_dist import hamming_dist, str_2_bin
from s1c4_detect_single_char_xor import read_file
from s1c5_rep_key_xor import rep_xor
from s1c2_fixed_xor import fixed_xor
from s1c3_crack_single_byte_xor import hax_the_gibson


def get_first_byte_blocks(in_bytes, keysize):
   block1 = in_bytes[:keysize].decode('utf-8')
   block2 = in_bytes[keysize:(2 * keysize)].decode('utf-8')
   return (block1, block2)


def get_byte_blocks(in_bytes, keysize):
    blocks = []
    for start, stop in zip(range(0, len(in_bytes), keysize),
                           range(keysize, len(in_bytes), keysize)):
        blocks.append(in_bytes[start:stop])
    return blocks


def find_best_keysize(in_bytes, lb=2, ub=40, scorer=hamming_dist):
    ub = ub + 1
    # res = {k: scorer(*next(get_byte_blocks(in_bytes, k))) / k for k in range(lb, ub)}
    res = {k: scorer(*get_first_byte_blocks(in_bytes, k)) / k for k in range(lb, ub)}

    ###
    for asdf in res.items():
        print(asdf)
    ###

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
    print(key, type(key)) # byte object of key
    print(binascii.hexlify(key)) # hex of hte key
    print(rep_xor(in_bytes, key)) # returns byte object
