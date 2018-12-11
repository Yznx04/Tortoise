import re

import requests
import bs4
from lxml import etree
url = 'https://www.piaotian.com/bookinfo/9/9910.html'
header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}
response = requests.get(url=url, headers=header)
txt = response.content.decode('gbk')
html = etree.HTML(txt)
name = html.xpath('//*[@id="content"]/table/tr[4]/td/table/tr/td[2]/div/text()')
name = ''.join(name)
name = name.strip()
name = re.sub(r'\r', '', name)


