import requests
import json

url = 'http://www.ip.cn/api/index?ip=&type=0'

req = requests.get(url=url)
rtl = json.loads(req.text)
# print(req.text)
print('IP:'+rtl['ip'])
print('City:'+rtl['address'])
os.system("pause")
