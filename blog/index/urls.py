from django.urls import path,re_path,include
from . import views
app_name = 'index'  #APP命名空间

urlpatterns = [
               path('',views.index,name='index'),
               path('detail/<int:pk>',views.detail,name='detail'),
               path('add_comment/', views.add_comment, name='add_comment'),
               path('delete_comment/',views.delete_comment,name='delete_comment'),
               path('edit_comment/',views.edit_comment,name='edit_comment'),
               path('get_comment/<int:pk>', views.get_comment, name='get_comment'),
               path('blog/<str:c_name>',views.blog,name='blog'),
               path('post/',views.post,name='post'),
               path('contact/',views.contact,name='contact'),
               path('categroy/',views.categroy,name='categroy'),
               path('publish/',views.publish,name='publish'),
               path('center/',views.center,name='center'),
               path('mdeditor/', include('mdeditor.urls')),
               path('mymd/', views.MyBlogMd.as_view()),
               path('coderain/',views.coderain,name='coderain'),


               # #?P分组的命名模式，取此分组中的内容时可以使用索引也可以使用name
               # re_path('(?P<year>[0-9]{4}).html',views.myyear,name='myyear'),
               # re_path('(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/(?P<day>[0-9]{1,2}).html',views.mydate,name='mydate'),

               ]