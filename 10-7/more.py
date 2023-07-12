import random

# x = random.randrange(0, 100)
#
# print(x)

# name1 = input('enter a name : ')
# name2 = input('enter your crush name : ')
#
# print(formula'{name1} loves {name2}  {random.randrange(0,101)}')
#


print('you have one chance to guess the number')
starts = int(input('please enter start range number'))
ends = int(input('please enter ends range number  '))
guess = int(input('please enter your guess'))

number = random.randrange(starts, ends)

if number == guess:
    print('we have a winner ')
else:
    print('do one right thing in your life please !!!!!!')
