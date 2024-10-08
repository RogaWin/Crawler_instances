import requests
import re
import json
import os

# 确保保存视频和音频的目录存在
dir_path = '.\\dir\\'
if not os.path.exists(dir_path):
    os.makedirs(dir_path)

# TODO 记得更改你要的url和你自己的cookie
url = input('请输入要爬取的网站:\n')
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0',
    'Cookie': "buvid3=7D544545-F9CB-CFBC-AC01-7BA57BC1DCD254930infoc; b_nut=1716982754; _uuid=DE6463C7-665D-B959-85C2-8E63E37ED55857684infoc; buvid4=C3AB4840-6DDF-47A8-7E4D-B862E6E82D1D57976-024052911-kWwIJXuJHj9I1jCGBKKVHg%3D%3D; rpdid=|(km||m)))Yk0J'u~uYm)k~Y|; enable_web_push=DISABLE; header_theme_version=CLOSE; DedeUserID=291132045; DedeUserID__ckMd5=32793a75c8c79edd; hit-dyn-v2=1; is-2022-channel=1; CURRENT_QUALITY=80; SESSDATA=ca51c7d5%2C1733362791%2C473e4%2A61CjANeuyyefTAJnHs6SbK32mhcGo9LC-1DzW7gVjGuDjw1S_9x6mJwCHokWqWAWUzdcQSVmFfZm13OWhtaktrWlptbkpWX1NQQ2FBeVZVSlphZEhzX3lqWWcwNV80S1JTbXFySHJFY1RzSVJOTG5RU1hsb3d4YWtTVnFjQ1NlSXExaEpOT1VCaF9RIIEC; bili_jct=46e6f550556ff8183b6b987e944994ff; LIVE_BUVID=AUTO3317178108184590; PVID=1; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MTgwNzAwMjMsImlhdCI6MTcxNzgxMDc2MywicGx0IjotMX0._LIkEYz7Rv7opI0VYBl_rFxgS52DAFand_4AvcGs4KQ; bili_ticket_expires=1718069963; buvid_fp_plain=undefined; sid=7n8yqi9u; bp_t_offset_291132045=941002775987224581; CURRENT_BLACKGAP=0; home_feed_column=5; browser_resolution=1528-838; CURRENT_FNVAL=4048; fingerprint=8eca77d2d9d27abe83de268a24ba02b0; b_lsid=104611E39_18FFD1D1BE9; buvid_fp=8eca77d2d9d27abe83de268a24ba02b0"
}

try:
    # 发送请求
    response = requests.get(url=url, headers=headers)
    response.raise_for_status()  # 如果请求失败，则引发异常

    html = response.text

    # 解析数据: 提取视频标题
    title = re.findall('title="(.*?)"', html)
    if not title:
        raise ValueError("未找到视频标题")
    title = title[0]

    # 处理文件名中的特殊字符
    safe_title = re.sub(r'[<>:"/\\|?*]', '', title)

    # 提取视频信息
    info = re.findall('window.__playinfo__=(.*?)</script>', html)
    if not info:
        raise ValueError("未找到视频信息")
    info = info[0]

    # info -> json字符串转成json字典
    json_data = json.loads(info)

    # 提取视频链接
    video_url = json_data['data']['dash']['video'][0]['baseUrl']
    audio_url = json_data['data']['dash']['audio'][0]['baseUrl']

    # 下载视频和音频
    video_content = requests.get(url=video_url, headers=headers).content
    audio_content = requests.get(url=audio_url, headers=headers).content

    # 保存数据
    with open(os.path.join(dir_path, safe_title + '.mp4'), mode='wb') as v:
        v.write(video_content)
    with open(os.path.join(dir_path, safe_title + '.mp3'), mode='wb') as a:
        a.write(audio_content)

    print("下载完成！")

except requests.RequestException as e:
    print(f"请求错误: {e}")
except ValueError as e:
    print(f"数据解析错误: {e}")
except Exception as e:
    print(f"发生错误: {e}")
