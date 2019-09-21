import requests
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import time

caps = webdriver.DesiredCapabilities().FIREFOX
caps["marionette"] = True
f = open('geckodriver.log','w')
binary = FirefoxBinary(r'C://Program Files//Mozilla Firefox//firefox.exe',log_file=f)
driver = webdriver.Firefox(firefox_binary=binary, capabilities=caps)
driver.get('https://item.jd.com/100005182160.html')
# f.close() 
# 模拟点击事件
comment = driver.find_element_by_css_selector("li[data-anchor='#comment']")
comment.click()
time.sleep(3)

content = driver.find_element_by_css_selector('p.comment-con')
print(content.text)
# driver = webdriver.Chrome()
# driver.maximize_window()
# url = "http://www.santostang.com/2018/07/04/hello-world/"
# driver.get(url)