import requests

# r = requests.get('http://www.santostang.com')
# print (r.encoding) #响应内容编码
# print (r.status_code) #响应状态字
# print (r.text) # 响应内容
# print (r.content) #响应体，字节形式
# print (r.json)

# # 带参数的get
# key_dict = {'key1':'value1', 'key2':'value2'}
# r = requests.get('http://httpbin.org/get', params=key_dict)
# print ("URL已经正确编码", r.url)
# print ("响应体",r.text)

# # 带参数的post
# r = requests.post('http://httpbin.org/post',data=key_dict)
# print (r.text)

# # 设置timeout
# r = requests.get('http://www.santostang.com', timeout=0.001)

## 爬取top250电影数据
params = {'start':0,'filter':''}

from bs4 import BeautifulSoup

for i in range(10):
  params['start'] = i*25;
  r = requests.get('https://movie.douban.com/top250',timeout=20,params=params)
  print(r.url)
  soup = BeautifulSoup(r.text,'lxml')
  movies = soup.find_all("span",class_="title")
  stars = soup.find_all("span",class_ ="rating_num")
  authors = soup.find_all("div",class_="bd")
  del authors[0]
  print(len(stars))
  with open('movies.txt','a+',encoding="utf-8") as f:
    for i in range(len(stars)):
      if (i*2+1 < len(movies)):
        f.write(movies[2*i].text.strip()+" "+movies[2*i+1].text.strip()+"\t")
      f.write(stars[i].text.strip()+"\t")
      f.write(authors[i].p.text.strip() +"\n")
      # print(authors[i].p.text.strip())
  