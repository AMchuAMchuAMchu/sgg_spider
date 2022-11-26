# Description ==> TODO
# BelongsProject ==> sgg_spider
# BelongsPackage ==> 
# Version ==> 1.0
# CreateTime ==> 2022-11-26 20:11:13
# Author ==> _02雪乃赤瞳楪祈校条祭_艾米丽可锦木千束木更七草荠_制作委员会_start

proxies = [
    {'http:':'116.205.238.209:3389'},
    {'http:':'116.205.238.209:3390'},
    {'http:':'116.205.238.209:3391'},
]

import random


for i in range(1,10):
    res01 = random.choice(proxies)
    print(res01)


