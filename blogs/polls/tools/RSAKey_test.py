from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.PublicKey import RSA
from Crypto import Random
import base64


message = b'hello django asjdasjdlkajlksdj a'
print('加密前数据:', message)
with open('master-public.pem') as f:
    key = f.read()
    rsakey = RSA.importKey(key)
    cipher = Cipher_pkcs1_v1_5.new(rsakey)
    cipher_text = base64.b64encode(cipher.encrypt(message))

    # print(cipher_text)

random_generator = Random.new().read

with open('master-private.pem') as f:
    key = f.read()
    rsakey = RSA.importKey(key)
    cipher = Cipher_pkcs1_v1_5.new(rsakey)
    text = cipher.decrypt(base64.b64decode(cipher_text), random_generator)
    print('解密后数据:', text)


if __name__ == '__main__':
    pass