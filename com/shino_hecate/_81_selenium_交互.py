# Description ==> TODO
# BelongsProject ==> sgg_spider
# BelongsPackage ==> 
# Version ==> 1.0
# CreateTime ==> 2022-12-06 18:32:29
# Author ==> _02雪乃赤瞳楪祈校条祭_艾米丽可锦木千束木更七草荠_制作委员会_start
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service('chromedriver.exe')

browser = webdriver.Chrome(service=service)

browser.get(url='http://www.baidu.com')

input_ = browser.find_element(by=By.XPATH,value='//input[@id="kw"]')

input_.send_keys('周杰伦')

time.sleep(2)

button_ = browser.find_element(by=By.XPATH,value='//input[@id="su"]')

button_.click()

time.sleep(2)

js_bottom = 'document.documentElement.scrollTop=100000'

browser.execute_script(script=js_bottom)

time.sleep(3)

next = browser.find_element(by=By.XPATH,value='//a[@class="n"]')

next.click()

time.sleep(2)

browser.back()

time.sleep(2)

browser.forward()

time.sleep(2)

browser.quit()















































