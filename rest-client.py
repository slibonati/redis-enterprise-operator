#!/usr/bin/python

import ssl
import urllib3
import json

cert_reqs = ssl.CERT_NONE
urllib3.disable_warnings()

http = urllib3.PoolManager(cert_reqs = cert_reqs)

payload = {'name': 'John Doe'}
encoded_data = json.dumps(payload).encode('utf-8')

resp = http.request(
     'POST',
     'https://httpbin.org/post',
     body=encoded_data,
     headers={'Content-Type': 'application/json'})

data = json.loads(resp.data.decode('utf-8'))['json']
print(data)