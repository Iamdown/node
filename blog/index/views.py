from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .models import Artical,Categroy,Comment
from .pages import MyPage
from .settings import page_num_show,per_page_num
import requests
from urllib.parse import quote
import json
import ssl
import re
import uuid
from lxml import etree
import markdown
from django.utils.text import slugify
from markdown.extensions.toc import TocExtension
from django.shortcuts import get_object_or_404, render
from datetime import datetime
import time
import string
from django.contrib.auth.models import User
from django.db.models import Q
from haystack.views import SearchView
from drf_haystack.viewsets import HaystackViewSet
from django.core.paginator import Paginator
from .serializer import *
ssl._create_default_https_context = ssl._create_unverified_context
headers ={"user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"}


def get_baidu_new():
    header = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "default",
        "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Cookie": 'BIDUPSID=87F2E50C4E02FFA062334CC605BAF47F; PSTM=1650046794; BD_UPN=123253; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BAIDUID=87F2E50C4E02FFA07135C8C76EA73E59:SL=0:NR=10:FG=1; sug=0; sugstore=0; ORIGIN=2; bdime=0; H_PS_PSSID=31254_34813_35914_36165_34584_36120_36074_36126_36297_36233_26350_35868_22157_36061; delPer=0; BD_CK_SAM=1; PSINO=1; BD_HOME=1; COOKIE_SESSION=8832_0_7_7_7_6_1_0_7_3_0_3_8999_0_174_0_1650115078_0_1650114904%7C8%230_0_1650114904%7C1; av1_switch_v3=0; ariaDefaultTheme=undefined; RT="z=1&dm=baidu.com&si=up4913lg8po&ss=l21w3ecc&sl=2&tt=w1&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=1zn&ul=5j7&hd=5k2"; channel=baidusearch; baikeVisitId=fa50f9f3-c814-43ae-924d-32dd80dc0ab1; ab_sr=1.0.1_ZmFiM2ExZjQ1NWZjNDg5YmQ1MWMyNTBhZTc2YTgzOTc2ZmM1NmNjM2U1ZjExNjgzZTc3Y2RiMmI0MDQ1MzE5ZDM5MGYyNTE3MTFhYmMwMDUzYjU4MGQ5OGJiYmIwMjJmNDk5NjU4MWEyNjczZjRhMDVkYmQwODcyNzE0NDJkODkwMmQ1OGM4NmM4NDY2ZmQ3ZDRmNDIxODU4MGM0M2FhZg==; BDRCVFR[S4-dAuiWMmn]=mk3SLVN4HKm; H_PS_645EC=a0ecV2AdgOGSqUjO7TfMYaRjZ2sfp82RYc9LOvp%2FNMGlTFRTdMOQ%2F1tVyKhOsYtArg; BA_HECTOR=802g2l8h8421al85tl1h5lhf00q',
        "Host": "www.baidu.com",
        "Pragma": "no-cache",
        "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"macOS"',
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36",
    }
    url = "https://www.baidu.com"
    res = requests.get(url=url,headers=header)
    element = etree.HTML(res.text)
    other_title =  json.loads(element.xpath("//textarea[@id='hotsearch_data']/text()")[0])["hotsearch"]
    url_list = []
    for item  in other_title:
        title = item["pure_title"]
        url = f"https://www.baidu.com/s?wd={title}"
        url = quote(url,safe=string.printable)
        # res = requests.get(url=url,headers=headers)
        # res.encoding = "gb2312"
        # element = etree.HTML(res.text)
        # try:
        #     ture_url = element.xpath("//div[@id='content_left']/div//p[@class='title_2e25d']/a/@href")[0]
        # except Exception as e:
        #     print(e)
        #     ture_url = ''
        # print(title,ture_url)

        data_dict ={title:url}
        url_list.append(data_dict)
    return url_list


