# Description ==> TODO
# BelongsProject ==> sgg_spider
# BelongsPackage ==> 
# Version ==> 1.0
# CreateTime ==> 2022-11-26 20:23:19
# Author ==> _02雪乃赤瞳楪祈校条祭_艾米丽可锦木千束木更七草荠_制作委员会_start

from lxml import etree

html_tree = etree.parse('_70_xpath的基本使用.html')

# print(html_tree)

# li_list = html_tree.xpath('//ul/li')
# li_list = html_tree.xpath('//ul/li[@id]')
# li_list = html_tree.xpath('//ul/li[@id]/text()')
# li_list = html_tree.xpath('//ul/li[@id="l1"]/text()')
# li_list = html_tree.xpath('//ul/li[@id="l1"]/@class')
# li_list = html_tree.xpath('//ul/li[contains(@id,"l")]/text()')
li_list = html_tree.xpath('//ul/li[starts-with(@id,"c")]/text()')

# print(li_list)

# print(len(li_list))
print(li_list)















