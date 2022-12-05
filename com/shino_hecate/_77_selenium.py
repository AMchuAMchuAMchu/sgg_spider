# Description ==> TODO
# BelongsProject ==> sgg_spider
# BelongsPackage ==> 
# Version ==> 1.0
# CreateTime ==> 2022-12-05 21:01:01
# Author ==> _02雪乃赤瞳楪祈校条祭_艾米丽可锦木千束木更七草荠_制作委员会_start
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from urllib import request


service = Service('chromedriver.exe')

browser = webdriver.Chrome(service=service)

# url = 'https://www.baidu.com'
url = 'https://www.jd.com'

browser.get(url=url)

print(browser.page_source)


# 阻塞一下的话即可延长浏览器的打开时间的说
time.sleep(10)

browser.quit()

# response01 = request.urlopen('https://www.jd.com')
#
# content = response01.read().decode('utf-8')
#
# print(content)






