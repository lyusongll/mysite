#!usr/bin/env python
# -*- coding:utf-8 -*-
from django import forms
# from django.contrib.auth.models import User
# from .models import UserProfile

# 自定义的登录，暂时不用，采用内置的登录
class LoginForm(forms.Form):#提交表单之后不对数据库进行修改
    username = forms.CharField()
    password = forms.CharField(widget = forms.PasswordInput)


