# import re
#
# import requests
# import bs4
# from lxml import etree
# url = 'https://www.piaotian.com/bookinfo/9/9910.html'
# header = {
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
# }
# response = requests.get(url=url, headers=header)
# txt = response.content.decode('gbk')
# html = etree.HTML(txt)
# name = html.xpath('//*[@id="content"]/table/tr[4]/td/table/tr/td[2]/div/text()')
# name = ''.join(name)
# name = name.strip()
# name = re.sub(r'\r', '', name)


import pymysql
book = {'author': '阴险的悟净',
         'book_name': ['大怪医'],
         'category': '都市言情',
         'content': '以医入道未济世，功德十万方问仙！',
        'href': "https://www.piaotian.com/html/6/6966/index.html",
        'status': '连载中',
        'toupdate': '2016-11-17',
        'word_number': '1794394字'
        }
db = pymysql.connect(host='120.78.78.202', port=3306, user='root', passwd='420420', db='ptwx', charset='utf8')
print(type(book['href']))
print(book['content'])
c = db.cursor()

s3 = "INSERT INTO allbook(bookname, author, category, word_number, toupdate, status, href, content) values " \
     "(%s, %s, %s, %s, %s, %s, %s, %s)"
c.execute(s3, (book['book_name'][0], book['author'] , book['category'], book['word_number'], book['toupdate'], book['status'], book['href'], book['content'], ))
db.commit()