def get_keke_htm():

    url = 'http://www.kekenet.com/'
    response =  requests.get(url=url,headers=headers).content.decode('utf-8')
    selector = etree.HTML(response)
    news_time = selector.xpath('//ul[@id="con1"]//li//span[@class="list_date"]/text()')
    news_title = selector.xpath('//ul[@id="con1"]//li//span[@class="f14"]/a/text()')
    urls = selector.xpath('//ul[@id="con1"]//li//span[@class="f14"]/a/@href')
    content_list= []
    for n in range(len(news_time)):
        time = news_time[n]
        title = news_title[n]
        url = "http://www.kekenet.com"+urls[n]
        html = requests.get(url=url,headers=headers).content.decode('utf-8')
        selector= etree.HTML(html)
        p_text = selector.xpath('//div[@id="article"]//descendant::text()')
        artical_text =''
        for i in p_text:
           if i!='\n':
               artical_text+=i
               artical_text+='\n'
        data_dict= {'time':time,'title':title,'url':url,'artical':artical_text}
        content_list.append(data_dict)
    return content_list


#获取背景图片
def get_404_background_img(request):

    url ="https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&nc=1621244458742&pid=hp&uhd=1&uhdwidth=3840&uhdheight=2160"
    res = requests.get(url=url,headers=headers)
    img_data = json.loads(res.text)
    if img_data:
       img_url =  "https://www.bing.com"+img_data['images'][0]['url']
       return render(request,'404.html',{"img_url":img_url})

#获取背景图片
def get_500_background_img(request):

    url = 'https://cn.bing.com/HPImageArchive.aspx?format=hp&idx=0&n=1&nc=1621337488211&pid=hp&FORM=BEHPTB&ensearch=1&quiz=1&og=1&uhd=1&uhdwidth=3840&uhdheight=2160&IG=8B725D5CD1E04A15B34B936E77EBDC49&IID=SERP.1050'
    res = requests.get(url=url,headers=headers)
    selector  =  etree.HTML(res.text)
    text = selector.xpath('//div[@class="json"]/text()')[0]
    img_data = json.loads(text)
    if img_data:
       img_url =  "https://www.bing.com"+img_data['images'][0]['url']
       return  render(request,'500.html',{"img_url":img_url})

#获取每日内容
def get_sentence():

    url = "http://sentence.iciba.com/api/sentence/list?app_type=0&brand=apple&ck=07f3b2d0a7b9e8d3cc9ab93d8d87144f&client=3&client_ua=Mozilla%252F5.0%2520%2528iPhone%253B%2520CPU%2520iPhone%2520OS%252014_4_1%2520like%2520Mac%2520OS%2520X%2529%2520AppleWebKit%252F605.1.15%2520%2528KHTML%252C%2520like%2520Gecko%2529%2520Mobile%252F15E148%2520iciba_iPhone&deviceBrand=iPhone&deviceId=5126660zA84uzC5x42F0uz0-8353231260ef&dip=3&height=2688&identity=4&idfa=unknown&key=1000003&lang=en_CN&limit=1&loginToken=33733581&mcc=460&mnc=11&model=iPhone11%2C6&nonce=64894&nt=1&setup_time=0&signature=dfed97b0dd3674ff067d14f67974105b&sourceId=2&sv=iOS14.4.1&timestamp=1618063003&tzone=%2B0800&uid=33733581&uuid=5126660zA84uzC5x42F0uz0-8353231260ef&v=11.0.9&width=1242"
    response = requests.get(url=url,headers=headers)
    res = response.text
    s = json.loads(res)
    datas = s['data']['sentenceViewList']
    dailysentence = datas[0]['dailysentence']
    content = dailysentence['content']
    note = dailysentence['note']
    return content,note



class BlogSearchViewSet(HaystackViewSet):

    """
    返回博客文章搜索列表

    """
    index_models = [Artical]
    serializer_class = BlogIndexSerializer

#搜索
class BlogSearchView(SearchView):
    # 重写template的位置
    template = 'search/search.html'

    def get_context(self):
        context = super(BlogSearchView, self).get_context()
        results = self.results
        # 当搜索引擎找不到时，重新从数据库中找一遍
        if results.__len__() <= 1:
            results = []
            search_blogs = Artical.objects.filter(Q(a_title__contains=self.query) | Q(a_content__icontains=self.query)).order_by('-a_publish_date')
            for search_blog in search_blogs:
                results.append( search_blog)
            # 将result结果返回为Blog列表   #results.values('object')
        else:
            results = [blog["object"] for blog in results.values("object")]
        total = len(results)
        context.update({
            'title': '博客搜索',
            'results': results,
            'total':total,
        })
        return context

