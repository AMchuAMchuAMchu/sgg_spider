# Description ==> TODO
# BelongsProject ==> sgg_spider
# BelongsPackage ==> 
# Version ==> 1.0
# CreateTime ==> 2022-12-06 19:48:41
# Author ==> _02雪乃赤瞳楪祈校条祭_艾米丽可锦木千束木更七草荠_制作委员会_start

import requests

response = requests.get(url='http://www.baidu.com')

print(type(response))

response.encoding = 'utf-8'

print(response.text)

print(response.content)

print(response.url)

print(response.status_code)

print(response.headers)













