import scrapy


class MvSpider(scrapy.Spider):
    name = 'mv'
    allowed_domains = ['dy.dytt8.net']
    start_urls = ['https://dy.dytt8.net/index2.htm']

    def parse(self, response):
        print()
        print()
        print('椎名真白....')
        print()
        print()
        # pass

