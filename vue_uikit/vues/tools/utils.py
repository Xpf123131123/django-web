from django.contrib.auth.hashers import make_password, check_password

SALT = 'vues_tools_utils_salt'


# 密码加密
def data_encrypt(pw):
    return make_password(pw, SALT)


# 验证密码是否正确
def data_decrypt(pw, salt_pw):
    return check_password(pw, salt_pw)
