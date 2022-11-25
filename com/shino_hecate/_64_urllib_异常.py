# Description ==> TODO
# BelongsProject ==> sgg_spider
# BelongsPackage ==> 
# Version ==> 1.0
# CreateTime ==> 2022-11-25 20:30:56
# Author ==> _02雪乃赤瞳楪祈校条祭_艾米丽可锦木千束木更七草荠_制作委员会_start
from urllib import request



# url = 'https://baike.baidu.com/item/%E6%A4%8E%E5%90%8D%E7%9C%9F%E7%99%BD/10073247'
url = 'https://baikeA.baidu.com/item/%E6%A4%8E%E5%90%8D%E7%9C%9F%E7%99%BD/10073247'

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.35'
}

try:
    request01 = request.Request(url=url,headers=headers)

    response01 = request.urlopen(request01)

    content = response01.read().decode('utf-8')

    print(content)
except Exception:
    print('系统正在升级....果咩捏~~^_^')

















