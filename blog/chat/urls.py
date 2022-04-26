# -*- coding: utf-8 -*-
'''
File Name:urls.py
Program IDE:PyCharm
Create FIle Time:2022/3/19 02:39
File Create By Author:"祖华"
'''
from django.urls import path
from . import views
app_name = 'wechat'  #APP命名空间

urlpatterns = [
    path('newchat/',views.newchat,name="newchat"),
    path('<room_name>/',views.room,name='room'),
]