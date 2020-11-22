import requests
import json

url = 'http://ifconfig.me'

req = requests.post(url=url)

rtl = json.loads(req.text)
print('IP:'+rtl['ip'])
print('City:'+rtl['city'])
print('Country:'+rtl['country'])
print('Location:'+rtl['loc'])
print('Org:'+rtl['org'])
print('TimeZone:'+rtl['timezone'])
# print(req.text)
os.system("pause")
