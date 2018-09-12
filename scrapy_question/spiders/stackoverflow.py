__author__ = 'xue'
import urllib.request
import scrapy
#from scrapy_question.translate.translate import translate1,translate
from googletrans import Translator
from lxml import etree

class stackoverflow(scrapy.Spider):
    name = 'stackoverflow'
    start_urls = ['https://stackoverflow.com/questions/8039907/']

    def parse(self, response):
        translator = Translator()
        #title
        title = response.selector.xpath('//h1/a/text()').extract()
        title = ''.join(title)
        title = translator.translate(title, dest='zh-CN').text
        #question
        question = str(response.selector.xpath('//div[contains(@class,"postcell post-layout--right")]/div/node()').extract()).replace('<blockquote>', '').replace('</blockquote>', '').replace('</code>', '').replace('<code>', '').replace('</p>', '').replace('<p>', '').replace('\'', '').replace('\\n', '').replace('[', '').replace(']', '.')
        #question = response.selector.xpath('//div[contains(@class,"postcell post-layout--right")/text()]').extract()
        #print(question)
        #question = ''.join(question)
        #question = translator.translate(question, dest='zh-CN').text
        #print(question)
        #answer
        # alist = response.selector.xpath('//div[contains(@id, "answers")]')
        # print (alist)
        # i = 0
        # for answer in alist:
        #     item[i]['answer'] = answer.xpath('div[contains(@class, "answer")]/div[contains(@class, "answercell post-layout--right")]/div[contains(@class, "post-text")]/p/text()').extract_first()
        #     print (item[i]['answer'])
        #     i = i+1


        #print(translate1(b))
        #print(translate1('S'))
        #js = Py4Js()
        #tk = js.getTk('good')
        #print(translate1('good'))
        #print(Translate.translate1('good','good'))
