"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from .consumers import ChatConsumer
#from django.views import static ##新增
from django.conf import settings ##新增
from django.conf.urls import url ##新增
from django.views.static import serve
from .views import page_not_found,permission_denied
#page_error
urlpatterns = [

    path('admin/', admin.site.urls),
    path('',include('index.urls')),
    path('user/',include('user.urls')),
    path('chat/', include('chat.urls')),
    #settings文件debug设置为False之后需要配置的两个路径
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT},name='media'),
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}, name='static'),

]

#聊天功能
web_socket_urlpatterns = [
    path('ws/chat/<room_name>/',ChatConsumer)
]


# 定义错误跳转页面
handler403 = permission_denied
handler404 = page_not_found
# handler500 = page_error