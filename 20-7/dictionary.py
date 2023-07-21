# name -> meaning
#
# key -> value
#
# 314151515 -> roni
#
# name -> nati
#
# # -------------------------------
# # | name  | id  |  grade | car  |
# # -------------------------------
# # | roni  | 11  |  100   | bmw  |
# # -------------------------------
# # |ibrahim| 17  |  99.0  | lambo|
# # -------------------------------
# # | nato  | 55  |  99.0  | mos  |
# # -------------------------------
#


# student_1 = {'id': 314774060,
#              'name': 'roni',
#              "job": 'QA eng',
#              'salary': 19000}
#
# print(student_1['name'])
# print(type(student_1['name']))
# print(student_1.values())
# print(student_1.keys())
# print(student_1)
# student_1['salary'] = 1
# student_1['favfood'] = 'coffee'
# print(student_1)
# print(student_1.get('married'))
# student_1.pop('salary')
# print(student_1)

# using this user
# print yes if the company name starts with R else print no
# user1 = {
#     "id": 1,
#     "name": "Leanne Graham",
#     "username": "Bret",
#     "email": "Sincere@april.biz",
#     "address": {
#         "street": "Kulas Light",
#         "suite": "Apt. 556",
#         "city": "Gwenborough",
#         "zipcode": "92998-3874",
#         "geo": {
#             "lat": "-37.3159",
#             "lng": "81.1496"
#         }
#     },
#     "phone": "1-770-736-8031 x56442",
#     "website": "hildegard.org",
#     "company": {
#         "name": "Romaguera-Crona",
#         "catchPhrase": "Multi-layered client-server neural-net",
#         "bs": "harness real-time e-markets"
#     }
# }
# print('yes' if user1['company']['name'].startswith('R') else'no')
# print(user1['name'])
# print(user1['address']['street'])
# print(user1['address']['geo']['lat'])


# movies = [
#     {'name': "deadpool", "release_year": 2020, "genre": "Action"},
#     {'name': "rush hour", "release_year": 2019, "genre": "Comedy"},
#     {'name': "jumanji", "release_year": 2022, "genre": "Drama"},
#     {'name': "fast f9", "release_year": 2018, "genre": "Science Fiction"},
#     {'name': "barbie", "release_year": 2021, "genre": "Thriller"},
#     {'name': "black panther", "release_year": 2017, "genre": "Adventure"},
#     {'name': "tokyo drift", "release_year": 2023, "genre": "Fantasy"},
#     {'name': "bad boys", "release_year": 2016, "genre": "Mystery"},
#     {'name': "adam project", "release_year": 2024, "genre": "Romance"},
#     {'name': "it", "release_year": 2015, "genre": "Sci-Fi"}
# ]
#
# for movie in movies:  # iterate the list
#     print(movie)
#     for k, v in movie.items():  # iterate the dict
#         if len(k) > 4:
#             print(f'the key is {k}, the value is {v}')
