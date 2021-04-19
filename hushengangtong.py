#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 17:34:03 2021

@author: lambda
"""
import aiohttp
import asyncio
import re
import os
import sys
import json
import random
import pandas as pd
import datetime
import time
import requests as request
from lxml import etree

user_agent = [
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; rv:11.0) like Gecko",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
    "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
    "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
    "Mozilla/5.0 (iPod; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
    "Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
    "Mozilla/5.0 (Linux; U; Android 2.3.7; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "Opera/9.80 (Android 2.3.4; Linux; Opera Mobi/build-1107180945; U; en-GB) Presto/2.8.149 Version/11.10",
    "Mozilla/5.0 (Linux; U; Android 3.0; en-us; Xoom Build/HRI39) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13",
    "Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en) AppleWebKit/534.1+ (KHTML, like Gecko) Version/6.0.0.337 Mobile Safari/534.1+",
    "Mozilla/5.0 (hp-tablet; Linux; hpwOS/3.0.0; U; en-US) AppleWebKit/534.6 (KHTML, like Gecko) wOSBrowser/233.70 Safari/534.6 TouchPad/1.0",
    "Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaN97-1/20.0.019; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) BrowserNG/7.1.18124",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; HTC; Titan)",
    "UCWEB7.0.2.37/28/999",
    "NOKIA5700/ UCWEB7.0.2.37/28/999",
    "Openwave/ UCWEB7.0.2.37/28/999",
    "Mozilla/4.0 (compatible; MSIE 6.0; ) Opera/UCWEB7.0.2.37/28/999",
    # iPhone 6：
	"Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25",
]

start = time.time()

host = 'http://data.eastmoney.com/hsgtcg/list.html?DateType=DateType=%27jd%27'
res = request.get(host)
xml = etree.HTML(res.text)
result = xml.xpath('/html/body/div[1]/div[8]/div[2]/div[2]/div[1]/div[1]/div/span/text()')[0]
today = result[1:11]
print(f'今天获取的数据是: {today}')

fname = str(today)+".xlsx"
fname1 = "PPOS_POTE_"+fname
fname2 = "PPOS_POTE_SZ_"+fname

file_path = '/home/lambda/Documents/jiatou'
if not os.path.exists(file_path):
    os.mkdir(file_path)
os.chdir(file_path)

if os.path.exists(fname):
    print('文件已存在，明天再来吧')
    sys.exit()

heads = {'HdDate', 'SCode', 'SName', 'NewPrice', 'ShareSZ_Chg_One',  'ShareSZ_Chg_Rate_One', 'LTZB_One', 'ZZB_One'}
rows = []

# 获取网页信息
async def fetch(session, url):
    headers = {'User-Agent': random.choice(user_agent)}
    async with session.get(url, headers=headers) as response:
        return await response.text(encoding='utf-8')
    
# 解析网页
async def parser(html):
    pat = re.compile('data:(.*)}', re.S) # 使用正则
    result = re.search(pat, html).group(1)
    data = json.loads(result)
    if len(data) == 0:
        print('日期有错误，看看是不是日期不对。。。。。。')
        sys.exit()
    for d in data:
        row = {key: value for key, value in d.items() if key in heads}
        rows.append(row)
    
# 下载网页
async def download(url):
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, url)
        await parser(html)

#urls = [f'http://dcfm.eastmoney.com/em_mutisvcexpandinterface/api/js/get?callback=jQuery112305322211230994847_1618827285261&st=ShareSZ_Chg_One&sr=-1&ps=50&p='+str(p)+'&type=HSGT20_GGTJ_SUM&token=894050c76af8597a853f5b408b759f5d&js=%7B%22data%22%3A(x)%2C%22pages%22%3A(tp)%2C%22font%22%3A(font)%7D&filter=(DateType%3D%27jd%27)(HdDate%3D%27'+str(today)+'%27)' for p in range(1, 31)]
urls = [f'http://dcfm.eastmoney.com/EM_MutiSvcExpandInterface/api/js/get?type=HSGT20_GGTJ_SUM&token=894050c76af8597a853f5b408b759f5d&st=ShareSZ_Chg_One&sr=-1&p='+str(p)+'&ps=50&js=var%20mXyeKPjW={pages:(tp),data:(x)}&filter=(DateType=%27jd%27%20and%20HdDate=%27'+str(today)+'%27)&rt=53931781' for p in range(1, 31)]

# 利用asyncio模块进行异步IO处理
async def main():
    await asyncio.gather(*[download(url) for url in urls])
               
asyncio.run(main())
# 将rows转化为pandas中的DataFrame
df = pd.DataFrame(rows)
df.columns = ['日期', '代码', '名称', '最新股价' , '市值', '市值增幅', '占流通股比', '占总股比']
# 从大到小排序
df.sort_values(by='市值', ascending=False)
try:
    df.to_excel(fname) # 保存成Excel文件
except Exception as e:
    print("请关闭文件后再试", e)

df1 = df.nlargest(20, '占总股比')
df2 = df.nlargest(20, "占流通股比")
df3 = df.nlargest(10, "市值")
# 占总股比前20和流通股比前20的交集
df1_df2 = pd.merge(df1, df2, on=list(df.columns), how='inner')
# 三者的交集
df1_df2_df3 = pd.merge(df1_df2, df3, on=list(df.columns), how='inner')
try:
    df1_df2.to_excel(fname1) 
except Exception as e:
    print("请关闭文件后再试", e)
   
try:
    df1_df2_df3.to_excel(fname2)
except Exception as e:
    print("请关闭文件后再试", e)

stop = time.time()
print(f"使用aiohttp共耗时{stop-start} S")