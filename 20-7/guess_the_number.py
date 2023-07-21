print('welcome to my game !!!!!')

import random

# numbers = []
# for i in range(5):
#     numbers.append(random.randrange(2, 50))

# ---------- 12 ---------- without challenges
# numbers = [random.randrange(2, 50) for x in range(5)]
#
# print(numbers)
#
# while numbers:
#     guess = int(input('please enter your guess : '))
#     if guess in numbers:
#         print('boooom')
#         numbers.remove(guess)
#     else:
#         print('hard luck')
#
# print('we have a winner ')


numbers = []
guesses = []
for i in range(5):
    x = random.randrange(2, 50)
    if x not in numbers:
        numbers.append(x) # to fill the numbers list

c = 0
while numbers:
    print(numbers)
    if c >= 20: # refill the list
        numbers.clear()
        for i in range(5):
            x = random.randrange(2, 50)
            if x not in numbers:
                numbers.append(x)
        c = 0
    guess = int(input('please enter your guess : '))
    c += 1
    if 2 > guess > 49:  # guess range
        continue
    if guess in guesses:  # without duplicates
        break
    if guess in numbers:
        print('boooom')
        numbers.remove(guess)
        guesses.append(guess)
    else:
        print('hard luck')

if len(guesses) == 5:
    print(f'we have a winner, you tried {c} numbers ')
else:
    print('hard luck')