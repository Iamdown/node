from django.test import TestCase

# Create your tests here.

import json
import time
import requests
from lxml import etree

def get_baidu_new():
    headers = {
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
    res = requests.get(url=url,headers=headers)
    element = etree.HTML(res.text)
    #lis = element.xpath("//li[contains(@class,'hotsearch-item')]")
    # for item in lis:
    #    url =  item.xpath('./a/@href')
    #    title = item.xpath('.//span[@class="title-content-title"]/text()')
    #
    #    print(title,url)
    other_title =  json.loads(element.xpath("//textarea[@id='hotsearch_data']/text()")[0])["hotsearch"]
    url_list = []
    for item  in other_title:
        title = item["pure_title"]
        url = f"https://www.baidu.com/s?wd={title}"
        res = requests.get(url=url,headers=headers)
        res.encoding = "gb2312"
        element = etree.HTML(res.text)
        try:
            url = element.xpath("//div[@id='content_left']/div//p[@class='title_2e25d']/a/@href")[0]
        except Exception as e:
            print(e)
        print(title,url)
        data_dict = {title:url}
        url_list.append(data_dict)
    return url_list
if __name__ == '__main__':
    get_baidu_new()