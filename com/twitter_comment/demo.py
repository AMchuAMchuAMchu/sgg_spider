# Description ==> TODO
# BelongsProject ==> sgg_spider
# BelongsPackage ==> 
# Version ==> 1.0
# CreateTime ==> 2022-11-14 17:33:27
# Author ==> _02雪乃赤瞳楪祈校条祭_艾米丽可锦木千束木更七草荠_制作委员会_start


import requests

from bs4 import BeautifulSoup


file = open(file='d:/twitter_comment.txt',encoding='utf-8',mode='w')
for i in range(1,101,1):
    print('====>',i)
    result01 = requests.request(method='get',
                                url='https://explorer.altmetric.com/details/82549788/twitter/page:%d'%(i))
                                # 1.0 url='https://explorer.altmetric.com/details/77676422/twitter/page:%d'%(i))
                                # 2.0 'https://explorer.altmetric.com/details/94531651/twitter/page:2?'
                                # 3.0 'https://explorer.altmetric.com/details/91957925/twitter/page:2?_pjax=.content-panel'
                                # 4.0 'https://explorer.altmetric.com/details/77699394/twitter/page:2?_pjax=.content-panel'
                                # 5.0 'https://explorer.altmetric.com/details/82549788/twitter/page:2?_pjax=.content-panel'
    result01.encoding = 'utf-8'

    result002 = BeautifulSoup(result01.text, 'html.parser')
    i = 0
    for item in result002.select('.summary'):
        i += 1
        if i >= 5:
            res = '第%d条=>%s'%(i-4,item.text)
            file.writelines(res)
            file.write('\n')
            print('第',i-4,'条','==>',item.text)










