#  Write a Python program to convert temperatures to
#  and from Celsius and Fahrenheit.
#  c= 5/9 * (f -32)
#  f = 1.8 *c  + 32
# Expected Output :
# '60 C'    ->   140 in Fahrenheit
# '45 F'     ->  7 in Celsius


# t = input('enter the tmp in this format [number F/C]: ')
# t = t.split()
#
# if t[1] == 'F':
#     c = int(5 / 9 * (int(t[0]) - 32))
#     print(f'{t[0]}F is  {c}C ')
# elif t[1] == 'C':
#     f = 1.8 * int(t[0]) + 32
#     print(f'{t[0]}C is  {f}F ')

#  Write a Python program to count the
#  number of even and odd numbers in a series of numbers
# Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# Expected Output :
# Number of even numbers : 5
# Number of odd numbers : 4


# Write a Python program that prints all the numbers
# from 0 to 6 except 3 and 6.
# Note : Use 'continue' statement.
# Expected Output : 0 1 2 4 5


# Write a Python program to check the
# validity of passwords input by users.
# Validation :
# At least 4 letter
# At least 2 number
# Minimum length 6 characters.
# Maximum length 16 characters.
# if the user insert invalid pass ask him to insert another one
# exit when the password is valid


while True:
    password = input('please ente a number')
    letters = 0
    digits = 0
    for char in password:
        if char.isdigit():
            digits += 1
        elif char.isalpha():
            letters += 1
    if 6 <= len(password) <= 16 and digits > 2 and letters > 4:
        break

print(password)
