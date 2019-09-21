import requests
from lxml import etree
"""
XPath: 一门在XML文档中查找信息的语言，使用路径表达式来选取XML文档中的节点或者节点集，也可以用在HTML获取数据当中
"""
link = 'http://www.santostang.com/'
headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
r = requests.get(link, headers=headers)
html = etree.HTML(r.text)
title_list = html.xpath('//*[@id="main"]/div/div[1]/article[1]/header/h1/a/text()')
print(title_list)