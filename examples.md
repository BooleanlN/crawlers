### 爬虫案例

1. B站热门动态

   打开动态页面：https://t.bilibili.com/

   按‘F12’键打开控制台，并选择Network标签页，并点击XHR（即通过AJAX等异步拿到的数据，XHR为XMLHttpRequest）

   点击查看各请求连接，可在右侧查看请求详情，preview页面为响应数据的格式化预览，headers是请求头和响应头，response是原始的响应数据，initlator是反映请求的调用栈，cookies是该请求携带的cookie信息。

   ![image-20201011183628373](http://ww1.sinaimg.cn/large/a251ceedly1gjllszm244j22lc138ql7.jpg)

   从上图，可以找到https://api.vc.bilibili.com/dynamic_svr/v1/dynamic_svr/unlogin_dynamics?fake_uid=006033&hot_offset=0
   该链接是动态信息的请求，里面包括了其动态内容、动态点赞数、转发数以及UP主的相关信息。结构如下，（这里用到的是一个Chrome插件，JSONView，可以很清晰地看到整个JSON结构）

   ![image-20201011185855152](http://ww1.sinaimg.cn/large/a251ceedly1gjlm2lpdehj22la1bon5o.jpg)

   可以通过requests库以及json库，实现对该API的爬取。

   ```python
   import requests
   import json
   
   content = requests.get(
       "https://api.vc.bilibili.com/dynamic_svr/v1/dynamic_svr/unlogin_dynamics")
   content.encoding = 'utf-8'
   dynamic_info = json.loads(content.text,encoding='utf-8')
   print(dynamic_info['data']['cards'])
   ```

2. 关注UP主动态爬取

   同样的步骤，这次是登录之后，打开动态页，打开控制台，找到相应的Ajax请求。

   https://api.vc.bilibili.com/dynamic_svr/v1/dynamic_svr/dynamic_new?uid=269078589&type_list=268435455&from=weball&platform=web

   ![image-20201011190405674](http://ww1.sinaimg.cn/large/a251ceedly1gjlm1mqxwxj22lc0v613k.jpg)

   与第一个案例不同，此处需要一个登录态，而B站的登录态是通过cookie来维护的，因此在Headers标签页，找到Request Headers，可以看到Cookie字段。

   ![image-20201011190601527](http://ww1.sinaimg.cn/large/a251ceedly1gjlm1vsirqj21ua0gyn2x.jpg)

   在脚本中，同样地构建一个请求header，用于伪装。

   ```python
   import requests
   import json
   
   headers = {
       'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit',
       'Cookie': 'l=v; _uuid=DE11DD47-6F63-47DC-26E7-3389128D822725552infoc; buvid3=A428FD7D-2912-4AA0-B1AD-DD7783171BA253922infoc; sid=9qpjqv7j; DedeUserID=269078589; DedeUserID__ckMd5=2d0fd23381765653; SESSDATA=c02d858d%2C1617611370%2C028a6*a1; bili_jct=cbf75b7d1e099ce523272f4551df67ee; CURRENT_FNVAL=80; blackside_state=1; rpdid=|(JY~|J)J|Rl0J\'uY|k|lmR|k; CURRENT_QUALITY=112; LIVE_BUVID=AUTO5616021668274232; _dfcaptcha=8d62a690e6a23c6a5f09572bbe25cc38; PVID=8; bp_video_offset_269078589=444841213232482532; bp_t_offset_269078589=444841548244127539'
   }
   content = requests.get(
       "https://api.vc.bilibili.com/dynamic_svr/v1/dynamic_svr/dynamic_new?uid=269078589&type_list=268435455&from=weball&platform=web",headers=headers)
   content.encoding = 'utf-8'
   dynamic_info = json.loads(content.text,encoding='utf-8')
   print(dynamic_info['data']['cards'])
   ```

   此时，拿到的数据便是登录用户关注UP主的动态。
   
3. Seleium使用

   - 安装seleium`pip install selenium`

   - 下载浏览器驱动[下载地址](http://www.testclass.net/selenium_python/selenium3-browser-driver/)，版本要对应好。

   - 驱动环境变量配置，将驱动的文件夹路径，添加至Path环境变量

     操作步骤：我的电脑-->属性-->系统设置-->高级-->环境变量-->系统变量-->Path

   案例：

   使用Seleium模拟登录B站，同时请求该用户的动态数据。

   介绍一个seleium的[教程网站](http://www.testclass.net/selenium_python/install-selenium)

   本次案例用到的有：

   元素定位：ID定位`find_element_by_id`、CSS选择器定位`find_element_by_css_selector`

   键盘事件：send_keys

   鼠标事件：click

   元素等待：显式等待

   Cookie操作：`get_cookies()`

   ```python
   from selenium import webdriver
   import requests
   import json

   from selenium.webdriver.support import expected_conditions as EC
   from selenium.webdriver.support.wait import WebDriverWait
   from selenium.webdriver.common.by import By

   driver = webdriver.Chrome()
   driver.get('https://passport.bilibili.com/login')
   input_box = driver.find_element_by_id('login-username') # 使用标签的ID属性来定位
   password_box = driver.find_element_by_id('login-passwd') # 使用标签的ID属性来定位
   input_box.send_keys("xxx") # 账号输入
   password_box.send_keys("xxxx") # 密码

   submit_btn = driver.find_element_by_css_selector(".btn.btn-login") # 找到登录按钮，
   submit_btn.click() # 点击事件
   element = WebDriverWait(driver,20,0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR,".t"))) # 等待20s，直到页面中可以定位到类名为t的元素，每隔0.5s检查一次
   cookies = driver.get_cookies() # 拿到登录后的cookie
   print(cookies) # 该cookie是以键值对输出的，因此需要进行拼接
   cookie_strs = ["{}={}".format(cookie['name'],cookie['value']) for cookie in cookies]
   cookie = ";".join(cookie_strs) #使用分号拼接即可
   print(cookie)

   #下面的和之前的案例一样的流程
   headers = {
       'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit',
       'Cookie': cookie
   }
   content = requests.get(
       "https://api.vc.bilibili.com/dynamic_svr/v1/dynamic_svr/dynamic_new?uid=269078589&type_list=268435455&from=weball&platform=web",headers=headers)
   content.encoding = 'utf-8'
   dynamic_info = json.loads(content.text,encoding='utf-8')
   print(dynamic_info['data']['cards'])
   ```

   可以尝试自己用隐式等待做下。
   
