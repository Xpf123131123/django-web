from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class User(models.Model):
    # 用户名
    username = models.CharField(max_length=30)
    # 密码
    password = models.CharField(max_length=200)
    # 邮箱
    email = models.CharField(max_length=200)

    def __str__(self):
        return 'username={us}\npassword={pd}\nemail={em}'\
            .format(us=self.username, pd=self.password, em=self.email)