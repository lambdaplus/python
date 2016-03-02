# -*- coding: utf-8 -*-
import sys

import json

import requests

def get_weather(loaction):

    response = requests.get(url)
    data = response.json()
    keys = ['week', 'days', 'weather', 'temperature', 'winp']

    print('>>>未来%s七天天气如下<<<\n' %weather[0]['citynm'])
    for day in range(len(weather)):
        for key in keys:
            print(weather[day][key])
        print('---------------')

if __name__ == '__main__ True:
    while True:
        loaction = input('请输入你想要查询的城市名称，例如：北京或beijing\n>>>')
        if loaction == 'q':
            sys.exit()
        else:
            url = 'http://api.k780.com:88/?app=weather.future&weaid=%s&&\
                    appkey=17976&sign=c6ed32baf5cdf23c19ba2883838ae09e&format=json' %loaction
            get_weather(url)
            print('提示：输入q结束查询')
