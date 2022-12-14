import scrapy
from scrapy_ddw_094.items import ScrapyDdw094Item

class DdwSpider(scrapy.Spider):
    name = 'ddw'
    allowed_domains = ['http://category.dangdang.com/cp01.01.02.00.00.00.html']
    start_urls = ['http://category.dangdang.com/cp01.01.02.00.00.00.html']

    def parse(self, response):
        # //ul[@id="component_59"]/li
        # //ul[@id="component_59"]/li/a/img/@data-original
        # //ul[@id="component_59"]/li/a/img/@alt
        # //ul[@id="component_59"]/li/p/span[@class="search_now_price"]
        print()
        print()
        li_books = response.xpath('//ul[@id="component_59"]/li')
        for li in range(len(li_books)):
            src = li_books[li].xpath('.//a/img/@data-original').extract_first()
            if src:
                src = li_books[li].xpath('.//a/img/@data-original').extract_first()
            else:
                src = li_books[li].xpath('.//a/img/@src').extract_first()
            name = li_books[li].xpath('.//a/img/@alt').extract_first()
            price = li_books[li].xpath('.//p/span[@class="search_now_price"]/text()').extract_first()
            # print(type(name))
            # print(name,'||',price,'||',src)
            book = ScrapyDdw094Item(name=name,src=src,price=price)
            yield book
        print()
        print()
