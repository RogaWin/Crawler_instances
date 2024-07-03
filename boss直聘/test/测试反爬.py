import time
from random import randint, choice
import requests

url = 'https://ja.58.com/job.shtml?utm_source=sem-baidu-pc&spm=u-2few7p4vh988mb62t1.2few8w827wgt4eurg.kd_201345177084.cr_43861026238.ac_20304970.cd_11302497077865040299'

user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.0.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.0.0 Safari/537.36 Edg/100.0.0.0'
]

headers = {
    'User-Agent': choice(user_agents)
}

response = requests.get(url=url, headers=headers)

with open('test.html', 'w', encoding='utf-8') as f:
    f.write(response.text)

# 随机延时 1 到 5 秒
time.sleep(randint(1, 5))
