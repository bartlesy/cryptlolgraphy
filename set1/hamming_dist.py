#!/usr/bin/python3
import binascii


def str_2_bin(in_str):
    in_bytes = bytes(in_str, 'utf-8')
    return bin(int(binascii.hexlify(in_bytes), 16))


def hamming_dist(in1, in2):
    if len(in1) != len(in2):
        raise ValueError
    if isinstance(in1, str):
        bin1 = str_2_bin(in1)
    else:
        bin1 = in1
    if isinstance(in2, str):
        bin2 = str_2_bin(in2)
    else:
        bin2 = in2
    return sum([1 if b1 != b2 else 0 for b1, b2 in zip(bin1, bin2)])


if __name__ == '__main__':
    test_strs = ['this is a test', 'wokka wokka!!!']
    print(hamming_dist(*test_strs))
