import scrapy


class MvSpider(scrapy.Spider):
    name = "mv"
    allowed_domains = ["dytt.dytt8.net"]
    start_urls = ["https://dytt.dytt8.net/html/gndy/china/index.html"]
    def parse(self, response):
        a_list = response.xpath('//div[@class="co_content8"]//b/a[2]')

        for a in a_list:
            name = a.xpath('./text()').extract_first()
            href = a.xpath('./@href').extract_first()
            url = 'https://dytt.dytt8.net'+href

            yield scrapy.Request(url=url,callback=self.parse_second)

    def parse_second(self,response):
        src = response.xpath('//div[@id="Zoom"]//img/@src').extract_first()
        print(src)




