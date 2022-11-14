# Description ==> TODO
# BelongsProject ==> sgg_spider
# BelongsPackage ==> 
# Version ==> 1.0
# CreateTime ==> 2022-11-14 17:33:27
# Author ==> _02雪乃赤瞳楪祈校条祭_艾米丽可锦木千束木更七草荠_制作委员会_start


import requests

from bs4 import BeautifulSoup


result01 = requests.request(method='get',url='https://explorer.altmetric.com/details/77676422/twitter/page:2?_pjax=.content-panel&_pjax=.content-panel')

result01.encoding = 'utf-8'

print(result01.ok)

result002 = BeautifulSoup(result01.text,parser='html.parser')
i = 0
for item in result002.select('.summary'):
    i += 1
    print(i,'==>',item)








