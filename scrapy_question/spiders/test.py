__author__ = 'xue'
import urllib.request
import scrapy
#from scrapy_question.translate.translate import translate1,translate

from selenium import webdriver
import requests
import re

class test(scrapy.Spider):
    name = 'test'
    start_urls = ['https://segmentfault.com/q/1010000015992166']

    def parse(self, response):

        header = {
            'cookie': '_ga=GA1.2.625705121.1516883301; Hm_lvt_e23800c454aa573c0ccb16b52665ac26=1534599344,1534655995,1534668853,1534669434; Hm_lpvt_e23800c454aa573c0ccb16b52665ac26=1534675087; afpCT=1',
            'pragma': 'no-cache',
            'referer': 'https://segmentfault.com/q/1010000016045152',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'       ,
       }
        #i = ScrapyQuestionItem()
        # # image_urls = str(response.selector.xpath('//div[contains(@class,"question fmt")]//img/@data-src | //div[contains(@id,"goToReplyArea")]/article[contains(@class,"clearfix widget-answers__item")]/div[contains(@class,"post-offset")]/div[contains(@class,"answer fmt")]//img/@data-src').extract())
        # # i['image_urls'] = "https://segmentfault.com" + image_urls
        # image_urls = response.selector.xpath('//div[contains(@class,"question fmt")]//img/@data-src | //div[contains(@id,"goToReplyArea")]/article[contains(@class,"clearfix widget-answers__item")]/div[contains(@class,"post-offset")]/div[contains(@class,"answer fmt")]//img/@data-src').extract()
        # # for a in image_urls:
        # #     reaURL = requests.get("https://segmentfault.com" + a, allow_redirects=False)
        # #     i['image_urls']  = reaURL.headers['Location']
        # #     yield i
        # i['image_fake_url'] = image_urls
        # a = []
        # for u in image_urls:
        #     reaURL = requests.get("https://segmentfault.com" + u, allow_redirects=False)
        #     a.append(reaURL.headers['Location'])
        #
        # i['image_urls'] = a
        # yield i
        # question = str(response.selector.xpath('//div[contains(@class,"question fmt")]').extract()).replace('\\n', '<br>').replace('[\'', '').replace('\']', '')
        # i['question'] = question
        #
        # #images
        # image_urls = response.selector.xpath('//div[contains(@class,"question fmt")]//img/@data-src | //div[contains(@id,"goToReplyArea")]/article[contains(@class,"clearfix widget-answers__item")]/div[contains(@class,"post-offset")]/div[contains(@class,"answer fmt")]//img/@data-src').extract()
        # i['image_fake_url'] = image_urls
        # a = []
        # for u in image_urls:
        #     reaURL = requests.get("https://segmentfault.com" + u, allow_redirects=False)
        #     a.append(reaURL.headers['Location'])
        #     #i['image_urls']  = reaURL.headers['Location']
        #     #print(i['image_urls'])
        # i['image_urls'] = a
        #
        # j = 0
        # for a in i['image_fake_url']:
        #     a = a.replace('?', '\?')
        #     a = a.replace('&', '&amp;')
        #     reg = '(<img\sdata-src="' + a + '"\ssrc=")[^"]+"'
        #     #reg = '第二参数，'
        #     #path =  str(i['image_path'][j].get('path'))
        #     path = '<img src="' + str(j) + '"'
        #     i['question'] = re.sub(r'%s'%reg, path, str(i['question']))
        #     j = j + 1
        #     #print(a)
        # print(i)
        #print(self.existence("/q/1010000016080941111111"))
        dict_arr = {'javascript':3, 'php':4, 'python':5, 'java':6, 'mysql':7, 'ios':8, 'android':9, 'node.js':10, 'html5':11, 'linux':12, 'c%2B%2B':13, 'css3':14, 'git':15, 'golang':16, 'ruby':17, 'vim':18, 'docker':19, 'mongodb':20}
        for d in dict_arr.keys():
            print(d)
            print(dict_arr.get(d))
            yield(self.existence(d))

    def existence(self,name):
        file = open('E:\\python\\scrapy\\scrapy_question\\scrapy_question\\urls.txt', 'r+')
        lines = file.readlines()
        for line in lines:
            if line.rstrip() == name:
                return False
        file.write(name + '\n')
        return True