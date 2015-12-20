
# coding: utf-8

# In[52]:

import requests
from bs4 import BeautifulSoup
data = []
headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36'}

res = requests.get('http://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&wq=%E6%89%8B%E6%9C%BA&pvid=sl23r3ii.7xmm81', headers = headers)
soup = BeautifulSoup(res.text)
for item in soup.select('.gl-i-wrap'):
    data = item.select('strong')[0].text, item.select('em')[1].text, item.select('.p-commit')[0].text


# In[ ]:



