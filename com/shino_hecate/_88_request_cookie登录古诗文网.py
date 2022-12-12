# Description ==> TODO
# BelongsProject ==> sgg_spider
# BelongsPackage ==> 
# Version ==> 1.0
# CreateTime ==> 2022-12-08 21:06:23
# Author ==> _02雪乃赤瞳楪祈校条祭_艾米丽可锦木千束木更七草荠_制作委员会_start


import requests


'''
__VIEWSTATE: jp93JigsiGERm2dwPSsTXWUOfLaZ3rudPANuso8emoPlySlhnj+TT+60iEPE3kK84g+SKBaqqYBlaMKle6bRB3IoNlOhFguLctKGsubO/0OX87h4JcqndBbwWxMNoRF92Jzpv1muToxgl1/KSKYfXb8oJi4=
__VIEWSTATEGENERATOR: C93BE1AE
from: http://so.gushiwen.cn/user/collect.aspx
email: 236234686@qq.com
pwd: eeeeeeeee
code: llll
denglu: 登录
'''

url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}

response = requests.post(url=url,headers=headers)

# print(response.text)

response.encoding = 'utf-8'

from lxml import etree

xpath = etree.HTML(text=response.text)

# print(xpath)

__VIEWSTATE = xpath.xpath('//input[@id="__VIEWSTATE"]/@value')

__VIEWSTATEGENERATOR = xpath.xpath('//input[@id="__VIEWSTATEGENERATOR"]/@value')

print(__VIEWSTATE)

print(__VIEWSTATEGENERATOR)

code = xpath.xpath('//img[@id="imgCode"]/@src')

code_url = 'https://so.gushiwen.cn'+code[0]

# from urllib import request

# request.urlretrieve(url=code_url,filename=r'D:\seldom\rd\Python_ProjectAll\sgg_spider\com\shino_hecate\assets\code\code.jpg')

session = requests.session()

resp01 = session.get(url=code_url)

content_code = resp01.content

with open(file=r'D:\seldom\rd\Python_ProjectAll\sgg_spider\com\shino_hecate\assets\code\code.jpg',mode='wb')as fp:
    fp.write(content_code)







code_name = input('请输入验证码:')

post_data = {
'__VIEWSTATE':__VIEWSTATE,
'__VIEWSTATEGENERATOR':__VIEWSTATEGENERATOR,
'from': 'http://so.gushiwen.cn/user/collect.aspx',
'email': '236234686@qq.com',
'pwd': '79652185',
'code': code_name,
'denglu': '登录',
}

response01 = session.post(url=url,headers=headers,data=post_data)

content01 = response01.text

with open(file=r'D:\seldom\rd\Python_ProjectAll\sgg_spider\com\shino_hecate\assets\code\gushiwen.html',mode='w',encoding='utf-8')as fp:
    fp.write(content01)
    fp.close()



































