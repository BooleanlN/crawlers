from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import time

caps = webdriver.DesiredCapabilities().FIREFOX
caps["marionette"] = True
f = open('geckodriver.log','w')
binary = FirefoxBinary(r'C://Program Files//Mozilla Firefox//firefox.exe',log_file=f)
fp = webdriver.FirefoxProfile()
fp.set_preference("permissions.default.stylesheet",2)
fp.set_preference("permissions.default.image",2)
# fp.set_preference("javascript.enabled",False)
driver = webdriver.Firefox(firefox_binary=binary, capabilities=caps)
driver.get('https://www.airbnb.cn/s/Shenzhen--China/homes')
next_btn = driver.find_element_by_css_selector('div._1m76pmy')
with open('houses.txt','a+',encoding="utf-8") as f:
  for i in range(1,20):
   time.sleep(3)
   box = driver.find_elements_by_css_selector('div._qlq27g')
   for i in range(len(box)):
    name = box[i].find_element_by_css_selector('div._qhtkbey').text
    house_type = box[i].find_element_by_css_selector('span._fk7kh10').text
    price = box[i].find_element_by_css_selector('div._1ixtnfc span:nth-child(2)').text
    comment = box[i].find_element_by_css_selector('span._6rrm590').text
    f.write("名称："+name + "  类型："+house_type+" 价格："+price+" 评价："+comment+"\n")
   f.write("----------------------------------\n")
   next_btn.click()
