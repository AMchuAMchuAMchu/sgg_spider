# Description ==> TODO
# BelongsProject ==> sgg_spider
# BelongsPackage ==> 
# Version ==> 1.0
# CreateTime ==> 2022-10-31 08:45:01
# Author ==> _02雪乃赤瞳楪祈校条祭_艾米丽可锦木千束木更七草荠_制作委员会_start

# def sum(num01, num02):
#     return num01 + num02
#
# print(sum(100, 99))

import  numpy as np
file = open(file='d:/twitter_comment.txt',encoding='utf-8',mode='w')
for i in range(1,101,1):
    res = '第',i-4,'条','==>'
    file.writelines(res)


