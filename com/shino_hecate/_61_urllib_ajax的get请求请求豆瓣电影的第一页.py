# Description ==> TODO
# BelongsProject ==> sgg_spider
# BelongsPackage ==> 
# Version ==> 1.0
# CreateTime ==> 2022-11-24 20:02:59
# Author ==> _02雪乃赤瞳楪祈校条祭_艾米丽可锦木千束木更七草荠_制作委员会_start

from urllib import request
from urllib import parse


url = 'https://movie.douban.com/j/chart/top_list?type=25&interval_id=100%3A90&action=&start=0&limit=20'

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.35'
}

request01 = request.Request(url=url,headers=headers)

result01 = request.urlopen(request01)

result02 = result01.read().decode('utf-8')

print(result02)

file = open(file=r'D:\seldom\rd\Python_ProjectAll\sgg_spider\com\shino_hecate\assets\_01_douban_01.json',mode='w',encoding='utf-8')

file.write(result02)

file.close()





















