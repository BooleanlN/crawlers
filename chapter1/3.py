import requests
from bs4 import BeautifulSoup
import json

key = {
  'cityId':1
}
r = requests.post('http://www.dianping.com/bar/search',timeout=20,params=key)
print(r.text)
json_data = json.loads(r.text)
commet_list = json_data['recordList']
for i in range(len(commet_list)):
  print(commet_list[i]['valueMap']['suggestkeyword'])