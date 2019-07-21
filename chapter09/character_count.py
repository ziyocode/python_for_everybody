word = 'brontosaurus'
d = dict()
for c in word:
    if c not in d:
        d[c] = 1
    else:
        d[c] = d[c] + 1
print(d)

# user th get method
word1 = 'brontosaurus'
d1 = dict()
for c1 in word1:
    d1[c1] = d1.get(c1, 0) + 1
print(d1)


counts = {'chuck': 1, 'annie': 42, 'jan': 100}
print(counts.get('chuck', 0))
print(counts.get('jan', 0))
