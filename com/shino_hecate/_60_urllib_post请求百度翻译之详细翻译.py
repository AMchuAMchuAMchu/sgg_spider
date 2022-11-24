# Description ==> TODO
# BelongsProject ==> sgg_spider
# BelongsPackage ==> 
# Version ==> 1.0
# CreateTime ==> 2022-11-23 20:43:00
# Author ==> _02雪乃赤瞳楪祈校条祭_艾米丽可锦木千束木更七草荠_制作委员会_start


from urllib import request
from urllib import parse
import json

url = 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
}

data_origin = {
'from':'en',
'to':'zh',
'query':'love',
'transtype':'realtime',
'simple_means_flag':'3',
'sign':'198772.518981',
'token':'6d788ed1d5bae487e2e6bfdd5dab50d0',
'domain':'common'
}

data = parse.urlencode(data_origin).encode('utf-8')

request01 = request.Request(url=url,headers=headers,data=data)

result01 = request.urlopen(request01)

content01 = result01.read().decode('utf-8')

print(content01)

import json

content02 = json.loads(content01)

print(content02)










































