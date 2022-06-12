# https://ubntwiki.com/products/software/unifi-controller/api
import sys
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

mac_address = sys.argv[1]
controller = '192.168.1.1:443'
username = sys.argv[2]
password = sys.argv[3]
ip_address = ''

with requests.sessions.Session() as session:
    session.headers = {"Accept": "application/json" ,"Content-Type": "application/json"}
    session.verify = False

    response = session.post(f'https://{controller}/api/auth/login', json={'username': username, 'password': password})
    response.raise_for_status()

    response = session.get(f"https://{controller}/proxy/network/api/s/default/stat/sta")
    response.raise_for_status()

    clients = response.json()


for client in clients['data']:
    if client['mac'] == mac_address:
        ip_address = client['ip']
        break

if ip_address:
    print(ip_address)
else:
    raise Exception(f'Was not able to find a host with mac address {mac_address}')

1.216796875