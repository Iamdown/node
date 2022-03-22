import requests, parsel, os, time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}

url = 'https://www.jdlingyu.com/tuji/hentai/gctt'
response = requests.get(url=url, headers=headers)
html_str = response.text
# print(html_str)
# 数据提取。用xpath（parsel）
selector = parsel.Selector(html_str)  # 转换数据类型
lis = selector.xpath('//*[@id="post-list"]/ul/li')
dirname = "image"
if not os.path.exists(dirname):
    os.mkdir(dirname)
for li in lis:
    pic_title=li.xpath('.//h2/a/text()').get() #相册的标题,用于保存相册的文件夹标题
    pic_url=li.xpath('.//h2/a/@href').get() #相册的访问地址
    # print(pic_title,pic_url)
  #  print(pic_title,'ing')
#     可以根据大文件的地址，创建各类的文件夹，即文件夹里面再放详细的图片
    mydir = dirname+"/"+pic_title.replace(' ','')
    os.mkdir(mydir)
#     发送详情页地址请求
    response_pic = requests.get(url=pic_url,headers=headers).text #详情页数据
    selector_2=parsel.Selector(response_pic)
    # pic_url_list = selector_2.xpath('//div[@class="entry-content"]//img/@src').getall()  #所有图片的链接
    pic_url_list = selector_2.xpath('//*[@id="primary-home"]/article/div[2]/p/img/@src').getall()  #所有图片的链接
    # print(pic_url_list)
    for pic_url in pic_url_list:
        # print(pic_url)
        # 二进制数据用content提取
        img_data=requests.get(url=pic_url,headers=headers).content
        # 数据保存
        file_name=pic_url.split('/')[-1]
        path = mydir+'/'+file_name.replace(' ','')
        with open(path,mode='wb') as f:
            f.write(img_data)
            print(file_name,'ok')





