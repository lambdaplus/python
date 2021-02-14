#!/usr/bin/env python
# coding: utf-8

# In[10]:


import re
import os
import json
import csv
import sys
import pandas as pd
import datetime
import time
import requests as request

headers = {'HdDate', 'SCode', 'SName', 'NewPrice', 'ShareSZ_Chg_One',  'ShareSZ_Chg_Rate_One', 'LTZB_One', 'ZZB_One'}

today = datetime.date.today()
fname = str(today)+".xlsx"
fname1 = "PPOS_POTE_"+fname
fname2 = "PPOS_POTE_SZ_"+fname

file_path = 'C:\\eastmoney'
if not os.path.exists(file_path):
    os.mkdir(file_path)
os.chdir(file_path)

def get_html(page):
    url = 'http://dcfm.eastmoney.com/EM_MutiSvcExpandInterface/api/js/get?type=HSGT20_GGTJ_SUM&token=894050c76af8597a853f5b408b759f5d&st=ShareSZ_Chg_One&sr=-1&p='+str(page)+'&ps=50&js=var%20Hyeikcqr={pages:(tp),data:(x)}&filter=(DateType=%27jd%27%20and%20HdDate=%272021-02-10%27)&rt=53772857'
    res = request.get(url).text
    pat = re.compile('data:(.*)}', re.S)
    result = re.search(pat, res).group(1)
    data = json.loads(result)
    return data

def get_one_page_stock(page):
    rows = []
    data = get_html(page)
    
    for a in data:
        row = {key: value for key, value in a.items() if key in headers}
        rows.append(row)
    return rows

def get_all_stock():
    all_rows = []
    for page in range(1, 31):
        print('\n正在下载第 %s 页表格' % page)
        rows = get_one_page_stock(page)
        all_rows.extend(rows)
    print("下载已完成。。。。。")
    return all_rows

def get_pd():
    
    all_rows = get_all_stock()
    df = pd.DataFrame(all_rows)
    df.columns = ['日期', '代码', '名称', '最新股价' , '市值', '市值增幅', '占流通股比', '占总股比']
    try:
        df.to_excel(r'C:\eastmoney\%s' % fname)
    except Exception as e:
        print("请关闭文件后再试", e)
    return df

def good(f):
    df1 = f.nlargest(20, '占总股比')
    df2 = f.nlargest(20, "占流通股比")
    df3 = f.nlargest(10, "市值")
    df1_df2 = pd.merge(df1, df2, on=list(f.columns), how='inner')
    df1_df2_df3 = pd.merge(df1_df2, df3, on=list(f.columns), how='inner')
    try:
        df1_df2.to_excel(r'C:\eastmoney\%s' % fname1)
    except Exception as e:
        print("请关闭文件后再试", e)
        
    try:
        df1_df2_df3.to_excel(r'C:\eastmoney\%s' % fname2)
    except Exception as e:
        print("请关闭文件后再试", e)

def main():
    start_time = time.time()
    if os.path.exists(fname):
        df = pd.read_excel(fname)
        good(df)
    else:
        df = get_pd()
        good(df)

    end_time = time.time() - start_time
    print('文件保存在C盘eastmoney文件夹下')
    print('程序耗时：{:.1f} s'.format(end_time))

main()

