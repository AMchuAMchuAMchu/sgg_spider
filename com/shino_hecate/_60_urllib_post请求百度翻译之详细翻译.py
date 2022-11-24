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
# 'Accept':'*/*',
# 'Accept-Encoding':'gzip, deflate, br',
# 'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8',
# 'Acs-Token':'1669273447716_1669288824024_9SYLeTVBFdSeC07WNbyQaC93iMmJjuOD/cc5VSNkfxRW44wyfR0jFUFCwVazcPyE28yJBE9PI767lCpfYSzCxD9NLo5YxV4G+m+0qqZYR0oUX8xkFbLwIQ8pXu9NqUoKEyPRlz20e6Pas0JeSUL15cMwqFjt+jB5dtb7xW2lheGtPbAJjeCO05zBOEsZaonmNeK0gC+pNIdsclKZ0GOkApoaivhoN5r9E0Xmjzcuh5aGDXbvt1MUzD9rhXuLJ0MIQpUrapzeCSdPrgWpeaJq64WGPCZPcXcaUqYRyuPOHyQ=',
# 'Connection':'keep-alive',
# 'Content-Length':'135',
# 'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
'Cookie':'BIDUPSID=B989E09B98B7719CE90AE6DA1BCAEE8D; PSTM=1663403509; BAIDUID=B989E09B98B7719CCB3F652D933EA615:FG=1; BAIDUID_BFESS=B989E09B98B7719CCB3F652D933EA615:FG=1; BDUSS=U54TFB0RU9EdX5ubWJXRGZjZnJINjlFSVVBWm14YzN5bzlhSXlYT1IxYmJjRjVqSVFBQUFBJCQAAAAAAAAAAAEAAADxy7PTwrfC~sL-srvAtAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANvjNmPb4zZjT; BDUSS_BFESS=U54TFB0RU9EdX5ubWJXRGZjZnJINjlFSVVBWm14YzN5bzlhSXlYT1IxYmJjRjVqSVFBQUFBJCQAAAAAAAAAAAEAAADxy7PTwrfC~sL-srvAtAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANvjNmPb4zZjT; ZFY=h0mTNxOgtPXmRsC0VJTENCAm2ybGzTr:BOf:AkRK6geHY:C; BAIDU_WISE_UID=wapp_1666502937392_657; __bid_n=1840353f8a3af244184207; BA_HECTOR=8l0g0l2g208580218h0k87nj1hns1p31f; APPGUIDE_10_0_2=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1669288811; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1669288811; ab_sr=1.0.1_ZjIwM2FmZmQ4YWQ1ZjQ5MzhkNTk3NTYwZDM3ZTMxNDg4NTEyYmUxNzE4NmRmYThmNmRjZTA4N2I2MGQ1ZDZjZGU1ZmNjZmMyMjI2NzNjYTcxMWNmYjRmOWNkMzliZmU5ODkwNjgzOGMzMzZkMjIyODA0NjNiMThhOTI4MTYxMWRiOTgxYjAxNzBiYzViMTA5YzQzMWU3N2JiNzhmZDk2MTNiNzYzY2I2MmY2ZGI2NzQyNzU4NDkwOWZiY2ZkMGUw',
# 'Host':'fanyi.baidu.com',
# 'Origin':'https://fanyi.baidu.com',
# 'Referer':'https://fanyi.baidu.com/',
# 'sec-ch-ua':'"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
# 'sec-ch-ua-mobile':'?0',
# 'sec-ch-ua-platform':'"Windows"',
# 'Sec-Fetch-Dest':'empty',
# 'Sec-Fetch-Mode':'cors',
# 'Sec-Fetch-Site':'same-origin',
# 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
# 'X-Requested-With':'XMLHttpRequest'
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

request01 = request.Request(url=url,data=data,headers=headers)

result01 = request.urlopen(request01)

content01 = result01.read().decode('utf-8')

# print(content01)

import json

content02 = json.loads(content01)

print(content02)










































