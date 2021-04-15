#UTF-8

#把anti-AD的dsnmasq转换成MelinClash的hosts格式

import wget
from datetime import date
today = date.today()

def host_trans(url):
    file = wget.download(url, out='/home/lambda/Documents/adblock/anti_ad_'+str(today)+'.conf')
    with open(file, 'r') as f:
        new_f = open('/home/lambda/Documents/adblock/anti_ad_'+str(today)+'.yaml', 'w')
        new_f.write('hosts:\n')
        new_f.write('  router.asus.com: 192.168.50.1\n')
        new_f.write('  services.googleapis.cn: 74.125.193.94\n')
        for lines in f:
            if '#' not in lines and not lines == "\n":
                # 获取网址
                tail = lines[9:].strip()
                # tail[:-1] 去掉字符串尾部的 /
                new_lines = "  " + tail[:-1] + ": " + '127.0.0.1'
                new_f.write(new_lines+'\n')
            else:
                pass
        new_f.close()
    print("anti-ad.yaml文件保存在文档/adblock文件夹下")
    
if __name__ == '__main__':
    url = 'https://anti-ad.net/anti-ad-for-dnsmasq.conf'
    host_trans(url)