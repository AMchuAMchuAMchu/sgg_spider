# Description ==> TODO
# BelongsProject ==> sgg_spider
# BelongsPackage ==> 
# Version ==> 1.0
# CreateTime ==> 2022-11-23 20:43:00
# Author ==> _02雪乃赤瞳楪祈校条祭_艾米丽可锦木千束木更七草荠_制作委员会_start


from urllib import request
from urllib import parse
import json


url = 'https://fanyi.baidu.com/sug'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.35'
}

data = {
    'kw': 'spider'
}

data01 = parse.urlencode(data).encode('utf-8')

request01 = request.Request(url=url, data=data01, headers=headers)

result01 = request.urlopen(request01)

result02 = result01.read().decode('utf-8')

print(result02)


content03 = json.loads(result02)

print(content03)
