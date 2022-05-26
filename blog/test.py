# -*- coding: utf-8 -*-
'''
File Name:test.py
Program IDE:PyCharm
Create FIle Time:2022/4/28 10:09
File Create By Author:"祖华"
'''
def application(env, start_response):
    start_response('200 OK', [('Content-Type','text/html')])
    return [b"Hello World"] # python3