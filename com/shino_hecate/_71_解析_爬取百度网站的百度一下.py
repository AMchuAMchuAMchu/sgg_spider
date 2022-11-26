# Description ==> TODO
# BelongsProject ==> sgg_spider
# BelongsPackage ==> 
# Version ==> 1.0
# CreateTime ==> 2022-11-26 21:05:55
# Author ==> _02雪乃赤瞳楪祈校条祭_艾米丽可锦木千束木更七草荠_制作委员会_start


from lxml import etree
from urllib import request

response01 = request.urlopen(url='http://www.baidu.com')

content = response01.read().decode('utf-8')

baidu_tree = etree.HTML(text=content)

baiduOne = baidu_tree.xpath('//span/input[@id="su"]/@value')

print(baiduOne)








