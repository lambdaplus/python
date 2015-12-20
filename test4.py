#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @Date    : 2015-12-03 14:31:20
# @Author  : yangyinshen
# @Email   : 278298125@qq.com
# @Link    : http://my.oschina.net/eddylinux
# @Version : 1.0
import re
import requests
url='http://tieba.baidu.com/p/2970106602'
html=requests.get(url)
detail =  html.content
r = 'BDE_Image" src=(.*?) pic_ext'
pict_list =  re.findall(r,detail,re.S)
j  = 1
for i in pict_list:
    i = i.replace('"','')
    response = requests.get(i,stream=True)
    image = response.content
    with open('%s.jpg' %j ,"wb") as jpg:
        jpg.write(image)
    j +=1
     
#<img class="BDE_Image" src="http://imgsrc.baidu.com/forum/w%3D580/sign=a97e769d9045d688a302b2ac94c37dab/36fb513d269759ee57eedf65b0fb43166c22dfe7.jpg" pic_ext="jpeg" pic_type="0" width="560" height="466"> 
#r = 'BDE_Image" src=(.*?) pic_ext'   
#"http://imgsrc.baidu.com/forum/w%3D580/sign=a97e769d9045d688a302b2ac94c37dab/36fb513d269759ee57eedf65b0fb43166c22dfe7.jpg"
