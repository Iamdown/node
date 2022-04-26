# -*- coding: utf-8 -*-
'''
File Name:views.py
Program IDE:PyCharm
Create FIle Time:2022/4/23 21:00
File Create By Author:"祖华"
'''
from django.shortcuts import render

# 全局400、 403、404、500错误自定义页面显示

def bad_request(request,exception=None):
    return render(request, "400.html",status=400)

def permission_denied(request,exception=None):
    return render(request, '403.html',status=403)

def page_not_found(request,exception=None):
    return render(request, '404.html',status=404)

def page_error(request,exception=None):
    return render(request, '500.html',status=500)




