from django.contrib.auth.hashers import make_password
from django.db import models


# Create your models here.
class UserProfile(models.Model):
    username = models.CharField(max_length=20, verbose_name='账号')
    password = models.CharField(max_length=100, verbose_name='口令')
    nick_name = models.CharField(max_length=20, verbose_name='别名')
    phone = models.CharField(max_length=11, verbose_name='手机号')
    photo = models.CharField(max_length=100,
                             verbose_name='头像',
                             blank=True,
                             null=True)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if len(self.password) < 50:  # 判断密码是否为明文
            self.password = make_password(self.password)

        super().save()

    class Meta:
        db_table = 't_user'
        verbose_name = '用户'
        verbose_name_plural = verbose_name



