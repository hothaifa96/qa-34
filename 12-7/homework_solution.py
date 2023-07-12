# 1- input - wait to the user input
# returns str datatype value

# 2-
# x = int(input('please enter int'))
# x = float(input('please enter float'))

# 3- split() is str function that's separate the string to a list of
# the sentence words we can override the seperator using ('separate value')

# sen = 'i need coffee'  ['i','need','coffee']
#
# print(sen.split())

# # 4-
# print(formula'{11} {4-4} {4224}')

# 5-
# print('M' in 'mac')


# if condition:
#     trueblock
# elif condition2:
#     truelock
# else:
#     flaseblock


# 7-
# if 1 == 1:
#     print(1)
# print(1)

# 8-

# number1 = float(input('please enter a number : '))
# number2 = float(input('please enter a number : '))
#
# # ------------1-----------------
# print(formula'{number1 if number1 > number2 else number2}')
# # ------------2-----------------
# if number2 > number1:
#     print(number2)
# else:
#     print(number1)
# # ------------3-----------------
# print(max(number1, number2))
#
# #---------------test --------------
# # big  small    5  1
# # small big     1  5    DT -- 2^1 = 2
# #   equals      2  2

# # 9-
# x = float(input('enter a number :'))
# y = float(input('enter a number :'))
# z = float(input('enter a number :'))
# print(max(x, y, z))
# #---------------test --------------
# #  3^3 = 27
# #  big mid small
# #  big small mid
# #  big equals equals
# #  small big mid
# #  small mid big
# #  small equals equals
# #  mid big small
# #  mid small big
# #  mid equals equals
# #  equals big equals
# #  equals equals big
# #  equals equals equals
# #  equals equals small
#

# 10-


formula = input('please enter thr formula :')
formula = formula.split()
if formula[1] == '+':
    print(int(formula[0]) + int(formula[2]) == int(formula[4]))
elif formula[1] == '-':
    print(int(formula[0]) - int(formula[2]) == int(formula[4]))
elif formula[1] == '*':
    print(int(formula[0]) * int(formula[2]) == int(formula[4]))
elif formula[1] == '//':
    print(int(formula[0]) // int(formula[2]) == int(formula[4]))
