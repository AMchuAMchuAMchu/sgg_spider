# Description ==> TODO
# BelongsProject ==> sgg_spider
# BelongsPackage ==> 
# Version ==> 1.0
# CreateTime ==> 2022-11-23 20:29:03
# Author ==> _02雪乃赤瞳楪祈校条祭_艾米丽可锦木千束木更七草荠_制作委员会_start

from urllib import parse

args = {
    'q':'那朵花',
    'director':'长井龙雪'
}



url02 = parse.urlencode(args)
url = 'https://cn.bing.com/search?%s'%(url02)

print(url)














