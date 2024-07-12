""" 
Write a code to suggest automatically activates for 
https://api.ipify.org/?format=json 
Get your public IP Get your location
https://ipinfo.io/<YOUR_IP>/geo
"""

import requests
from pprint import pprint
url="https://api.ipify.org/?format=json"
response=requests.get(url)
data=response.json()
pprint(data)

ip_address=data['ip']
url2=f"https://ipinfo.io/{ip_address}/geo"
response2=requests.get(url2)
data2=response2.json()
pprint(data2)
