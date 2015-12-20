# -*- coding: utf-8 -*-

import http.cookiejar
import urllib.request

# head: dict og hander
def makeMyOpener(head = {
	'Connection': 'Keep-Alive',
    'Accept': 'text/html,application/xhtml+xml,\
	application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) \
    AppleWebKit/537.36 (KHTML, like Gecko) \
    Chrome/47.0.2526.73 Safari/537.36'}):

	cj = http.cookiejar.CookieJar()
	opener = urllib.request.build_opener(urllib.\
		request.HTTPCookieProcessor(cj))
	header = []
	for key, value in head.items():
		elem = (key, value)
		header.append(elem)
	opener.addheaders = header
	return opener

oper = makeMyOpener()
uop = oper.open('http://www.baidu.com/', timeout = 1000)
data = uop.read().decode('utf-8')
print(data)
