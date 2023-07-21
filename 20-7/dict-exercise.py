# d1 = {'a': 155}
# d2 = {'b': 188}

# concatenating dict's
# d2= {'b': 188,'a':155}

# for k,v in d1.items():
#     d2[k]=v
# print(d2)
# d3 = {}
# d3.update(d1)  # adds one dict item to aniother
# d3.update(d2)
# print(d2)

# כתבו קוד בפייתון שמדפיס את כמות המפתחות ב dict נתןן
# dict1 = {'a': 2, 'b': 3, 'c': 4, 'd': 5, 'e': 6, 'f': 7}
# expected results : this dict contain 6 keys
#
# print(len(dict1.keys()))


# תאר את המחשב שלך בעזרת מילון תאר את : צבע גודל מחיר וגובה

# table={'color':'white',
#        'size':'M',
#        'price': 140,
#        'height':1.1}


# Write a Python program to combine two
# dictionary by adding values for common keys.
# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'c':400,'d':600}
# Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})

# d3={}
# for k1,v1 in d1.items():
#     if k1 not in d2.keys():
#         d3[k1]=v1
#     for k2,v2 in d2.items():
#         if k1 == k2:
#             d3[k1] = v1+v2
#         if k2 not in d1.keys():
#             d3[k2]=v2
#
#
# print(d3)
#gnaipnga