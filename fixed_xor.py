import binascii
import base64

def fixed_xor(str1, str2):
    bytes1 = bytes.fromhex(str1)
    bytes2 = bytes.fromhex(str2)
    # decoded_str = ''.join([chr(b1 ^ b2) for b1, b2 in zip(bytearray(bytes1), bytearray(bytes2))])
    decoded_str = [b1 ^ b2 for b1, b2 in zip(bytearray(bytes1), bytearray(bytes2))]
    decoded_str = bytearray(decoded_str)
    return binascii.hexlify(decoded_str)
    #return base64.b64encode(decoded_str)


if __name__ == '__main__':
    test_str1 = '1c0111001f010100061a024b53535009181c'
    test_str2 = '686974207468652062756c6c277320657965'
    print(fixed_xor(test_str1, test_str2))