#简单全文搜索
def search_simple(request):
    q = request.GET.get('q')
    error_msg = ''
    if not q:
        error_msg = "请输入关键词"
        return render(request, 'index/detail.html', {'error_msg': error_msg})
    post_list = Artical.objects.filter(Q(a_title__icontains=q) | Q(a_content__icontains=q))
    return render(request, 'index/detail.html', {'error_msg': error_msg,
                                               'post_list': post_list})


#首页
def index(request,*args,**kwargs):

        cookie = request.get_signed_cookie('is_login',default=None,salt='ban')
        session = request.session.get("is_login",default=None)
        username = request.user.username
        if cookie and session and cookie==session:
            content = get_sentence()
         #   titles_urls  = get_baidu_new()
            return render(request, 'index/index.html',
                                                    {
                                                    'username':username,
                                                    'content':content[0],
                                                    'note':content[1],
                         #                               "titles_urls":titles_urls
                                                     }
                          )
        return render(request,'index/index.html')


#详情页
def detail(request, pk):
    post = get_object_or_404(Artical, pk=pk)
    md = markdown.Markdown(extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                     # 记得在顶部引入 TocExtension 和 slugify
                                     TocExtension(slugify=slugify),
                                                 ])
    post.a_content = md.convert(post.a_content)
    post.toc = md.toc
    # if "<p>" in post.a_content and "\n" in post.a_content:
    #       print("wwwwwwwpk:",pk)
    #       post.a_content = post.a_content.replace('\n','<br>')
    # if "<ol>" in post.a_content:
    #     post.a_content = post.a_content.replace(r'<ol>','<ul>')
    n = post.a_content.count('<pre class="codehilite">', 0, len(post.a_content))
    for i in range(n):
        post.a_content = re.sub(r'<pre class="codehilite">',
                                '<pre class="codehilite" id="code{}">'
                                '<button  style="float:'
                                'right;z-index:10;background-color:#21262d;display:none;color:#A9B7C6" class="copybtn"'
                                ' data-clipboard-action="copy"'
                                'data-clipboard-target="#code{}">复制'
                                '</button>'.format(i, i), post.a_content, 1)
    m = re.search(r'<div class="toc">\s*<ul>(.*)</ul>\s*</div>', md.toc, re.S)
    post.toc = m.group(1) if m is not None else ''
    print("content2:",post.a_content)
    return render(request,'index/detail.html',context={'post': post})



def add_comment(request):  # 提交评论的处理函数
    if request.user.username:
        comment_content = request.POST.get('comment_content')
        level = int(request.POST.get('level'))
        article_id = request.POST.get('article_id')
        pid = request.POST.get('pid')
        user = request.user  # 获取当前用户的ID
        unique_code = uuid.uuid5(uuid.uuid1(), comment_content)
        #将提交的数据保存到数据库中
        Comment.objects.create(
            comment_content=comment_content,
            level = level,
            pre_comment_id=pid,
            article_id=article_id,
            unique_code= unique_code,
            comment_author = user)
        # reply_comment =  request.POST.get('reply_comment')
        # if "1" in reply_comment:
        obj_data = Comment.objects.get(unique_code=unique_code)
        c_id = obj_data.id
        pid = obj_data.pre_comment_id
        comment_time = datetime.timestamp(obj_data.comment_time)
        comment_list = [{"username":user.username,
                         "level":level,
                         "comment_content":comment_content,
                         "comment_time":comment_time*1000,
                         "pid":pid,
                         "id":c_id}]
        return JsonResponse(comment_list, safe=False)
        # else:
        #     res = get_comment_datas(article_id)
        #     return HttpResponse(json.dumps(res))
        # JsonResponse返回JSON字符串，自动序列化,
        # 如果不是字典类型，则需要添加safe参数为False
    else:
        return redirect('/user_login/')

def delete_comment(request):
     res = {'msg': None}
     if request.method =="POST":
          cid = request.POST.get("comment_id")
          Comment.objects.filter(id=cid).delete()
          msg = "删除成功"
     else:
          msg = "删除失败"
     res["msg"] = msg
     return  HttpResponse(json.dumps(res))

def edit_comment(request):
    res = {'msg': None}
    if request.method == "POST":
        cid = request.POST.get("comment_id")
        comment_content = request.POST.get("comment_content")
        Comment.objects.filter(id=cid).update(comment_content=comment_content)
        msg = "修改成功"
    else:
        msg = "修改失败"
    res["msg"] = msg
    return HttpResponse(json.dumps(res))




