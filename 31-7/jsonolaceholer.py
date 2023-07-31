import requests

url = 'https://jsonplaceholder.typicode.com/users'

res = requests.get(url)

# data = res.json()
#
# print(data['name'])
# print(data['address']['geo']['lat'])

users = res.json() # list of dict
print(users)

print(f'you have {len(users)}')

for user in users:
    print(user['name'])