"""
    Module contains hex to b64 conversion function.
    Set 1 Challenge 1 of Cryptopals Crypto Challenges
"""
from binascii import a2b_hex, b2a_base64

def hex2base64(hex_string):
    """
        param: hex string
        return: base64 converted
    """
    return b2a_base64(a2b_hex(hex_string))

print hex2base64(raw_input())
