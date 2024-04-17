from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import base64
from Crypto.Util import Counter
import binascii
from base64 import b64decode, b64encode


class AESEnCrpTor:
    # 定义密钥和明文
    # key = '34CC23EF3C094C22B01114B7F1050534'
    key = base64.b64decode('34CC23EF3C094C22B01114B7F1050534')

    # plaintext = bytearray('奶粉', encoding='utf-8')

    # 加密流程
    @staticmethod
    def aes_encrypt(data):
        plaintext = bytearray(data, encoding='utf-8')
        cipher = AES.new(AESEnCrpTor.key, AES.MODE_ECB)  # 创建新的cipher对象，使用ECB模式和定义的密钥
        ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))  # 对明文进行填充并加密
        encoded_ciphertext = base64.b64encode(ciphertext)  # 对加密后的密文进行base64编码
        # print('Ciphertext:', encoded_ciphertext.decode())  # 输出密文
        return encoded_ciphertext.decode()

    # 解密流程
    @staticmethod
    def aes_decrypt(data):
        decoded_ciphertext = base64.b64decode(data)  # 对密文进行base64解码
        cipher_dec = AES.new(AESEnCrpTor.key, AES.MODE_ECB)  # 创建新的cipher对象，使用ECB模式和定义的密钥
        decrypted_plaintext = unpad(cipher_dec.decrypt(decoded_ciphertext), AES.block_size)  # 对解码后的密文进行解密和去填充
        # print('Decrypted plaintext:', decrypted_plaintext.decode())  # 输出解密后的明文
        return decrypted_plaintext.decode()


class AESCipher:

    def __init__(self):
        self.key = '34CC23EF3C094C22'.encode()
        self.iv = '13CC29EF2C194CVC'.encode()

    def encrypt(self, text):
        text = text.encode()
        iv_int = int(binascii.hexlify(self.iv), 16)
        ctr = Counter.new(AES.block_size * 8, initial_value=iv_int)
        cipher = AES.new(key=self.key, mode=AES.MODE_CTR, counter=ctr)
        encrypted_text = cipher.encrypt(text)
        return b64encode(encrypted_text).decode('utf-8')

    def decrypt(self, encrypted_text):
        encrypted_text = b64decode(encrypted_text)
        iv_int = int(binascii.hexlify(self.iv), 16)
        ctr = Counter.new(AES.block_size * 8, initial_value=iv_int)
        cipher = AES.new(key=self.key, mode=AES.MODE_CTR, counter=ctr)
        decrypted_text = cipher.decrypt(encrypted_text)
        return decrypted_text.decode()

#
# aes = AESEnCrpTor()
#
# cipher = AESCipher()
# enc = cipher.encrypt("19857187478")
# print(enc)
# print(cipher.decrypt('EgZ/k2Gel3DaFLU='))
#
# print(aes.aes_encrypt('13916076548'))
# #
# print(aes.aes_decrypt('7M2+R9NX+lxcho/1UtPYjQ=='))
# # print(aes.aes_encrypt('13461600557'))
