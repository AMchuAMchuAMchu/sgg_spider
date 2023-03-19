# Description ==> TODO
# BelongsProject ==> sgg_spider
# BelongsPackage ==> 
# Version ==> 1.0
# CreateTime ==> 2022-12-06 18:32:29
# Author ==> _02雪乃赤瞳楪祈校条祭_艾米丽可锦木千束木更七草荠_制作委员会_start
import time

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from lxml import etree

desired_capabilities = DesiredCapabilities.CHROME  # 修改页面加载策略
desired_capabilities["pageLoadStrategy"] = "eager"

service = Service('chromedriver.exe')

from selenium import webdriver

url = 'https://item.jd.com/7952881.html#none'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}

cookie = {
    'domain':'',
    'shshshfpa':'dffc5c23-e844-2a77-59df-ee409bc12f06-1667707036',
    'shshshfpb':'p-oHNXqdy-N_CzwK1qi-r0w',
    '__jdu': '16677070362122071639903',
    '__jdv': '122270672|direct|-|none|-|1671149738933',
    'areaId': '19',
    'PCSYCityID': 'CN_440000_440100_0',
    'pinId': 'fXANBW9PC63li3IOUSCsXbV9-x-f3wj7',
    'pin': 'jd_7d861c9a06dce',
    'unick': 'Berkeley_%E5%B0%A4%E6%B4%8B%E6%98%AF%E5%81%B6%E5%83%8F',
    '_tp': 'yoq4pysAVJtWIJ3kK6koowv52vwvdpiu%2FnpDybR7RjA%3D',
    '_pst': 'jd_7d861c9a06dce',
    ' user-key': 'cd9989af-14c8-4db9-939e-0315a2455191',
    'ipLoc-djd': '19-1601-50258-62839',
    'jsavif': '1',
    'shshshfp': '0dcbc347fd2711eabe970b3357d9b850',
    'ip_cityCode': '1601',
    '__jda': '122270672.16677070362122071639903.1667707036.1671238256.1671242276.9',
    'TrackID': '1BhSExysLRG-Dg7--1Ut82Skps_KrkAR2VPcA5GB425Q3mOHqlyKSjBAXIroCSqX5jiU5kVZCElbDVu-U4MxNtE1FHkRgOwsaiLkFOlhWs4w',
    'token': '1a956d0235b3b701ed1d2c22eadd8024,2,928468',
    '__tk': 'AcezAuj1kUGEAVft4VswBVawjVGFBUs0juWDjVhtAUe,2,928468',
    'shshshsID': '911765a1e9a49caf0548544c71ca6370_5_1671243716415',
    '__jdb': '122270672.7.16677070362122071639903|9.1671242276',
    '__jdc': '122270672',
    '3AB9D23F7A4B3C9B': 'EC5VOLZG2QB3Q7R67KLVTVJUP6HWUUWUKOSEOHJP57SAYQQK5CDKFSAB6DXF2CCTF4O4NPK7OZX3ZOG7SKS27Z4IDQ',
    'wlfstk_smdl': 'ii8zai520bzwv47obkoewazlwy830xfi',
}

browser = webdriver.Chrome(service=service)


for k,v in cookie.items():
    browser.add_cookie({'name':k,'value':v})

browser.refresh()

browser.get(url=url)


time.sleep(100)
# browser.add_cookie(cookie_dict=cookie)

page = browser.find_element(by=By.XPATH, value='//div[@class="tab-main large"]//s/text()')

# time.sleep(1)

print(page.text)

time.sleep(100)
