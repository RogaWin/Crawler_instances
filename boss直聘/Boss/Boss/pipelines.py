# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import csv
from asyncore import dispatcher

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy import signals
from xlwt import Workbook


# 写csv文件
import csv


class BossPipeline:
    def open_spider(self, spider):
        # 打开文件，并创建一个 CSV 写入器
        filename='A:\\Code\PythonProgram\\boss直聘\\Boss\\outputDir\\' + input('输出文件名:')+'.csv'
        self.fp = open(filename, 'w', newline='', encoding='utf-8')
        self.writer = csv.writer(self.fp)

        # 写入表头
        self.writer.writerow(['位置', '公司名', '公司行业', '学历要求', '经验要求', '薪资', '技能要求', '职位'])

    def process_item(self, item, spider):
        # 将item的值按照顺序写入 CSV
        row = [
            item.get('address', ''),
            item.get('company', ''),
            item.get('companyType', ''),
            item.get('education', ''),
            item.get('experience', ''),
            item.get('salary', ''),
            item.get('skill_list', ''),
            item.get('title', '')
        ]
        self.writer.writerow(row)
        return item

    def close_spider(self, spider):
        self.fp.close()

# import xlwt
#
# class ExcelPipeline:
#     def __init__(self):
#         dispatcher.connect(self.colse_spider, signals.spider_closed)
#         self.wb = Workbook()
#         self.ws = self.wb.active
#         self.ws.append(["职位", "位置", "薪资", "经验要求", "学历要求", "公司名", "公司行业", "技能要求", "福利待遇"])
#     def process_item(self, item, spider):
#          # print(item)
#          line = [item['title'], item['address'], item['salary'],item['experience'],item['education'],item['company'],item['companyType'],item['skill_list']]
#          self.ws.append(line)
#          return item
#     def colse_spider(self, spider):
#         self.wb.save('output.xlsx')