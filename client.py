import requests
import os
import time


pid = os.getpid()
print(f"pid - {pid}")

# r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
r = requests.get('http://127.0.0.1:5000')
print(r.status_code)
print(r.headers['content-type'])
print(r.encoding)
print(r.text)
# r.json()



time.sleep(3000)