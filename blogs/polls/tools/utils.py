import base64
from django.contrib.auth.hashers import make_password, check_password
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.PublicKey import RSA
from Crypto import Random


SALT = 'polls_tools_utils_salt'


# 密码加密
def password_encrypt(pw):
    return make_password(pw, SALT)


# 验证密码是否正确
def password_decrypt(pw, salt_pw):
    return check_password(pw, salt_pw)


def decrypt(data):

    random_generator = Random.new().read
    with open('master-private.pem') as f:
        key = f.read()
        rsa_key = RSA.importKey(key)
        cipher = Cipher_pkcs1_v1_5.new(rsa_key)
        text = cipher.decrypt(base64.b64decode(data), random_generator)
        return text