def get_comment(request,pk):
    res = {'status': True, 'data': None, 'msg': None}
    try:
        comment_obj = Comment.objects.filter(article_id=pk).order_by("-comment_time")
        com_list = []
        for cm in comment_obj:
            username = cm.comment_author.username
            comment_time = datetime.timestamp(cm.comment_time)
            #comment_time = datetime.strftime(comment_time, '%Y-%m-%d')
            comment_content = cm.comment_content
            level = cm.level
            article_username = cm.article.a_auth_name
            pre_comment_id = cm.pre_comment_id
            com_list.append({"id": cm.id, "username": username,
                             "article_username": article_username,
                             "comment_content": comment_content,
                             "comment_time": comment_time*1000,
                             "pre_comment_id": pre_comment_id,
                             "child": [],
                             "level": level,
                             "before_user": article_username})
        com_list_dict = {}  # 建立一个方便查找的数据结构字典
        for item in com_list:  # 循环评论列表,给每一条评论加一个child:[]就是让他装对他回复的内容
            com_list_dict[item['id']] = item
        result = []
        for item in com_list:
            rid = item['pre_comment_id']
            if rid:  # 如果reply_id不为空的话,那么就是说明他是子评论,我们要把他加入对应的评论后面
                item["before_user"] = com_list_dict[rid]["username"]
                com_list_dict[rid]['child'].append(item)
            else:
                result.append(item)
        res['data'] = result
    except Exception as e:
        res['status'] = False
        res['mag'] = str(e)
    return HttpResponse(json.dumps(res))




#博客
def blog(request,c_name):

    c_obj = Categroy.objects.filter(c_name=c_name) #获取当类别的id
    if  not c_obj:
        return HttpResponse("sorry,do not have result...  please add a new categroy")
    else:
        c_id = c_obj[0].c_id
    if request.method=='POST':
        print('iam post')
    # 当前页
    page_num = request.GET.get('page')
    # 获取路径
    req_path = request.path_info
    datasSet = Artical.objects.filter(category=c_id)
    page_num_count = datasSet.count()
    # 封装的分页组件
    page_obj = MyPage(page_num, page_num_count, req_path, per_page_num, page_num_show)
    page_html = page_obj.page_html()
    # 获取所有的数据
    datas_list = datasSet[page_obj.start_data_num:page_obj.end_data_num][:10:]
    #查询用户名#https://pan.baidu.com/s/1c2DCauW <span class="ff1">密码：</span>5k19</span>
    return render(request,'index/blog.html', { 'datas_list': datas_list,'page_html': page_html,"total":page_num_count})


def center(request):
    return render(request,'index/center.html')

#编辑markdown
def publish(request):

    if request.method == 'GET':
        return render(request, 'index/publish.html')

    elif request.method == 'POST':
        result = {"status": True,'url': None}
        title = request.POST.get('title')
        auth_name = request.POST.get('auth_name')
        content = request.POST.get('content')
        print("content:",content)
        publish_date = request.POST.get('publish_date')
        publish_time = request.POST.get('publish_time')
        publish_date = datetime.strptime(publish_date, '%Y-%m-%d').date()
        publish_time = datetime.strptime(publish_time,'%H:%M:%S').time()
        username = request.user.username
        uid = User.objects.get(username=username)
        c_id = request.POST.get('categroy')
        cid =Categroy.objects.get(c_id=c_id)
        result["url"] = 'http://127.0.0.1/blog'
        Artical.objects.create(a_title=title,a_auth_name=auth_name,
                                    a_content=content,a_publish_date=publish_date,
                                    a_publish_time=publish_time,
                                    category=cid,auth_user=uid)
        response = HttpResponse(json.dumps(result))
        return response





#主题
def categroy(request):
    c_obj_q = Categroy.objects.all()
    return render(request,'index/categroy.html',context={"c_obj_q":c_obj_q})


#帖子
def post(request):
    return render(request,'index/post.html')

#联系
def contact(request):
    return HttpResponse('Hallo')


#代码雨
def coderain(request):
    return render(request,'index/codingrain.html')

#自定义md视图
from mdeditor.fields import MDTextFormField
from django import forms
from django.views.generic import View
# Create your views here.

class BlogForm(forms.Form):
    content = MDTextFormField()

class MyBlogMd(View):
    def get(self,request):
        form = BlogForm()
        return render(request,'index/mymd.html',{'form':form})
















