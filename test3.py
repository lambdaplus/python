# -*- coding:utf-8 -*-
import requests, re

def get_img(url):
    img_html = requests.get(url)
    detail = img_html.content.decode('utf-8')
    r = re.compile('<img pic_type="0" class="BDE_Image" src="(.*?)"')
    img_url_list = r.findall(detail)
    i = 1
    for img_url in img_url_list:
        img = requests.get(img_url)._content
        with open('/home/mouse/pictures/%i.jpg' % i, 'wb') as f:
            f.write(img)
            print('Downloading... the %d picture' % i)
        i += 1

if __name__ == '__main__':
    get_img('http://tieba.baidu.com/p/2166231880')
