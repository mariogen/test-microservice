import requests
import pprint
import os
import time

tags = ['TIC-01','PIC-02','XXX']
server = 'http://'+os.environ.get('SERVER','localhost:5000')+'/read'

while True :
    values = requests.post(server,json=tags).json()
    pprint.pprint(values)
    time.sleep(1)