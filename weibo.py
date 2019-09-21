import requests
from bs4 import BeautifulSoup

urls = ['https://weibo.com/p/1001063937348351/service?cfs=600&Pl_Core_ArticleList__36_filter=&filter=&time=&type=&Pl_Core_ArticleList__36_page=2#Pl_Core_ArticleList__36',]
for url in urls:
  r = requests.get(url,timeout=20)
  soup = BeautifulSoup(r.text,"lxml")
  artcle_boxes = soup.find_all("div",class_="W_autocut")
  for box in artcle_boxes:
    a = box.a
    print(a.text.strip()+"\t地址："+a['href']+"\n")
