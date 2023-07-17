# DRY - dont repeat yourself

# [] () {} range
# for var_name in iterable:
# the code


# --------- 3 ------------
#          0  1  2  3   4
# numbers = [1, 5, 7, 8, 100]

# sol 1
# middle = len(numbers)//2
#
# for i in range(middle):
#     print(numbers[i])

# sol 2
# for n in numbers[:len(numbers)//2]:
#     print(n)


# --------- 4 ------------

# words = ['pen', 'python', 'potatoes', 'barbe', 'booom' , 'doors']
#
# for word in words:
#     print(word.upper())

# --------- 5 ------------
# words = ['python', 'potatoes', 'barbe', 'booom', 'pen', 'doors']
#
# for word in words:
#     if len(word) < 4:
#         break
#     print(word.upper())

# --------- 6 ------------

# name = 'Tal Markovich'
#
# # a
# print(name[-5:])
# # b
# print(name[:len(name) // 3])
#
# # print(name[len(name) // 3:2 * len(name) // 3])  #the second 1/3
# # print(name[-len(name)//3:])
#
# #c
# print(f'the letter a appeared {name.count("a")}  times')
#
# #d
# print('b' in name)
#
# #e
# name_list = name.split()
# print(name_list)
#
# #f
# name_list.reverse()
# # name_list = name_list[::-1]
# print(name_list)
#
# #g
# name_list[0] = name_list[0].upper()
# print(name_list)
#
# #h
# first = name_list[1]
# mid = len(first)//2
# name_list[1] = first[:mid] + first[mid+1:]
# print(name_list)
#
# # print(first)
# #
# # print(first.replace(first[mid],''))
#
# # j
# name =' '.join(name_list)
#
# print(name)


# ----------7----------
# text = 'Hello world!'
#
# print(f"index of the first o in the sentence {text.find('o')} and the last o in {text.rfind('o')}")
# print(text[:text.find('o')+1])
# print(text[text.find('o'):])

# for i in range(len(text)):
#     if text[i] == 'o':
#         print(i)

# -----------8----------
# t = 'hello world'

# print(t.replace('o', ''))

# # ------------ 9 ----------
# numbers = [8, 1000, -3, 2, 5]
# # print(sum(numbers))
# # print(max(numbers))
# # print(min(numbers))
# # print(sum(numbers) / len(numbers))
# # numbers.pop(len(numbers)//2)
# # print(numbers)
# # numbers.sort()
# # print(numbers)
# # for i in range(5):
# #     print(numbers)
# #
# # numbers.pop(0)
# # print(numbers)
#
# avg = sum(numbers)/len(numbers)
#
# # new_list=[]
# #
# # for n in numbers:
# #     if n < avg:
# #         new_list.append(n)
#
# #list name = [append  for append in old list if true ]
# new_list = [n for n in numbers if n < avg]
# print(new_list)

# -------- 10 --------

# numbers = [1, 5, 7, 8, 1000]
# max = numbers[0]
# for n in numbers:
#     if n > max:
#         max = n
# print(max)


matrix = [
    [12, 87, 5, ],
    [-1, 3000, 4, ],
    [200, 8, 4, ]]

min = matrix[0][0]
for row in matrix:
    for n in row:
        if n < min:
            min = n

print(min)
