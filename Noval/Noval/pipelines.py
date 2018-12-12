# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class NovalPipeline(object):
    def process_item(self, item, spider):
        name = item['book_name'][0]
        author = item['author']
        category = item['category']
        word_number = item['word_number']
        toupdate = item['toupdate']
        status = item['status']
        href = item['href']
        content = item['content']
        db = pymysql.connect(host='120.78.78.202', port=3306, user='root',
                             passwd='420420', db='ptwx', charset='utf8')
        cur = db.cursor()
        sql = "INSERT INTO allbook(bookname, author, category, word_number, toupdate, status, href, content) values " \
              "(%s, %s, %s, %s, %s, %s, %s, %s)"
        cur.execute(sql, (name,author, category, word_number, toupdate, status,
                          href, content))
        db.commit()