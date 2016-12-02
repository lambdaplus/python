# coding=utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import re
import csv
import requests
import jieba
import jieba.analyse
from bs4 import BeautifulSoup as bs
from tgrocery import Grocery
from train_txt_5 import train_src


def artical_content(url):
    rsp = requests.get(url)
    rsp.encoding = 'utf-8'
    html = bs(rsp.text, 'lxml')
    # artical = html.select('#sina_keyword_ad_area2')
    artical = html.select('.h1_tit')
    if len(artical) > 0:
        content = artical[0].text
    else:
        content = html.select('.SG_txta')[0].text
        # content = ''
    return content.strip()


def category(urls):
    for url in urls:
        artical = artical_content(url)
        cate2 = new_grocery.predict(artical)
        yield cate2.predicted_y


def unzip(seq, L=None):
    if L is None:
        L = []
    for s in seq:
        if not isinstance(s, (list, )):
            L.append(s)
        else:
            L.extend(unzip(s))
    return L


if __name__ == "__main__":

    grocery = Grocery('sample')
    grocery.train(train_src)
    grocery.save()
    new_grocery = Grocery('sample')
    new_grocery.load()

    L1 = []
    with open('/home/mouse/Downloads/female.csv', 'r') as f1:
        f1_csv = csv.reader(f1)
        for row in f1_csv:
            L1.append(row[0])
    # print(len(L1))

    cate = category(L1)
    i = 1
    with open('/home/mouse/infoss.csv', 'w') as f:
        f_csv = csv.writer(f)
        for row in zip(L1, cate):
            f_csv.writerow(unzip(row))
            print 'Writing now, please waiting...{}'.format(str(i))
            i += 1
    print 'Done'
