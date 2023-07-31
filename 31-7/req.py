# api testing
# pip install requests

import time
import requests
import datetime

## copy the content of the html pages
# response = requests.get('https://google.com/')
#
# print(response.status_code)
# sc = response.status_code
# if 200 <= sc < 400:
#     print('passed')
#     file = open('google.html', 'w+')
#     file.write(response.text)
#
# else:
#     print('failed')

# # ------- log file to http request module --------
# log = open(f'{datetime.datetime.now().strftime("%Y-%m-%d")}.txt', 'a+')  # add a new file with a name of the date of today
# url = input('please ente a site to check :')
# url = 'https://'+url
#
# time = datetime.datetime.now().strftime('%H:%M:%S')
# res = requests.get(url)
#
# log.write(f'{time}  {url} method : GET {res.status_code}\n')

# ------- ---------
url = 'https://' + input('enter your url')
start_time = time.time()  # start counting
res = requests.get(url)
end_time = time.time()  # stop counting

print(end_time - start_time)
