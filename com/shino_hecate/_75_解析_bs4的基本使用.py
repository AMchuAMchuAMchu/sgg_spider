# Description ==> TODO
# BelongsProject ==> sgg_spider
# BelongsPackage ==> 
# Version ==> 1.0
# CreateTime ==> 2022-11-30 20:19:07
# Author ==> _02雪乃赤瞳楪祈校条祭_艾米丽可锦木千束木更七草荠_制作委员会_start


from bs4 import BeautifulSoup

file = open(file=r'D:\seldom\rd\Python_ProjectAll\sgg_spider\com\shino_hecate\_75_解析_bs4的基本使用.html',mode='r',encoding='utf-8')

bs_res01 = BeautifulSoup(markup=file,features='lxml')

# print(bs_res01.a)
# print(bs_res01.a.attrs)

# print(bs_res01.find('a'))
# print(bs_res01.find('a',title='a2'))
# print(bs_res01.find('a',class_='a1'))
# print(bs_res01.find_all('a'))
# print(bs_res01.find_all(['a','span']))
# print(bs_res01.find_all('li',limit=2))
# print(bs_res01.select('a'))
# print(bs_res01.select('.a1'))
# print(bs_res01.select('#a2'))
# print(bs_res01.select('li[id=l2]'))








# bs_res = bs_res01.select('li')
# print(type(bs_res))

# for i in range(len(bs_res)):
#     print(bs_res[i].string)

# 注意返回值是列表的说
bs_res02 = bs_res01.select('#s1')[0]

# print(bs_res02.name)
# print(bs_res02.attrs)
print(bs_res02.attrs.get('class')[0])










