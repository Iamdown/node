from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib.auth.models import User

def newchat(request):
    return render(request,'chat/chat.html',locals())


def room(request,room_name):
    cur_user = request.user.username
    user_objs = User.objects.all()
    total = len(user_objs)
    return render(request,'chat/room.html',locals())