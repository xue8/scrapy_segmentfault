__author__ = 'xue'
import urllib.request
import requests
from scrapy_question.translate.py4js import Py4Js

def open_url(url):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    req = urllib.request.Request(url = url,headers=headers)
    response = urllib.request.urlopen(req)
    data = response.read().decode('utf-8')
    return data

def translate(content,tk):
    if len(content) > 4891:
        print("翻译的长度超过限制！！！")
        return


    param = {'tk': tk, 'q': content}

    result = requests.get("""http://translate.google.cn/translate_a/single?client=t&sl=en
        &tl=zh-CN&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss
        &dt=t&ie=UTF-8&oe=UTF-8&clearbtn=1&otf=1&pc=1&srcrom=0&ssel=0&tsel=0&kc=2""", params=param)

    #返回的结果为Json，解析为一个嵌套列表
    res = ''
    # for text in result.json():
    #     return text
    return result.text
    #return (result.json())

def translate1(content):
    js = Py4Js()
    tk = js.getTk(content)
    return translate(content,tk)