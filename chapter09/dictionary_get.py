counts = dict()
names = ['jane', 'tom', 'jhon', 'tom']

for name in names:
    counts[name] = counts.get(name, 0) + 1

print(counts)
