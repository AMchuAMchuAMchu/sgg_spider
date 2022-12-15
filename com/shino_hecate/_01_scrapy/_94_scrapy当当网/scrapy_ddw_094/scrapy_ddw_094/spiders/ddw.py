import scrapy
from scrapy_ddw_094.items import ScrapyDdw094Item

class DdwSpider(scrapy.Spider):
    name = 'ddw'
    allowed_domains = ['category.dangdang.com']
    start_urls = ['http://category.dangdang.com/cp01.01.02.00.00.00.html']
    # http://category.dangdang.com/pg2-cp01.01.02.00.00.00.html
    base_url = 'http://category.dangdang.com/pg'
    page = 1

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

#             # http://category.dangdang.com/pg2-cp01.01.02.00.00.00.html
        if self.page < 100:
            self.page = self.page +1
            url = self.base_url + str(self.page) + '-cp01.01.02.00.00.00.html'
            yield scrapy.Request(url=url,callback=self.parse)
