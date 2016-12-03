
# coding: utf-8

# In[30]:

import re
import concurrent.futures
import requests
from bs4 import BeautifulSoup as bs
from pymongo import MongoClient


def fetch(url):
    res = requests.get(url)
    res.encoding = 'gbk'
    content = bs(res.text, 'lxml')
    return content

def base_info(html):
    pattern = re.compile(r'http://blog.sina.com.cn/s/blog_.*\.html')
    links = re.findall(pattern, str(html))
    date_ = re.findall(r'\((\d{2,}.*)\)', str(html))
    tle_auth = html.select('li')
    authes = (auth.text.split(' ')[0] for auth in tle_auth)
    titles = (title.text.split(' ')[-1] for title in tle_auth)
    for infos in zip(links, titles, authes, date_):
        yield infos
        
def save(url):
    html = fetch(url)
    data = base_info(html)
    for num, d in enumerate(data, 1):
        datum = {
            'links': d[0],
            'title': d[1],
            'auther': d[2],
            'date': d[3]
        }
        count = coll.find({'links': d[0]}).count()
        if count == 0:
            coll.insert_one(datum)
        print('crawl the page of {}'.format(num))
        
        
def main():
    client = MongoClient('localhost', 27017)
    db = client.infos
    coll = db.coll
    pages = range(start, end+1)
    urls = [url.format(page) for page in pages]
    with concurrent.futures.ProcessPoolExecutor(max_workers=6) as executor:
        executor.map(save, urls)
    
if __name__ == '__main__':
    url = 'http://roll.blog.sina.com.cn/list/other/index_{}.shtml'
    start = int(input('请输入开始页数, 默认为1 >> '))
    if not start:
        start = 1
        
    end = int(input('输入结束页数， 默认为100 >> '))
    if not end:
        end = 100
        
    main()


# In[ ]:



