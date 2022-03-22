from django.urls import path,re_path
from . import views
app_name = 'user'  #APP命名空间
urlpatterns = [
               path('signin/',views.signin,name='signin'),#name参数为了给reverse 反转url路径
               path('register/',views.register,name='register'),
               path('forget/',views.forget,name='forget'),
               path('login_out/',views.login_out,name='login_out'),
               path('hello/',views.hello,name='hello'),
]