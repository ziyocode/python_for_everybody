t = ['a', 'b', 'c']
x = t.pop(1)
print(t)
print(x)

t1 = ['a', 'b', 'c']
del t1[1]
print(t1)

t2 = ['a', 'b', 'c']
t2.remove('b')
print(t2)

t3 = ['a', 'b', 'c', 'd', 'e', 'f']
del t3[1:5]
print(t3)
