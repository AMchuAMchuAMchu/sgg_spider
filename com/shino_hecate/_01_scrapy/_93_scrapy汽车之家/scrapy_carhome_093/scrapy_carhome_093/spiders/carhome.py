import scrapy


class CarhomeSpider(scrapy.Spider):
    name = 'carhome'
    allowed_domains = ['https://car.autohome.com.cn/price/brand-15.html']
    start_urls = ['https://car.autohome.com.cn/price/brand-15.html']

    def parse(self, response):
        print()
        print()
        car_name = response.xpath('//a[@class="font-bold"]/text()')
        car_price = response.xpath('//span[@class="font-arial"]/text()')
        print(len(car_name))
        print(len(car_price))
        for i in range(len(car_name)):
            print(car_name[i].extract(),'  ',car_price[i].extract())
        print()
        print()

