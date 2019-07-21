t1 = [1, 2]
t2 = t1.append(3)
print("t1 : {}".format(t1))
print("t2 : {}".format(t2))

# function // delete head


def tail(t):
    return t[1:]


letters = ['a', 'b', 'c', 'd']
rest = tail(letters)
print(rest)
