from django.db import models

# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


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


