# Description ==> TODO
# BelongsProject ==> sgg_spider
# BelongsPackage ==> 
# Version ==> 1.0
# CreateTime ==> 2022-11-26 19:46:46
# Author ==> _02雪乃赤瞳楪祈校条祭_艾米丽可锦木千束木更七草荠_制作委员会_start

from urllib import request

url = 'https://www.baidu.com/s?wd=ip'

headers = {
    'Accept': '*/*',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.35',
    'Cookie': '__yjs_duid=1_a1a27cb75a603e42c0b446919e63c65a1633649170913; BIDUPSID=99831FF1A951037F4998883D2E0CC602; PSTM=1635851880; MAWEBCUID=web_aLtEFvllYyTTQsVZWMAHLceFrxNvykDpxUMHVdtqulzheCNstN; BDUSS=mltbEU4aGp-eThKdzl6SjdUM1lNdnVOWHhmOHd2ZFNtR2tISkpyUFdBaGFrUUZqSVFBQUFBJCQAAAAAAAAAAAEAAADxy7PTwrfC~sL-srvAtAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFoE2mJaBNpiY; BAIDUID=2D2B23757BB9FF3DF3607626B7D00524:FG=1; BDUSS_BFESS=mltbEU4aGp-eThKdzl6SjdUM1lNdnVOWHhmOHd2ZFNtR2tISkpyUFdBaGFrUUZqSVFBQUFBJCQAAAAAAAAAAAEAAADxy7PTwrfC~sL-srvAtAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFoE2mJaBNpiY; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; ab_sr=1.0.1_NDNkYTk0ZmVjYzk4OGJhYzkxOGYwMGUyZWUzODkwNDAzOGNjMWE4NTczMjg5Yjc5YjMwMjU4Yjc3NzM4NTBhZTljOWQ0NGY2ZmU2ZmExOGVlZGI2ZTAyNjYyN2ZmYjEzNWY2MDNmNWY3ODY2YWY3ZWYyZWZlNDE0MzdmOTRmMjU3MzY1NDYzMmU1OGYxNjcyODk0YzkxNWYxMTkyODA5NWEzZWY4OTlhNWM5MWJhMTEyYTI4MjZkYmNkZmFkZDE1; H_PS_PSSID=36545_37555_37771_37140_34813_37778_37814_37760_37742_26350_37785; BAIDUID_BFESS=2D2B23757BB9FF3DF3607626B7D00524:FG=1'
}

request01 = request.Request(url=url,headers=headers)

response01 = request.urlopen(request01)

content = response01.read().decode('utf-8')

print(content)

with open(file=r'D:\seldom\rd\Python_ProjectAll\sgg_spider\com\shino_hecate\assets\_05_proxy.html',mode='w',encoding='utf-8') as fp:
    fp.writelines(content)
    fp.close()







