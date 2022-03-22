# -*- coding: utf-8 -*-
'''
File Name:urls.py
Program IDE:PyCharm
Create FIle Time:2022/3/19 02:39
File Create By Author:"祖华"
'''
from django.urls import path
from .views import *
app_name = 'wechat'  #APP命名空间

urlpatterns = [

    path('newChat/',newChat,name="newChat"),
    path('<room_name>/',room,name='room'),
]