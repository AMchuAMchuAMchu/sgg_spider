# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class ScrapyDdw094Pipeline:

    def open_spider(self,spider):
        self.fp = open(file='book.json',mode='w',encoding='utf-8')
        self.fp.write('[')

    def process_item(self, item, spider):
        self.fp.write(str(item))
        if item:
            self.fp.write(',')
        return item

    def close_spider(self,spider):
        self.fp.write(']')
        self.fp.close()



