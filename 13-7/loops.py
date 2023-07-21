#


# range(start,stop,step)
#
# range(0,10,1)  0-9
# range(10)  0-9
# range(0,20-7,2) 0,2,4,6,8,10,12,14,16,18


# # ====== DRY =======
#
# print('hello')
# print('hello')
# print('hello')
# print('hello')
# print('hello')
# print('hello')
# print('hello')
# print('hello')
# print('hello')
# print('hello')

# for i in range(1,11):
#     print(f'{i} hello')

#
# x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
# for number in range(20-7):
#     print(number)
# for n in x:
#     print(n)
#

# words = ['desk', 'ss', 'pen', 'oooop shel halyooon', 'mazda', 'cupra']
#
# for word in words:
#     if len(word) > 3:
#         print(word.upper())
#     else:
#         print(word.lower())


#

# 1
#
# numbers = []
#
# for n in range(7):
#     numbers.append(int(input('please enter a number : ')))
#
# print(numbers)
# print(f' the max number is {max(numbers)} ')
# print(f' the sum is {sum(numbers)} ')
# print(f' the avg is {sum(numbers)/len(numbers)} ')

# 2

# l1 = [-22, 14, 555, 616, -99, -414, 156, 0.266]
#
# print(l1)
#
# # for number in l1:
# #     if number > 0:
# #         print(number)
# #
#
# for number in l1:
#     if number % 7 == 0:
#         print(number)

# user_input = int(input('please enter a number : '))
#
# for i in range(user_input):
#     print('hello')

# words = ['hello', 'my ', 'Name', 'is', 'not', 'NTal', 'or', 'roni']
#
# for word in words:
#     if 'n' in word.lower():
#         print(word)


# for x in range(5):  # [0,1,2,3,4]
#     if x == 3:
#         break
#     print(x)
#
# print('out of the for')


# valid password is an password of 8 char len and starts with hi

# passwords = ['hight1234', 'hi1234', '123456hi', 'helliii', 'kawabanga', 'hiiiiiiiiiii']
#
# for password in passwords:
#     if len(password) < 8 or not password.startswith('hi'):
#         break
#     print(f'{password} valid password')


# name = 'roni fishelevitz'
#
# # print(name.lower())  # lower letter
# # print(name.upper())  # capital letter
# # print(name.startswith('ro'))  # return true if the string starts with the given str
# # print(name.endswith('itz'))  # return true if the string ends with the given str
# # print(name.replace('i', 'v'))  # replace all the given string with a new ones
# # print( name.count('i') )
# # print( name.find('i') ) # the first index of the given str
# # print(name.rfind('i'))
# #
# # print(name.rstrip()) # delete all the post spaces
# # print(name.strip())  # delete all spaces  the before and after the word
# # print(name.lstrip()) # delete all the pre spaces
# #
# # print(len(name.strip()))
# print(name)
# l1 = name.split(' ')
# print(l1)
# l1= ' '.join(l1[::-1])
# print(l1)

# # given the following list
# ws = ['121', 'tot', 'deed' , 'yoomaay', 'choco']
# # print all the words that's starts and ends with the same char
#
# for w in ws:
#     if w[0] == w[-1]:
#         print(w)


# Write a Python program to remove duplicates from a list.

list1 = [1, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 2, 21, 1, 1, 2, 24, 4, 451, 651, 26, 16, 16, 1, 6]

new_list = []

for n in list1:
    if n in new_list:
        continue
    new_list.append(n)

print(new_list)

# print(list1)
# list1 = set(list1)
# # list1 = list(list1)
# print(list1)
