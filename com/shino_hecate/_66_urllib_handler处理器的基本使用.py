# Description ==> TODO
# BelongsProject ==> sgg_spider
# BelongsPackage ==> 
# Version ==> 1.0
# CreateTime ==> 2022-11-26 19:19:47
# Author ==> _02雪乃赤瞳楪祈校条祭_艾米丽可锦木千束木更七草荠_制作委员会_start

from urllib import request

url = 'http://www.baidu.com'

headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.35',
}

request01 = request.Request(url=url,headers=headers)

handler01 = request.HTTPHandler()

opener01 = request.build_opener(handler01)

response01 = opener01.open(request01)

content = response01.read().decode('utf-8')

print(content)




























