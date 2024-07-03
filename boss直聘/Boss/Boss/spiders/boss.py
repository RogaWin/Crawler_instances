import scrapy
from ..items import BossItem


class BossSpider(scrapy.Spider):
    name = "boss"
    allowed_domains = ["www.zhipin.com"]
    start_urls = ["https://www.zhipin.com/"]
    page = 1

    def parse(self, response):
        with open('test.html', 'w', encoding='utf-8') as f:
            f.write(response.text)

        # 改进的XPath表达式
        li_list = response.xpath('//li[@class="job-card-wrapper"]')
        print(f"Number of items found: {len(li_list)}===============================================")

        for li in li_list:
            title = li.xpath(".//span[@class='job-name']/text()").extract_first() or ''
            salary = li.xpath(".//span[@class='salary']/text()").extract_first() or ''
            area = li.xpath(".//span[@class='job-area']/text()").extract_first() or ''

            # 确保提取job_lable_list的正确性
            job_lable_list = li.xpath(".//ul[@class='tag-list']//text()").extract()
            if len(job_lable_list) >= 2:
                experience = job_lable_list[0] or ''
                education = job_lable_list[1] or ''
            else:
                experience = ''
                education = ''

            company = li.xpath(".//h3[@class='company-name']/a/text()").extract_first() or ''

            # 确保提取company_message的正确性
            company_message = li.xpath(".//ul[@class='company-tag-list']//text()").extract()
            company_type = company_message[0] if company_message else ''

            # 提取boon字段
            boon = li.xpath('.//div[@class="job_card_footer"]//div[@class="info-desc"]/text()').extract()
            boon = boon[0] if boon else None
            # 技能
            skill_list = li.xpath(
                ".//div[@class='job-card-footer clearfix']//ul[@class='tag-list']/li/text()").extract() or []
            skill = "|".join(skill_list)
            # 创建BossItem对象并传递数据
            book = BossItem(
                title=title,
                address=area,
                salary=salary,
                experience=experience,
                education=education,
                company=company,
                companyType=company_type,
                skill_list=skill,
            )
            yield book

        if self.page < 10:
            self.page += 1
            next_url = f"https://www.zhipin.com/web/geek/job?query=java&city=101210100&page={self.page}"
            yield scrapy.Request(
                url=next_url,
                callback=self.parse,
                meta={'page_number': self.page, 'first_request': False}
            )
