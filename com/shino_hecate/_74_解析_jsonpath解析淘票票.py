# Description ==> TODO
# BelongsProject ==> sgg_spider
# BelongsPackage ==> 
# Version ==> 1.0
# CreateTime ==> 2022-11-30 19:38:40
# Author ==> _02雪乃赤瞳楪祈校条祭_艾米丽可锦木千束木更七草荠_制作委员会_start

from urllib import request

import jsonpath

import json

url = 'https://dianying.taobao.com/cityAction.json?activityId&_ksTS=1669808799446_103&jsoncallback=jsonp104&action=cityAction&n_s=new&event_submit_doGetAllRegion=true'

headers = {
# ':authority':'dianying.taobao.com',
# ':method':'GET',
# ':path':'/cityAction.json?activityId&_ksTS=1669808799446_103&jsoncallback=jsonp104&action=cityAction&n_s=new&event_submit_doGetAllRegion=true',
# ':scheme':'https',
'accept':'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
# 'accept-encoding':'gzip, deflate, br',
'accept-language':'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
'bx-v':'2.2.3',
'cookie':'tracknick=tb1179578919; _cc_=WqG3DMC9EA%3D%3D; sgcookie=E100j224ymlqDRtHmma4WEtru9GiZfg10E8z5d5dOZrZ1%2FwuOlsZyKWz37LscUukcC3Jr6WuCjjdfxN64r3JRcI8GYPaCdozIYOdOsbidloh0bz7w7GaAib8%2BYDo%2BIKx98P1; miid=6261474791882916413; enc=EQ%2BR%2Bji2b%2BbEmbUJ6OtPdFM7r77jhYXr7Md25TVaHgeFJN%2Blat%2BlnJtSF6wlFEooMn%2FB8DK3unJeb72dUUZeX24aE9lB0wnIsdtdN6zoiqA%3D; t=9b31fa784558b1e551dca01fbeb312e1; cookie2=1e3673bfb88b6863182b65f623e631df; v=0; _tb_token_=eb51867aeb17d; cna=nw0HHF+MDSkCAd0EIAufB1lP; xlly_s=1; tb_city=440100; tb_cityName="uePW3Q=="; tfstk=cByFBF9nt9BExAZRkADz3rL-xohdZH0oldoqtaju4no2O2hhilY-jVBxb0-wrXf..; l=fBELv7UngJpKwOGjBO5anurza77teIRb4sPzaNbMiIeca1rRtFsaRNCFZQM2SdtjgTCYgetzo7yoIdLHR3AgCc0c0KDtBacj3xvtaQtJe; isg=BFRUAGz6y4AoXl0pUN1Au4o1JZLGrXiXtORII-41Vl9i2fQjFr2VJ0JX2dHBIbDv',
'referer':'https://dianying.taobao.com/index.htm?spm=a1z21.3046609.city.4.73f7112aTWddWe&n_s=new&city=440100',
'sec-ch-ua':'"Microsoft Edge";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
'sec-ch-ua-mobile':'?0',
'sec-ch-ua-platform':'"Windows"',
'sec-fetch-dest':'empty',
'sec-fetch-mode':'cors',
'sec-fetch-site':'same-origin',
'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.35',
'x-requested-with':'XMLHttpRequest',
}

request01 = request.Request(url=url,headers=headers)

response01 = request.urlopen(request01)

content = response01.read().decode('utf-8')

city_str = content.split('(')[1].split(')')[0]

# print(city_str)

with open(file=r'D:\seldom\rd\Python_ProjectAll\sgg_spider\com\shino_hecate\assets\_07_tpp.json',mode='w',encoding='utf-8') as fp:
    fp.write(city_str)
    fp.close()

obj = json.load(open(file=r'D:\seldom\rd\Python_ProjectAll\sgg_spider\com\shino_hecate\assets\_07_tpp.json',mode='r',encoding='utf-8'))

json_city = jsonpath.jsonpath(obj,'$..regionName')

print(json_city)

























