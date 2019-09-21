import csv
import requests
from bs4 import BeautifulSoup

with open('books.csv','a+',encoding="utf-8",newline='') as f:
  w = csv.writer(f)
  r = requests.get('https://book.douban.com/top250?icn=index-book250-all',timeout=20)
  soup = BeautifulSoup(r.text,'lxml')
  items = soup.find_all('div', class_='pl2')
  item_boxes = soup.find_all('tr',class_='item')
  titles = []
  infos = []
  for item in item_boxes:
    title = item.find('div',class_='pl2').a.text.strip()
    info = item.p.text.strip()
    w.writerow([title,info])