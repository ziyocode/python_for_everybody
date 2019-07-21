import string
d = {'a': 10, 'b': 1, 'c': 22}

lst = list()
for key, val in d.items():
    lst.append((val, key))
    print(lst)

lst.sort(reverse=True)
print(lst)
