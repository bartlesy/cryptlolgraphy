#!/usr/bin/env python3
import binascii


char_freq = {
    'e': 27,
    't': 26,
    'a': 25,
    'o': 24,
    'i': 23,
    'n': 22,
    's': 21,
    'r': 20,
    'h': 19,
    'l': 18,
    'd': 17,
    'c': 16,
    'u': 15,
    'm': 14,
    'f': 13,
    'p': 12,
    'g': 11,
    'w': 10,
    'y': 9,
    'b': 8,
    'v': 7,
    'k': 6,
    'x': 5,
    ' ': 4,
    'j': 3,
    'q': 2,
    'z': 1
}


def xor_singlechar(in_bytes, key):
    return bytearray([b ^ key for b in in_bytes])


def score_output(xored_bytes):
    return sum([char_freq.get(chr(b), 0) for b in xored_bytes])


def hax_the_gibson(input_str):
    in_bytes = bytes.fromhex(input_str)
    scores = {key: [score_output(xor_singlechar(in_bytes, key)),
                  xor_singlechar(in_bytes, key)] for key in range(256)}
    best = max(scores, key=lambda x: scores.get(x)[0])
    return best, scores[best]


if __name__ == '__main__':
    test_string = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
    print(hax_the_gibson(test_string))
