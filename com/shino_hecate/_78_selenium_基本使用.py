# Description ==> TODO
# BelongsProject ==> sgg_spider
# BelongsPackage ==> 
# Version ==> 1.0
# CreateTime ==> 2022-12-06 17:53:04
# Author ==> _02雪乃赤瞳楪祈校条祭_艾米丽可锦木千束木更七草荠_制作委员会_start
import time

from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


service = Service('chromedriver.exe')

browser = webdriver.Chrome(service=service)

browser.get(url='http://www.baidu.com')

ele = browser.find_element(by=By.XPATH,value='//input[@id="su"]')

print(ele)

time.sleep(10)

browser.close()



















