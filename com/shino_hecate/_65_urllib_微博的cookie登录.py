# Description ==> TODO
# BelongsProject ==> sgg_spider
# BelongsPackage ==> 
# Version ==> 1.0
# CreateTime ==> 2022-11-25 20:45:07
# Author ==> _02雪乃赤瞳楪祈校条祭_艾米丽可锦木千束木更七草荠_制作委员会_start

from urllib import request

url = 'https://weibo.com/u/7231735697'


headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.35'
}

request01 = request.Request(url=url,headers=headers)

response01 = request.urlopen(request01)

content = response01.read().decode('gb2312')

print(content)
file=r'D:\seldom\rd\Python_ProjectAll\sgg_spider\com\shino_hecate\assets\_04_weibo_login.html'
with open(file=file,mode='w',encoding='gb2312') as fp:
    fp.writelines(content)


