import os

from scrapy import signals
from scrapy.http import HtmlResponse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json



class BossSpiderMiddleware:
    @classmethod
    def from_crawler(cls, crawler):
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        return None

    def process_spider_output(self, response, result, spider):
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        pass

    def process_start_requests(self, start_requests, spider):
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)


class SeleniumMiddleware:
    query = ""
    city_id = ""

    def __init__(self):
        self.cookie_file = 'boss_cookies.json'
        # 检查文件是否存在，如果不存在则创建一个空文件
        if not os.path.exists(self.cookie_file):
            with open(self.cookie_file, 'w') as f:
                pass
        self.getcookie('https://www.zhipin.com/web/geek/job-recommend', self.cookie_file)
        self.driver = webdriver.Chrome()

    def getcookie(self, url, cookies):
        driver = webdriver.Chrome()
        driver.get(url)
        time.sleep(6)
        dict_cookies = driver.get_cookies()
        json_cookies = json.dumps(dict_cookies)
        with open(cookies, "w") as fp:
            fp.write(json_cookies)
            print('Cookies保存成功！')
        driver.quit()

    def load_cookies(self):
        with open(self.cookie_file, "r") as fp:
            cookies = json.load(fp)
        for cookie in cookies:
            if 'domain' in cookie:
                del cookie['domain']
            self.driver.add_cookie(cookie)

    def process_request(self, request, spider):
        try:
            if request.meta.get('first_request', True):
                qe = input('请搜索岗位和城市id(空格隔开):').split(' ')
                self.query = qe[0]
                self.city_id = qe[1]
                target_url = f"https://www.zhipin.com/web/geek/job?query={self.query}&city={self.city_id}&page=1"
                q: str = self.query
                c = self.city_id
                request.meta['first_request'] = False
            else:
                page = int(request.meta.get('page_number'))
                target_url = f"https://www.zhipin.com/web/geek/job?query={self.query}&city={self.city_id}&page={page}"
            print(f"Fetching URL: {target_url}")
            self.driver.get(target_url)
            self.load_cookies()
            self.driver.refresh()

            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "job-card-wrapper"))
            )

            data = self.driver.page_source
            return HtmlResponse(url=request.url, body=data, encoding='utf-8', request=request)
        except Exception as e:
            print(f"An error occurred: {e}")
            return HtmlResponse(url=request.url, status=500, request=request)

    def __del__(self):
        if self.driver:
            self.driver.quit()


