import requests

## -------- users ---------
# url = 'https://jsonplaceholder.typicode.com/users'
#
# res = requests.get(url)
#
# # data = res.json()
# #
# # print(data['name'])
# # print(data['address']['geo']['lat'])
#
# users = res.json() # list of dict
# print(users)
#
# print(f'you have {len(users)}')
#
# for user in users:
#     print(user['name'])

# ## this code used to retrieve data from /comments resource
#
# comment_url = 'https://jsonplaceholder.typicode.com/comments'
#
# response = requests.get(comment_url)
#
# comments = response.json()  # list of dict -> dict {comment }
#
# print(f'we have {len(comments)}')
#
# for comment in comments:
#     print(comment['email'])
