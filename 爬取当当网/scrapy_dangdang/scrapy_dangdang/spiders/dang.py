import scrapy
from ..items import ScrapyDangdangItem
class DangSpider(scrapy.Spider):
    name = "dang"
    allowed_domains = ["category.dangdang.com"]
    start_urls = ["https://category.dangdang.com/cp01.01.02.00.00.00.html"]
    base_url = 'https://category.dangdang.com/pg'
    page = 1
    def parse(self, response):
        # pipelines 下载数据
        # items 定义数据结构
        # 通俗的说你要下载的数据都有什么
        # src = '//ul[@id="component_59"]/li//img/@src'
        # name = '//ul[@id="component_59"]/li//img/@alt'
        # price = '//ul[@id="component_59"]/li//p[@class="price"]/span[1]'
        # 所有的seletor的对象都可以再次调用xpath方法
        li_list = response.xpath('//ul[@id="component_59"]/li')
        print(f"Number of items found: {len(li_list)}===============================================")  # 打印出找到的元素数量
        for li in li_list:
            src = li.xpath('.//img/@data-original').extract_first()
            # 第一张的src是没问题的其他的是有问题的
            if src:
                src = src
            else:
                src = li.xpath('.//img/@src').extract_first()
            name = li.xpath('.//img/@alt').extract_first()
            price = li.xpath('.//p[@class="price"]/span[1]/text()').extract_first()
            book = ScrapyDangdangItem(src=src,name=name,price=price)
            # 给管道
            yield book
        if self.page < 100:
            self.page = self.page + 1
        url = self.base_url+str(self.page)+'-cp01.01.02.00.00.00.html'
        yield scrapy.Request(url=url, callback=self.parse)

