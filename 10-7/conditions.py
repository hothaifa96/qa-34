# a = 6
# b = 8

# print(a == b)  # False eq || = =
# print(a != b)  # True  nq || ! =
# print(a > b) # False  gt  || >
# print(a < b) # True  lt   || <
# print(a <= b) # True ge   || > =
# print(a >= b) # False le  || < =

# ____________________________________
# |condition1|add|condition2| result |
# ------------------------------------
# |    True  |and|   False  |  False |
# ------------------------------------
# |    False |and|   True   | False  |
# ------------------------------------
# |   False  |and|  False   | False  |
# ------------------------------------
# |   True   |and| True     | True   |
# ------------------------------------
# |condition1|or|condition2| result |
# ------------------------------------
# |    True  |or|   False  |  True  |
# ------------------------------------
# |    False |or|   True   | True   |
# ------------------------------------
# |   False  |or|  False   | False  |
# ------------------------------------
# |   True   |or| True     | True   |
# ------------------------------------


# print(a == b or b > a)
# print(a > 10 or b > 2 and a + b > 0)
# print(b > 2 or (a > 10 and a + b > 0))

# age = 100

# if age >= 18:
#     # True Block
#     print('welcome')
# else:
#     #flase block
#     print('come back in a few years')
#
# print('thanx for using hodi application')

# if comparison exp :
#     # true block
# else:
#     # false block


# e1 - write a pyhon code to check if person is eligible to vote
# eligible voting age 16

# age = int(input('enter your age : '))
#
# if age >= 16:
#     print('you can vote ! ! ! ! ')
# else:
#     print('you can wait a few years !!!!!')

# e2 - write a python program to check whether a number is odd or even %

# number = int(input('enter a number : '))

# if number % 2 == 0 :
#     print( f'{number} is even')
# else:
#     print(f'{number} is odd')

# if number%7 ==0:
#     print(f'we can divide {number} by 7')


# day = int(input('please enter a number'))
#
# day = day % 7
# 8  -> 1
# 9  -> 2
# 10 -> 3
# 11 -> 4
# 12 -> 5
# 13 -> 6
# 14 -> 0


#
# if day == 1:
#     print('rishon')
# elif day == 2:
#     print('monday')
# elif day == 3:
#     print('shlishi')
# elif day == 4:
#     print('wednesday')
# elif day == 5:
#     print('hamishi')
# elif day == 6:
#     print('friday')
# else:
#     print('shabat')


# a = int(input('please enter a number : '))  # 15
# b = int(input('please enter a number : '))  # 77
# c = int(input('please enter a number : '))  # 199
#
# if b < a > c:
#     print(a)
# elif b > c:
#     print(b)
# else:
#     print(c)


# e3 - write a python program to print the new price of the items
# if the items cost between 100 and 500 print the price with 30% discount
# else print the price with 20% discount

# price = float(input('enter the total price of your items: '))
# #
# # if 100 < price < 500:
# #     print(price*0.70)
# # else:
# #     print(price*0.8)
#
# # true block  if condition else false block
#
# print(price * 0.7 if 100 < price < 500 else 0.8)
