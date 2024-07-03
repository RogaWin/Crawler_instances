from selenium import webdriver
import time
import json
import random
from bs4 import BeautifulSoup
import pandas as pd


def 获取cookie(url, cookie文件名):
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(15)
    dictCookies = driver.get_cookies()  # 获得所有cookie信息(返回是字典)
    jsonCookies = json.dumps(dictCookies)  # dumps是将dict转化成str格式
    # 登录完成后,将cookies保存到本地文件
    with open(cookie文件名, "w") as fp:
        fp.write(jsonCookies)
        print('cookies保存成功！')


获取cookie('https://www.zhipin.com/web/geek/job-recommend', cookie文件名='boss直聘.json')

详情列表 = []
for i in range(1, 11):
    print(i)
    boss = webdriver.Chrome()
    # 打开网页
    url = f'https://www.zhipin.com/web/geek/job?query=bi&city=101210100&page={i}'

    boss.get(url)
    # 2.注入cookie
    with open(r"boss直聘.json", "r") as fp:
        jsonCookies = fp.read()
    # 将 JSON 格式的 Cookie 转换为字典
    cookies = json.loads(jsonCookies)
    # 添加 Cookie 到 WebDriver 对象
    for cookie in cookies:
        boss.add_cookie(cookie)
    boss.get(url)
    time.sleep(6)
    boss_text = boss.page_source
    print("2. 获取页面源代码")
    with open(f'test{i}.html', 'w', encoding='utf-8') as f:
        f.write(boss_text)

    from bs4 import BeautifulSoup

    soup = BeautifulSoup(boss_text, 'html.parser')
    # 查找所有 class="job-card-left" 的元素
    job_card_left_elements = soup.find_all(class_='job-card-left')
    # 遍历每个元素，获取 <a> 标签的 href 链接
    for element in job_card_left_elements:
        href = element['href']
        full_link = 'https://www.zhipin.com' + href
        详情列表.append(full_link)
    count = 0




# 源代码 = []






# for i in 详情列表:
#     count = count + 1
#     boss = webdriver.Chrome()
#     # 打开网页
#     url = f'{i}'
#     boss.get(url)
#     # 2.注入cookie
#     with open(r"boss直聘.json", "r") as fp:
#         jsonCookies = fp.read()
#     '1. 将 JSON 格式的 Cookie 转换为字典'
#     cookies = json.loads(jsonCookies)
#     ' # 添加 Cookie 到 WebDriver 对象'
#     for cookie in cookies:
#         boss.add_cookie(cookie)
#     boss.get(url)
#     time.sleep(random.uniform(5, 15))
#     boss_text = boss.page_source
#     源代码.append(boss_text)
#     boss.close()
