# Description ==> TODO
# BelongsProject ==> sgg_spider
# BelongsPackage ==> 
# Version ==> 1.0
# CreateTime ==> 2022-11-30 20:54:50
# Author ==> _02雪乃赤瞳楪祈校条祭_艾米丽可锦木千束木更七草荠_制作委员会_start

from urllib import request
from bs4 import BeautifulSoup

response01 = request.urlopen(url='https://www.starbucks.com.cn/menu/')

content = response01.read().decode('utf-8')

bs_str01 = BeautifulSoup(markup=content,features='lxml')

# print(bs_str01)

cafe_names = bs_str01.select('a>strong')

img_names01 = bs_str01.select('a>div[class="preview circle"]')

print(len(cafe_names))
print(len(img_names01))

for i in range(len(cafe_names)):
    img_names = img_names01[i].attrs.get('style').split('"')[1].split('"')[0]
    # print(cafe_names[i].get_text())
    # print(img_names)
    url = 'https://www.starbucks.com.cn%s'%(img_names)
    # print(url)
    pic_name = cafe_names[i].get_text().replace('（','_').replace('）','_').replace('/','_')
    filename = r'D:\seldom\rd\Python_ProjectAll\sgg_spider\com\shino_hecate\assets\strabucks_img\%s.jpg' % (pic_name)
    request.urlretrieve(url=url,filename=filename)



# 不断地尝试最终成功了.....星巴克的图片的链接需要自己尝试出来的说
'https://www.starbucks.com.cn/images/products/cold-brew-malt.jpg'##



# 'https://www.starbucks.com.cn/menu/'
'https://www.starbucks.com.cn/menu/images/products/cold-brew-malt.jpg'
# 'https://www.starbucks.com.cn/menu/beverages/coffee-plus-ice-cream/images/products/cold-brew-malt.jpg'
'http://www.starbucks.com.cn/menu/beverages/coffee-plus-ice-cream/images/products/cold-brew-malt.jpg'
# 'images/products/cold-brew-malt.jpg'


