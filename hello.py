#!/usr/bin/python

import json
import requests
import random
import time
while True:
        temperature=random.randint(90,120)
        print("temperature is "+str(temperature))
        url = "https://dweet.io:443/dweet/for/iotmanager-temperature-sensor-1"
        data = {'deviceId': 'Device-001', 'name': 'MasterRoom', 'temperature': temperature}
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        r = requests.post(url, data=json.dumps(data), headers=headers)
        time.sleep(5)
