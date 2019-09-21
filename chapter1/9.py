from pymongo import MongoClient
import requests
from bs4 import BeautifulSoup
import datetime

client = MongoClient('localhost',27017)
db = client.fortess
collection = db.blog

r = requests.get('http://www.santostang.com/',timeout=20)
soup = BeautifulSoup(r.text,'lxml')
boxes = soup.find_all('h1',class_='post-title')
for box in boxes:
  url = box.a['href']
  title = box.a.text.strip()
  post = {
    'url': url,
    'title': title,
    'posttime':datetime.datetime.now()
  }
  collection.insert_one(post)
client.close()