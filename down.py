import youtube_dl
import time
import requests
import json
import asyncio
from pyppeteer import launch

from pyquery import PyQuery as pq

API_URL = "https://liveapi.huya.com/moment/getMomentContent?&videoId={}"
# @retry(stop_max_attempt_number=7, wait_fixed=5000)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}

def down(data,name):
    ydl_opts = {
        'nooverwrites': True,
        'ignoreerrors': True,
        'retries': True,
        'outtmpl': name,
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([data])



with open("/Users/ming/projects/huyaPyDwon/down.txt" , 'r') as f:
    list = f.readlines()
    # print(list)
    list = [i.strip()[24:33] for i in list]
    list = [API_URL.format(i) for i in list]
    for l in list:
        data = json.loads(requests.get(l, headers=headers).text)

        m3u8Link = data['data']['moment']['videoInfo']['definitions'][0]['m3u8']
        name  = data['data']['moment']['videoInfo']['videoTitle']

        down(m3u8Link,name)
        
        time.sleep(5)
    
# url = "https://liveapi.huya.com/moment/getMomentContent?&videoId=508767507"

# data = requests.get(url, headers=headers)
# print(data.text, type(data))


# async def main(): 
#     browser = await launch()
#     page = await browser.newPage()
#     await page.goto(url)
#     # await page.waitForSelector('.content-list .statpid')
#     doc = await page.content()
#     # print(doc)
#     # doc = json.loads(doc)
#     doc = str(doc)
#     print(type(doc), doc[84:20])
#     await browser.close()

# asyncio.get_event_loop().run_until_complete(main())

    
# data = json.loads(requests.get(url, headers=headers).text)

# m3u8Link = data['data']['moment']['videoInfo']['definitions'][0]['m3u8']

# down(m3u8Link)


# while True:
    # data = pyperclip.paste()
    # data = str(data)
    # if (data == recent_data):
    #     print('文本相同, 3s后重新开始监听')
    #     time.sleep(3)
    #     continue
    # else:
    #     print('文本不同, 尝试下载')
    #     if (data.startswith("https")):
    #         # print(data)
    #         #     @retry(stop_max_attempt_number=7)
    #         #     try:
    #         #         ydl_opts = {
    #         #             'nooverwrites': True,
    #         #             'ignoreerrors': True
    #         #         }
    #         #         with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    #         #             ydl.download([data])
    #         #             recent_data = data
    #         #             continue
    #         #     except expression as identifier:
    #         #         pass
    #         down(data)
    #         recent_data = data
    #         continue
    #     else:
    #         print('文本非链接, 3s后重新开始监听')
    #         time.sleep(3)
    #         recent_data = data
    #         continue


# def onread():
#     data = pyperclip.paste()
#     while True:
#         with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#         ydl.download([youtube_url])
#         continue

# onread()

# data = pyperclip.paste()
# url = 'https://www.youtube.com/watch?v=Flf_7bpuxJU&t=141s'

# while True:
#         data = pyperclip.paste()
#         data= str(data)
#         if (data.startswith("https")):
#                 # print(data)
#                 ydl_opts = {}
#                 with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#                         ydl.download([data])
#                         continue
#         else:
#                 print('no')
#                 continue
