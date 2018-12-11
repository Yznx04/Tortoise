# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NovalItem(scrapy.Item):
    # define the fields for your item here like:
    book_name = scrapy.Field()
    category = scrapy.Field()
    author = scrapy.Field()
    word_number = scrapy.Field()
    toupdate = scrapy.Field()
    status = scrapy.Field()
    href = scrapy.Field()
    content = scrapy.Field()

