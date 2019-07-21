s = 'spam'
t = list(s)
print(t)

s = 'pining for the fjords'
t = s.split()
print(t)

s1 = 'spam-spam-spam'
delimiter = '-'
s1.split(delimiter)
print(s1)

t1 = ['pining', 'for', 'the', 'fjords']
delimiter1 = '-'
delimiter1.join(t1)
print(t1)
