# -*- coding: utf-8 -*-
import scrapy

from Noval.items import NovalItem


class PtwxSpider(scrapy.Spider):
    name = 'ptwx'
    allowed_domains = ['www.piaotian.com']
    start_urls = ['https://www.piaotian.com/booksort/0/1.html']

    def parse(self, response):
        """
        基本回掉函数，用于获取到每一页的URL
        :param response:
        :return:返回一个新的页面的URL。并发起新的request请求
        """
        page = response.xpath('//*[@id="pagelink"]/a[@class="last"]/text()').extract()[0]
        page = int(page)
        init_url = 'https://www.piaotian.com/booksort/0/{}.html'
        for num in range(1, page):
            request_url = init_url.format(num)
            yield scrapy.Request(url=request_url, callback=self.get_book_url)

    def get_book_url(self, response):
        """
        获取到每本书的首页地址
        :param response:
        :return: 发起新的请求，通过另一个函数处理详情并得到想要的结果
        """
        book_url_list = response.xpath(
            '//*[@id="content"]/table[2]/tr/td[1]/a/@href').extract()
        for book_url in book_url_list:
            yield scrapy.Request(url=book_url, callback=self.get_book_index)

    def get_book_index(self, response):
        novel = NovalItem()
        novel['book_name'] = response.xpath(
            '//*[@id="content"]/table/tr[1]/td/table/'
            'tr[1]/td/table/tr/td/span/h1/text()')
        novel['category'] = response.xpath(
            '//*[@id="content"]/table/tr[1]'
            '/td/table/tr[2]/td[1]/text()')[0].split('：')[-1]
        novel['author'] = response.xpath(
            '//*[@id="content"]/table/tr[1]'
            '/td/table/tr[2]/td[2]/text()')[0].split('：')[-1]
        novel['word_number'] = response.xpath(
            '//*[@id="content"]/table/tr[1]'
            '/td/table/tr[2]/td[4]/text()')[0].split('：')[-1]
        novel['toupdate'] = response.xpath(
            '//*[@id="content"]/table/tr[1]'
            '/td/table/tr[3]/td[1]/text()')[0].split('：')[-1]
        novel['status'] = response.xpath(
            '//*[@id="content"]/table/tr[1]'
            '/td/table/tr[3]/td[2]/text()')[0].split('：')[-1]
        novel['href'] = response.xpath(
            '//*[@id="content"]/table/tr[8]/td/table/caption/a/@href')
        content = ''.join(
            response.xpath(
                '//*[@id="content"]/table/tr[4]/td/table/tr/td[2]/div/text()'
            )).strip()
        novel['content'] = content
        yield novel