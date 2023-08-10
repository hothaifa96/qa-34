# 1
# number = 4  # int
# mp = 12 * 12  # int
# f = 2.4  # float
# word = 'hello'  # str
import random

# 2
# name = 'Donald Trump'
# print(len(name))
# name = name.upper()
# print(name)
# name = name.lower()
# print(name)
# print(f'the first lt is {name[0]}')
# print(f'a appears {name.count("a")} times')

# 3
# print(f'my name is {name}')
# print('my name is '+name)

# # 4
# a = float(input('please enter a number : '))
# b = float(input('please enter a number : '))
#
# print(f'{a} + {b} = {a+b}')

# 5
# user_input = int(input('enter a number : '))
# print('odd' if user_input % 2 else 'even')

# 6
# numbers = list(range(1,6))
# print(numbers)
# numbers.append(6)
# print(numbers)

# 7
# movies = ['avatar 2', 'it', 'night school', 'johny english', 'ted', 'iron man']
#
# for movie in movies:
#     if 'avatar' in movie:
#         print('i love avatar')

# import random
#
# random_numbers = []
#
# for i in range(10):
#     random_numbers.append(random.randrange(-100000, 100000))
# print(random_numbers)
#
# for number in random_numbers:
#     if number >= 0:
#         print(f'{number} positive')
#     else:
#         print(f'{number} negative')

# 9
# while True:
#     word = input('please enter a word')
#     if word == 'exit':
#         break
#     print(word)

# 10
# sum = 0
# while True:
#     x = int(input('enter a number'))
#     if x == -1:
#         break
#     sum += x
#
# print(sum)


# 11

# for i in range(1, 101):
#     print(i)

# 12
#
# for i in range(0, 51, 3):
#     print(i)
#
# for i in range(51):
#     if i %3 != 0:
#         print(i)

# 13

# bigi = list(range(1,501))
#
# print(bigi)

# 14

# guess = random.randrange(0, 11)
# print('very good' if guess == int(input('enter your guess')) else 'Wrong')

# 15

def doublit(n=0):
    return n*2


print(doublit())