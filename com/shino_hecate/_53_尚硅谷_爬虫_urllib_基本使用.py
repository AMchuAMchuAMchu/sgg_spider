# Description ==> TODO
# BelongsProject ==> sgg_spider
# BelongsPackage ==> 
# Version ==> 1.0
# CreateTime ==> 2022-11-03 20:26:49
# Author ==> _02雪乃赤瞳楪祈校条祭_艾米丽可锦木千束木更七草荠_制作委员会_start

import urllib.request as request

response01 = request.urlopen(url="http://www.baidu.com")

content01 = response01.read().decode('utf-8')

print(content01)
