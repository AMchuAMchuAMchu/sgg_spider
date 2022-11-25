# Description ==> TODO
# BelongsProject ==> sgg_spider
# BelongsPackage ==> 
# Version ==> 1.0
# CreateTime ==> 2022-11-25 20:45:07
# Author ==> _02雪乃赤瞳楪祈校条祭_艾米丽可锦木千束木更七草荠_制作委员会_start

from urllib import request

url = 'https://weibo.com/u/7231735697'


headers = {
    'cookie':'SINAGLOBAL=8872733439021.94.1633827353996; UOR=,,www.bilibili.com; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WF-jen-GcHnhwUiWDWw9dlI5JpX5KMhUgL.FoMEe02Ne0-c1KM2dJLoIc7LxK.L1h-L1KzLxKnLB.qL1hMLxKBLBonL1h.LxK-LBoMLBK2LxKqL1KMLBK5LxKBLB.2LB.2LxK.L1KMLB--LxKqLBoBLBK-LxKBLBonLBoBLxKqLBonL122LxKMLB.-LBK2LxK.LBo2LB.et; ULV=1667812192073:14:1:1:6317003198842.393.1667812192047:1666949297999; PC_TOKEN=bdfde57356; ALF=1700916546; SSOLoginState=1669380546; SCF=Av5CdUdAJZXyFKhZimhnL-PpxK3NHzSqsRRPfCDo_y3Oh4m7c25QQB5cMyD9GO99CaplmEtEjls2nrJykyJh0x4.; SUB=_2A25OhMmVDeRhGeFM6FMW8yvKwjuIHXVt87xdrDV8PUNbmtAKLW3ikW9NQMNkT4ZAMqetjnj9YcKTn2B2DatElbsv; XSRF-TOKEN=tP65p48ElDUByp0UCCX6pFPw; WBPSESS=toVtmjnnTqP5PzYsEwjQGdBdnauzoemIzYZ66unXacnooPuBeAWzU3DW0FXZ3ZOwhTBaKTCjnHu_ya2eTvc-3cYeMbAZ2lVkzTB-4bqSjdAG9evvow3r95tO_7QChaC4G_TzoJTD0y2iVkaqUiovwA==',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.35'
}

request01 = request.Request(url=url,headers=headers)

response01 = request.urlopen(request01)

content = response01.read().decode('gb2312')

print(content)
file=r'D:\seldom\rd\Python_ProjectAll\sgg_spider\com\shino_hecate\assets\_04_weibo_login.html'
with open(file=file,mode='w',encoding='gb2312') as fp:
    fp.writelines(content)


