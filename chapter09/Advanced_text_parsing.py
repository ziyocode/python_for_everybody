import string

fname = input('Enter the file name : ')
try:
    fhand = open(fname)
except:
    print('File not Found : ', fname)
    exit()

counts = dict()
for line in fhand:
    line = line.rstrip()
    line = line.translate(line.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

print(counts)
