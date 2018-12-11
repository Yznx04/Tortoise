# -*- coding: utf-8 -*-
import scrapy


class PtwxSpider(scrapy.Spider):
    name = 'ptwx'
    allowed_domains = ['www.piaotian.com']
    start_urls = ['http://www.piaotian.com/']

    def parse(self, response):
        pass
