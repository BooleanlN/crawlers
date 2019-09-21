import requests
from bs4 import BeautifulSoup

key = {
  'start':0
}
with open('musicTop250.txt','a+',encoding='utf-8') as f:
  for i in range(10):
    r = requests.get('https://music.douban.com/top250',timeout=20,params=key)
    soup = BeautifulSoup(r.text,"lxml")
    """
    搜索文档法：find()\find_all()
    """
    boxs = soup.find_all('div',class_='pl2') 
    for box in boxs:
      """
      选择器方法：select()
      """
      album_name = box.select('a:nth-child(1)')[0].text.strip()
      album_info = box.select('p.pl')[0].text.strip()
      album_rating = box.select('span.rating_nums')[0].text.strip()
      f.write('名称：'+ album_name + ' 信息：' + album_info + ' 评分：'+album_rating+'\n')
    key['start'] = key['start'] + 25
