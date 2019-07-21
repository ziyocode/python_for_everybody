m = ['have', 'fun']
print(type(m))
x, y = m
print(x)
print(y)

x = m[0]
y = m[1]
print(type(x))
print(x)
print(type(y))
print(y)

a = 3
b = 4

# swap
a, b = b, a
print(a)
print(b)

addr = 'monty@python.org'
name, domain = addr.split('@')

print(name)
print(domain)
