# -------- homework --------

# ------------1-------------
# נשתמש בטווח כשאנחנו רוצים להריץ את אותו הקוד מספר ידוע של פעמים

# ------------2-------------

# print(list(range(10, 100, 5)))
# range(start,end,skip)

# ------------3-------------
# all odd numbers between 90 -> 1  using range
# odds = list(range(89, 1, -2))
# print(odds)

# ------------4-------------

# name = input('please enter a name')
#
# while name != 'amir':
#     name = input('please enter a name')
#
# print('welcome sir')
#
# # --- do-while
# while True:
#     name = input('please enter a name')
#     if name == 'amir':
#         break

# ------------5-------------

# ---------8-------
# for i in range(200, 1, -1):
#     print(i)

# --------- 9 -------
# for i in range(1,100):
#     if i%7 == 0:
#         print(i)
#
# for i in range(0, 100, 7):
#     print(i)

# number = float(input('please enter a number :'))
# sum1 = 0
# while number >= 0:
#     sum1 += number
#     number = float(input('please enter a number :'))
#
# print(sum1)


# n = int(input('please enter a number '))
#
# factorial = 1
#
# for i in range(1, n + 1):
#     factorial *= i
# print(f'the factorial of {n} is {factorial}')

import math

print(math.factorial(5))