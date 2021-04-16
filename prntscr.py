import threading

import requests,json,os,sys,time,string,random
from fake_useragent import FakeUserAgent
from lxml import html
import urllib

def generator():
 url = 'https://prnt.sc/{0}'.format(''.join(random.choices(string.ascii_uppercase + string.digits, k=6))).lower()
 return url

def worker(i,papka,ua):
 try:
  url = generator()
  res = requests.get(url, headers={'User-Agent': ua.random}).text
  tree = html.fromstring(res)
  data = tree.xpath('//*[@id="screenshot-image"]/@src')
  p = requests.get(data[0], headers={'User-Agent': ua.random})
  out = open("{1}\\{0}.jpg".format(i, papka), "wb")
  out.write(p.content)
  out.close()
  print('# Thread №{0} Complete.'.format(i))
 except Exception:
  print('No image.')
  print('# Thread №{0} Complete.'.format(i))
 time.sleep(1)

def main(count):
 ua = FakeUserAgent()
 papka = time.time()
 os.mkdir('./{0}'.format(papka))
 for i in range(0,int(count)):
  if threading.activeCount() < 15:
   threading.Thread(target=worker, args=(i,papka,ua)).start()
  else:
   while threading.activeCount() > 15:
    pass
   threading.Thread(target=worker, args=(i,papka,ua)).start()


if __name__ == '__main__':
 main(input('Сколько скриншотов загружаем?: '))