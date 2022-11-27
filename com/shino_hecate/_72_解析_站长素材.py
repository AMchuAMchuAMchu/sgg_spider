# Description ==> TODO
# BelongsProject ==> sgg_spider
# BelongsPackage ==> 
# Version ==> 1.0
# CreateTime ==> 2022-11-27 20:19:43
# Author ==> _02雪乃赤瞳楪祈校条祭_艾米丽可锦木千束木更七草荠_制作委员会_start
from urllib import request
from lxml import etree


def acquire_pic(page):
    if page == 1:
        url = 'https://sc.chinaz.com/tupian/qinglvtupian.html'
    else:
        url = 'https://sc.chinaz.com/tupian/qinglvtupian_%s.html' % (page)
    # print(url)

    response01 = request.urlopen(url=url)

    content = response01.read().decode('utf-8')

    # print(content)

    content_html = etree.HTML(text=content)

    content_data_origin = content_html.xpath('//div[@class="item"]/img/@data-original')
    content_title = content_html.xpath('//div[@class="item"]/img/@alt')

    print(len(content_data_origin))
    print(len(content_title))


if __name__ == '__main__':

    start_page = int(input('请输入图片首页:'))
    end_page = int(input('请输入图片尾页:'))
    print('阿里嘎多~~')

    for page in range(start_page, end_page + 1):
        acquire_pic(page)
