#!/usr/bin/python3
# coding=utf-8

import logging
import re
import aiohttp
import asyncio
from bs4 import BeautifulSoup
from pymongo import MongoClient


class DouBanCrawl():

    def __init__(self, url):
        self.url = url

    async def fetch(self, url, headers):
        res = await aiohttp.request('GET', url)
        body = res.read()
        return (await body)

    def infos_get(self, html, name=None):
        soup = BeautifulSoup(html, 'lxml')
        scores = soup.select('.rating_num')
        scores = [score.text for score in scores]
        quotes = soup.select('p.quote > span')
        quotes = [quote.text for quote in quotes]
        pattern = r"https://movie.douban.com/subject/\w+/"
        hrefs = re.findall(pattern, str(html))[::2]
        title_list = soup.select('div.pic > a')
        try:
            titles = [re.findall(r'alt="(.*?)"', str(title))[0]
                      for title in title_list]
            img_links = [re.findall(r'src="(.*?)"', str(src))[0]
                         for src in title_list]
        except IndexError:
            pass
        return img_links, titles, scores, quotes, hrefs

    async def save_info(self, page):
        url = self.url.format(page)
        # print(url)
        with await sem:
            html = await self.fetch(url, headers)
        img_links, titles, scores, quotes, hrefs = self.infos_get(html)
        for infos in zip(img_links, titles, scores, quotes, hrefs):
            info = {'img': infos[0],
                    'name': infos[1],
                    'score': infos[2],
                    'quote': infos[3],
                    'href': infos[4]
                    }
            count = coll.find({"name": infos[1]}).count()
            if count == 0:
                coll.insert(info)


if __name__ == '__main__':
    url = 'https://movie.douban.com/top250?start={}&filter='
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
                (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}
    client = MongoClient('localhost', 27017)
    db = client.movies
    coll = db.coll
    douban = DouBanCrawl(url)
    pages = range(0, 250, 25)
    sem = asyncio.Semaphore(4)  # 限制协程并发量
    loop = asyncio.get_event_loop()
    f = asyncio.wait([douban.save_info(page) for page in pages])
    loop.run_until_complete(f)  # %time 为Ipython 自带功能模块
    print('Done')
