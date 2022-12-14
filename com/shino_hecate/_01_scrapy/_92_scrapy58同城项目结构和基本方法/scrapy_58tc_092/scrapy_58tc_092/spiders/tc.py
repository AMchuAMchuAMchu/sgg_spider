import scrapy


class TcSpider(scrapy.Spider):
    name = 'tc'
    allowed_domains = ['https://gz.58.com/sou/?key=%E5%89%8D%E7%AB%AF%E5%BC%80%E5%8F%91']
    start_urls = ['https://gz.58.com/sou/?key=%E5%89%8D%E7%AB%AF%E5%BC%80%E5%8F%91']

    def parse(self, response):
        print()
        print()
        print('椎名真白!!....神田空太...')
        content01 = response.xpath('//a[@class="t"]/@title')
        # print(content01)
        content01 = str(content01).split(',')
        # print(type(content01))
        # print(len(content01))
        print(content01[3])
        print(content01[3].split("'")[3])
        print()
        print()
