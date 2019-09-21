# coding: UTF-8
import requests
from bs4 import BeautifulSoup
import re
import MySQLdb

# conn = MySQLdb.connect(
#   host='localhost',
#   port= 3306,
#   user='root',
#   passwd='maxen1996',
#   db='safe',
#   charset='utf8'
# )
#cur = conn.cursor()
#cur.execute("create table positive(id int auto_increment,name varchar(1024),url varchar(1024),type varchar(100),primary key(id))")
url_culture = "http://culture.people.com.cn/GB/172318/index"
url_society  = "http://society.people.com.cn/GB/136657/index"
url_military = "http://military.people.com.cn/GB/172467/index"
url_physical = "http://sports.people.com.cn/GB/22176/index"
url_internet = "http://world.people.com.cn/GB/157278/index"
url_prefix = {"culture":"http://culture.people.com.cn",
              "society":"http://society.people.com.cn",
              "internation":"http://world.people.com.cn",
              "physical":"http://sports.people.com.cn",
              "military":"http://military.people.com.cn"
            }
urls = {"culture":url_culture,"society":url_society,"internation":url_internet,"military":url_military,"physical":url_physical}

backfeix = ""
for i in range(1,8):
  for url_name,url in urls.items():
    url = url + backfeix +'.html'
    print(url)
    r = requests.get(url,timeout=20)
    backfeix = str(i)
    soup = BeautifulSoup(r.content.decode("GB2312","ignore"),"lxml")
    box = soup.find('div',class_="ej_list_box clear")
    box2 = soup.find('div',class_='ej_left')
    box = box2 if box is None else box
    if (box is not None):
      aboxes = box.find_all('a')
      with open('articles.txt', 'a+',encoding="utf-8") as f:
        f.write(url_name+":\n")
        for abox in aboxes:
          if abox.get('href') and abox['href'].count('index')==0:
            f.write(abox.text + "\t" + url_prefix[url_name]+abox['href'] + '\n')
#           value = [abox.text.strip(),url_prefix[url_name]+abox['href'],url_name]
#           cur.execute("insert into positive(name,url,type) values(%s,%s,%s)",value)
# conn.commit()
# cur.close()
# conn.close() 