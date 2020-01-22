import requests
import random
import os
import time

tags = ['TIC-01','PIC-02','FIT-03']
server = 'http://'+os.environ.get('SERVER','localhost:5000')+'/write'

while True :
    values = {tag:random.random() for tag in tags}
    requests.post(server,json=values)
    print('.',end='',flush=True)
    time.sleep(1)