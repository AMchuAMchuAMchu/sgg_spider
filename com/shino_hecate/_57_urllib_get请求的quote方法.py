# Description ==> TODO
# BelongsProject ==> sgg_spider
# BelongsPackage ==> 
# Version ==> 1.0
# CreateTime ==> 2022-11-23 20:14:05
# Author ==> _02雪乃赤瞳楪祈校条祭_艾米丽可锦木千束木更七草荠_制作委员会_start


from urllib import request
from urllib import parse

name = parse.quote('那朵花')

url = 'https://cn.bing.com/search?q=%s'%(name)
print(url)
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.35'
}

request01 = request.Request(url=url,headers=headers)

res02 = request.urlopen(request01)

result01 = res02.read().decode('utf-8')

print(result01)




