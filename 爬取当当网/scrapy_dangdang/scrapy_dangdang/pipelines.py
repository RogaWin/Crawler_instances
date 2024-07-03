# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import os
import requests
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

# 如果想要使用管道就要开管道
class ScrapyDangdangPipeline:
    def open_spider(self, spider):
        self.fp = open('book.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        self.fp.write(str(item) + "\n")  # 写入每个item后加上换行符，确保每个item独立一行
        return item

    def close_spider(self, spider):
        self.fp.close()

class DangDangDownloadPipeline:
    def process_item(self, item, spider):
        url = item.get('src')
        if not url.startswith('http'):
            url = 'http:' + url  # 如果url不包含协议部分，添加'http:'

        filename = os.path.join('./scrapy_dangdang/books', item.get('name') + '.jpg')

        # 创建目录（如果不存在）
        os.makedirs(os.path.dirname(filename), exist_ok=True)

        try:
            response = requests.get(url)
            response.raise_for_status()  # 检查请求是否成功

            with open(filename, 'wb') as fimg:
                fimg.write(response.content)  # 将图片数据写入文件
        except requests.RequestException as e:
            spider.logger.error(f"Failed to download image {url}: {e}")

        return item
