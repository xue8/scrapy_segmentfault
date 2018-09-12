__author__ = 'xue'
import urllib.request
import scrapy
import pymysql
import re
import datetime
import jieba.analyse
import jieba
import requests
from ..items import ScrapyQuestionItem

class segmentfault(scrapy.Spider):
    name = 'segmentfault'
    type = 'javascript' #爬取对象
    url = "https://segmentfault.com/t/" + type + "/questions?type=newest&page="
    offset = 1
    start_urls = [url + str(offset)]
    cnid = 1 #栏目id
    num = 3 #爬取页数
    dict_arr = {'javascript':3, 'php':4, 'python':5, 'java':6, 'mysql':7, 'ios':8, 'android':9, 'node.js':10, 'html5':11, 'linux':12, 'c%2B%2B':13, 'css3':14, 'git':15, 'golang':16, 'ruby':17, 'vim':18, 'docker':19, 'mongodb':20}

    #页面连接
    def parse(self, response):
        for d in self.dict_arr.keys():
            self.cnid = self.dict_arr.get(d)
            yield scrapy.Request("https://segmentfault.com/t/" + d + "/questions?type=newest&page=", callback=self.parse_list,dont_filter=False, meta={'cnid': self.dict_arr.get(d)})

        # dict_arr = {'javascript':3, 'php':4, 'python':5, 'java':6, 'mysql':7, 'ios':8, 'android':9, 'node.js':10, 'html5':11, 'linux':12, 'c%2B%2B':13, 'css3':14, 'git':15, 'golang':16, 'ruby':17, 'vim':18, 'docker':19, 'mongodb':20}
        # for d in dict_arr.keys():
        #     self.cnid = dict_arr.get(d)
        #     self.type = d
        #     print(self.cnid)
        #
        #     for each in response.selector.xpath('//div[contains(@id, "qa")]/section'):
        #         print(d)
        #         #url_list.append(each.xpath('div[contains(@class, "summary")]/h2/a/@href').extract())
        #         aa = each.xpath('div[contains(@class, "summary")]/h2/a/@href').extract_first()
        #         #判断是否采集过
        #         if self.existence(aa):
        #             yield scrapy.Request("https://segmentfault.com" + str(aa), callback=self.parse_detail,dont_filter=False)
        #     if self.offset < self.num:
        #         self.offset += 1
        #         yield scrapy.Request(self.url + str(self.offset), callback=self.parse)


        # for each in response.selector.xpath('//div[contains(@id, "qa")]/section'):
        #     #url_list.append(each.xpath('div[contains(@class, "summary")]/h2/a/@href').extract())
        #     aa = each.xpath('div[contains(@class, "summary")]/h2/a/@href').extract_first()
        #     #判断是否采集过
        #     if self.existence(aa):
        #         yield scrapy.Request("https://segmentfault.com" + str(aa), callback=self.parse_detail,dont_filter=False)
        # if self.offset < 1:
        #     self.offset += 1
        #     yield scrapy.Request(self.url + str(self.offset), callback=self.parse)

    #爬取分页
    def parse_list(self, response):
        self.cnid = response.meta['cnid']
        for each in response.selector.xpath('//div[contains(@id, "qa")]/section'):
            #url_list.append(each.xpath('div[contains(@class, "summary")]/h2/a/@href').extract())
            aa = each.xpath('div[contains(@class, "summary")]/h2/a/@href').extract_first()
            #判断是否采集过
            if self.existence(aa):
                yield scrapy.Request("https://segmentfault.com" + str(aa), callback=self.parse_detail,dont_filter=False,meta={'cnid': response.meta['cnid']})
        if self.offset < self.num:
            self.offset += 1
            yield scrapy.Request(self.url + str(self.offset), callback=self.parse)
    #爬取详情
    def parse_detail(self,response):
        self.cnid = response.meta['cnid']
        i = ScrapyQuestionItem()
        #title
        title = response.selector.xpath('//h1[contains(@id, "questionTitle")]/a/text()').extract()
        i['title'] = title

        #question
        #question = str(response.selector.xpath('normalize-space(//div[contains(@class,"question fmt")]/p/text())').extract()).replace('\000', '').replace('\\n','<br>').replace('\', \'', '').replace('\', \"', '').replace('\", \'', '')
        question = str(response.selector.xpath('//div[contains(@class,"question fmt")]').extract()).replace('\\n', '<br>').replace('[\'', '').replace('\']', '')
        i['question'] = question

        #answer
        answer = str(response.selector.xpath('//div[contains(@id,"goToReplyArea")]/article[contains(@class,"clearfix widget-answers__item")]/div[contains(@class,"post-offset")]/div[contains(@class,"answer fmt")]').extract()).replace('\\n', '<br>').replace('[\'', '').replace('\']', '').replace('\', \'', '<b>回答：</b>')
        i['answer'] = answer
        i['question'] = i['question'] + "<br><b>回答：</b><br>" + answer
        #describes
        dr = re.compile(r'<[^>]+>',re.S)
        a = dr.sub('',i['question']).replace(' ','')
        i['describes'] = a[0:160]

        #keyword
        #i['keyword'] = str(jieba.analyse.extract_tags(a, topK=3, allowPOS=('n', 'nz','nl','ng','a','ad','an','ag','al'))).replace('[','').replace(']','').replace('/','')
        i['keyword'] = str(response.selector.xpath('//ul[contains(@class, "taglist--inline inline-block question__title--tag mr10")]/li/a/@data-original-title').extract()).replace('[','').replace(']','').replace('\'','').replace(' ','')

        #cnid
        i['cnid'] = self.cnid

        #datetime
        i['created_at'] = datetime.datetime.now()
        i['updated_at'] = datetime.datetime.now()

        #images
        image_urls = response.selector.xpath('//div[contains(@class,"question fmt")]//img/@data-src | //div[contains(@id,"goToReplyArea")]/article[contains(@class,"clearfix widget-answers__item")]/div[contains(@class,"post-offset")]/div[contains(@class,"answer fmt")]//img/@data-src').extract()
        i['image_fake_url'] = image_urls
        a = []
        for u in image_urls:
            reaURL = requests.get("https://segmentfault.com" + u, allow_redirects=False)
            a.append(reaURL.headers['Location'])
            #i['image_urls']  = reaURL.headers['Location']
            #print(i['image_urls'])
        i['image_urls'] = a

        yield i
    #判断连接是否存在
    def existence(self,name):
        file = open('E:\\python\\scrapy\\scrapy_question\\scrapy_question\\urls.txt', 'r+')
        lines = file.readlines()
        for line in lines:
            if line.rstrip() == name:
                file.close()
                return False
        file.write(name + '\n')
        file.close()
        return True