# api testing
# pip install requests

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
# log = open(f'{datetime.datetime.now().strftime("%Y-%m-%d")}.txt', 'a+')# add a new file with a name of the date of today
# url = input('please ente a site to check :')
# url = 'https://'+url
#
# time = datetime.datetime.now().strftime('%H:%M:%S')
# res = requests.get(url)
#
# log.write(f'{time}  {url} method : GET {res.status_code}\n')
