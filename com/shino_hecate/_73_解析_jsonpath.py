# Description ==> TODO
# BelongsProject ==> sgg_spider
# BelongsPackage ==> 
# Version ==> 1.0
# CreateTime ==> 2022-11-29 20:54:24
# Author ==> _02雪乃赤瞳楪祈校条祭_艾米丽可锦木千束木更七草荠_制作委员会_start


import json

import jsonpath

obj = json.load(open(file=r'D:\seldom\rd\Python_ProjectAll\sgg_spider\com\shino_hecate\assets\_06_store.json',mode='r',encoding='utf-8'))

# print(obj)

# json_value = jsonpath.jsonpath(obj=obj,expr='$.store.book[*].author')
# json_value = jsonpath.jsonpath(obj=obj,expr='$..author')
# json_value = jsonpath.jsonpath(obj=obj,expr='$.store..price')
# json_value = jsonpath.jsonpath(obj=obj,expr='$..book[2]')
# json_value = jsonpath.jsonpath(obj=obj,expr='$..book[(@.length-1)]')
# json_value = jsonpath.jsonpath(obj=obj,expr='$..book[:2]')
# json_value = jsonpath.jsonpath(obj=obj,expr='$..book[?(@.isbn)]')
json_value = jsonpath.jsonpath(obj=obj,expr='$..book[?(@.price>20)]')

print(json_value)









