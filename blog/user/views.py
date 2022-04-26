import random
from django.shortcuts import render,redirect,reverse,get_object_or_404
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
# Create your views here.

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
import json
from django.contrib.auth.hashers import make_password
from functools import wraps# 导入用于装饰器修复技术的包
#from django.core.mail import send_mail

#登录
def signin(request):
    result = {"status": False, "error": {"user_error": "", "pwd_error": "", "login_error": ""}, "username": None,'url':None}
    if request.method == 'GET':
        return render(request, 'user/signin.html')
    elif request.method == 'POST':
        name = request.POST.get('user')
        pwd = request.POST.get('pwd')

        if name:
            name = name.strip()
            user_obj = User.objects.filter(username=name).first()#查询是否存在该用户名
            if not user_obj:
                result["error"]["user_error"]  = "用户名错误或者不存在"
        else:
            result["error"]["user_error"] = "用户名不能为空"
        if pwd=="":
            result["error"]["pwd_error"] = "密码不能为空"
        else:
            user = authenticate(username=name, password=pwd)#校验用户名和密码是否正确
            if user and user.is_active:
                result["status"] = True
                login(request, user)
                result["url"] = 'http://127.0.0.1/'
                response = HttpResponse(json.dumps(result))
                response.set_signed_cookie("is_login","1",salt="ban",
                                           # max_age=100
                                           )#salt 加盐密 max_age cookie有效时长
                request.session["is_login"] = "1"
                return response
            else:
                result["error"]["pwd_error"] = "密码不正确"
        return HttpResponse(json.dumps(result))

#退出
def login_out(request):
    logout(request)
    return redirect('user:signin')

#注册
def register(request):
    result = {"username":None,"password":None,"email":None}
    if request.method=='GET':
        return render(request, './user/register.html')
    else:
        userName = request.POST.get('userName')
        if not userName:
            result['username'] = "用户名不能为空"
        userPassword = request.POST.get('userPassword')
        if not userPassword:
            result['password'] = "密码不能为空"
        email = request.POST.get('userEmail')
        if not email:
            result['email'] = "邮箱不能为空"
        user = User.objects.filter(username=userName).first()  # 查询是否存在该用户名
        if not user and userName and userPassword and email:
            User.objects.create_user(username= userName, password= userPassword,email= email)
            return render(request,'user/signin.html',context={"message":"注册成功 请登录"})
        else:
            return render(request,'user/register.html',context={"message":"注册失败"})



#忘记密码
def forget(request):
    result =  {'status':'','tips':'','button':''}
    if request.method=='GET':
        request.session.clear()
    elif request.method == 'POST':
        u = request.POST.get('username')
        vcode = request.POST.get('vcode')
        p = request.POST.get('password')
        if not u:
            result['tips'] = "username can't be blank"
            result['status'] = False
        else:
            user = User.objects.filter(username=u)
            #用户不存在
            if not user:
                result['tips'] = '用户名不存在'
                result['status'] = False
                # 判断验证码是否已经发送
            elif not request.session.get('vcode'):
                    # 发送验证码并将验证码写入session
                    result['button'] = '重置密码'
                    result['tips'] = '验证码已发送 请查收邮件'
                    result['status'] =True
                    vcode = str(random.randint(1000,9999))
                    request.session['vcode'] = vcode
                    user[0].email_user('找回密码',vcode)
            #匹配输入的验证码是否正确
            elif vcode == request.session.get('vcode'):
                    #密码加密处理并保存到数据库
                    dj_ps = make_password(p,None,'pbkdf2_sha256')
                    user[0].password = dj_ps
                    user[0].save()
                    del request.session['vcode']
                    result['tips'] = '密码已重置'
                    result['status'] = True
                    request.session.clear()
            else:
                    result['tips'] = '验证码错误,请重新获取'
                    result['status'] = False
                    request.session.clear()

        return HttpResponse(json.dumps(result))
    return render(request, 'user/forget.html', context=result)




# 装饰器函数，用来判断是否登录
def check_login(func):
    @wraps(func)  # 装饰器修复技术
    def inner(request, *args, **kwargs):
        cookie = request.get_signed_cookie("is_login", default=None, salt="ban")
        session = request.session.get("is_login",default=None)
        if cookie and session and cookie==session:
            # 已经登录，继续执行
            return func(request, *args, **kwargs)
        # 没有登录过
        else:
            # ** 即使登录成功也只能跳转到home页面，现在通过在URL中加上next指定跳转的页面
            # 获取当前访问的URL
            return redirect('user:login')
    return inner

def hello(request):
        return HttpResponse('Hallo!')

