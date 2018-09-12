# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from scrapy.pipelines.images import ImagesPipeline
from scrapy.http import Request
from scrapy.exceptions import DropItem
import scrapy
import re

def dbHandle():
    conn = pymysql.connect(
        host = "103.97.176.97",
        user = "biecheng_cn",
        passwd = "47iwSXjJhB7h2Zif",
        charset = "utf8",
        db = 'biecheng_cn',
        use_unicode = False
    )
    return conn

class ScrapyQuestionPipeline(object):
    def process_item(self, item, spider):
        dbObject = dbHandle()
        cursor = dbObject.cursor()

        #图片保存路径
        #print(item['image_path'][0].get('path'))
        j = 0
        for i in item['image_fake_url']:
            i = i.replace('?', '\?')
            i = i.replace('&', '&amp;')
            reg = '(<img\sdata-src="' + i + '"\ssrc=")[^"]+"'
            path = '<img src="/static/images/question/' + str(item['image_path'][j].get('path')) + '"'
            item['question'] = re.sub(r'%s'%reg, path, item['question'])
            j = j + 1
            #item['question'] = item['question'].replace('(?<=src=").*?(?=")',item['image_path'][j].get('path'))
        #item['question'] = item['question'].replace(str(item['image_fake_url']),"/static/images/question/" + str(item['image_path'][0].get('path')))
        #item['question'].xpath('//img[contains(@data-src,str(item["image_fake_url"]))]/').extract_first().replace('https://static.segmentfault.com/v-5b7544bd/global/img/squares.svg', "/static/images/question/" + str(item['image_path'][0].get('path')))

        sql = 'insert into que_content(content) values (%s)'
        try:
            #插入问答内容
            cursor.execute(sql,(item['question']))
            cursor.connection.commit()
            #查询问答内容id
            cursor.execute('select id from que_content ORDER BY id desc limit 1')
            cid = cursor.fetchall()
            #插入问答其他信息
            sql1 = 'insert into que_question(cnid, cid, title,describes,keyword,created_at,updated_at) values (%s,%s,%s,%s,%s,%s,%s)'
            cursor.execute(sql1,(item['cnid'],cid,item['title'],item['describes'],item['keyword'],item['created_at'],item['updated_at']))
            cursor.connection.commit()
        except BaseException as e:
            print("错误原因："+e)
            dbObject.rollback()
        return item

class PicsDownloadPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            yield scrapy.Request(image_url)

    def item_completed(self, results, item, info):
        # 将下载的图片路径（传入到results中）存储到 image_paths 项目组中，如果其中没有图片，我们将丢弃项目:
        image_path = [x['path'] for ok, x in results if ok]
        if not image_path:
            raise DropItem("Item contains no images")
        item['image_path'] = image_path
        return item



