# -*- coding: utf-8 -*-

import requests, re, os

def get_pictures(url):
	html_content = requests.get(url, stream=True)
	print(html_content)
	r = re.compile('<img pic_type="0" class="BDE_Image" src="(.*?)"')
#	picture_url_list = r.findall(html_content)#.decode('utf-8'))

	for i in range(len(picture_url_list)):
		picture_name = str(i) + '.jpg'
		req = requests.get[picture_url_list]
		return req.content

if __name__ == '__main__':
	get_pictures('http://tieba.baidu.com/p/2166231880?see_lz=1')
			

