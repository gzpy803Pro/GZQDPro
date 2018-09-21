import re

from django import forms
from django.core.exceptions import ValidationError

from user.models import UserProfile


class UserForm(forms.ModelForm):
    # 添加模型不存在的字段(页面表单中存在的)
    password2 = forms.CharField(label='重复口令', max_length=20, min_length=8,
                                error_messages={'required': '重复口令不能为空',
                                                'min_length': '长度不能少于8位',
                                                'max_length': '长度不能少于20位'
                                                })

    class Meta:
        model = UserProfile
        fields = '__all__'   # ['username', 'password']

        error_messages = {
            'username':{
                'required': '账号不能为空',
                'max_length': '长度不能超过20个字符'
            },
            'password':{
                'required': '口令不能为空'
            },
            'nick_name': {
                'required': '别名不能为空'
            },
            'phone': {
                'required': '手机号不能为空'
            }
        }

    def clean_username(self):  # 所有默认规则都验证通过，才会进入自定义验证
        username = self.cleaned_data.get('username')
        print('---clean_username----')
        if len(username) < 6:
            raise ValidationError('长度不能少于6位')

        # 再验证起始的字符是否为字母
        char_ = username[0]
        if not re.match(r'[a-zA-Z]', char_):  # match与search及findall函数的区别
            raise ValidationError('账号必须是以字母开头')
        return username

    def clean_password2(self):
        p1 = self.cleaned_data.get('password')
        p2 = self.cleaned_data.get('password2')

        if p1 != p2:
            raise ValidationError('两次口令不相同')

        return p1