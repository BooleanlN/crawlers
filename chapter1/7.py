import re
import requests
"""
re.match(pattern, string[, flags=0]) flags用来控制正则表达式是否区分大小写、多行匹配等
match 只能从字符串的起始位置进行匹配

re.search(pattern,string[, flags=0]) 扫描整个字符串，返回第一个成功的匹配

re.findall()返回所有成功的匹配

"""
r = requests.get('http://www.santostang.com/',timeout=20)
book = re.search(r'《网络爬虫：从入门到实践》(.*)勘误',r.text)
# print(book)

titles = re.findall(r'<a href=".*?">(.*)</a>',r.text)
for title in titles:
  print(title)
  print("-----------")
