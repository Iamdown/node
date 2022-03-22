# -*- coding: utf-8 -*-
'''
File Name:routing.py
Program IDE:PyCharm
Create FIle Time:2022/3/18 17:53
File Create By Author:"祖华"
'''
# 在项目名同名的文件夹下创建routing.py文件并在该文件内提前写好以下代码
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter
from channels.routing import URLRouter
from .urls import web_socket_urlpatterns
'''
django 连接channels的路由
'''
application =ProtocolTypeRouter({
    'websocket':AuthMiddlewareStack(
        URLRouter(web_socket_urlpatterns)
                                    ),
})
