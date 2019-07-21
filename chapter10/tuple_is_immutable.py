t = ('a', 'b', 'c', 'd', 'e')  # tuple sameple
t1 = ('a',)
print(type(t1))  # tuple

t2 = ('a')
print(type(t2))

t3 = tuple()
print(type(t3))
print(t3)

t = tuple('apple')
print(t)

t4 = ('a', 'b', 'c', 'd', 'e')
print(t4[0])

t4 = ('A',) + t[1:]  # 각 항목을 변경할 수 없으나,
print(t4)
