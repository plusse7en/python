from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import base64
from Crypto.Util import Counter
import binascii
from base64 import b64decode, b64encode

text = 'abc'
text = text.encode()

iv = '13CC29EF2C194CVC'
iv = iv.encode()
print(iv)

iv = binascii.hexlify(iv)
print(iv)
iv = int(iv, 16)
print(iv)

ctr = Counter.new(AES.block_size * 8, initial_value=iv)
print('ctr:')
print(ctr)

key = '34CC23EF3C094C22'.encode()
cipher = AES.new(key=key, mode=AES.MODE_CTR, counter=ctr)
print('cipher:')
print(cipher)

encrypted_text = cipher.encrypt(text)
print('encrypted_text:')
print(encrypted_text)

x = b64encode(encrypted_text)
print(x)
x = x.decode('utf-8')
print(x)
