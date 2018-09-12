# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyQuestionItem(scrapy.Item):
    # define the fields for your item here like:
    #name = scrapy.Field()

    title = scrapy.Field()
    question = scrapy.Field()
    answer = scrapy.Field()
    cnid = scrapy.Field()
    describes = scrapy.Field()
    keyword = scrapy.Field()
    created_at = scrapy.Field()
    updated_at = scrapy.Field()

    #images
    image_urls = scrapy.Field()
    image_fake_url = scrapy.Field()
    image_path = scrapy.Field()
    pass