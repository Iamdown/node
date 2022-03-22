from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def newChat(request):
    return render(request,'chat/chat.html',locals())


def room(request,room_name):
    return render(request,'chat/room.html',locals())