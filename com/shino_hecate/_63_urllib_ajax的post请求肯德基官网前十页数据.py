# Description ==> TODO
# BelongsProject ==> sgg_spider
# BelongsPackage ==> 
# Version ==> 1.0
# CreateTime ==> 2022-11-25 20:02:56
# Author ==> _02雪乃赤瞳楪祈校条祭_艾米丽可锦木千束木更七草荠_制作委员会_start

#
# POST
# cname:广州
# pid:
# pageIndex:2
# pageSize:10


from urllib import request
from urllib import parse


def create_request(page):
    base_url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.35'
    }

    data = {
        'cname':'广州',
        'pid':'',
        'pageIndex':page,
        'pageSize':'10'
    }

    url = base_url
    data = parse.urlencode(data).encode('utf-8')
    # print(url)

    request_pretend = request.Request(url=url,data=data,headers=headers)

    content = request.urlopen(request_pretend)

    content_str = content.read().decode('utf-8')

    file.writelines(content_str)
    file.write('\n')




# 程序的入口
if __name__ == '__main__':
    start_page = int(input('请输入其实的页码:'))
    end_page = int(input('请输入结束页码:'))
    file = open(file=r'D:\seldom\rd\Python_ProjectAll\sgg_spider\com\shino_hecate\assets\_03_kfc_10.json',mode='w',encoding='utf-8')


    for page in range(start_page,end_page+1):
        create_request(page)













