# Description ==> TODO
# BelongsProject ==> sgg_spider
# BelongsPackage ==> 
# Version ==> 1.0
# CreateTime ==> 2022-11-03 20:36:50
# Author ==> _02雪乃赤瞳楪祈校条祭_艾米丽可锦木千束木更七草荠_制作委员会_start

import urllib.request as request

response01 = request.urlopen(url='http://www.baidu.com')

# print(response01)

# res01 = response01.read()
# res01 = response01.readline()
# res01 = response01.readlines()
# res01 = response01.getcode()
# res01 = response01.geturl()
res01 = response01.getheaders()

print(res01)
