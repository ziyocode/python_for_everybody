fhand = open(
    '/Users/ziyocode/Documents/workspaces/python/edwith_python/chapter07/mbox-short.txt')
#fhand = open('./mbox-short.txt')
count = 0
for line in fhand:
    count = count + 1
print('Line Count:', count)

fhand = open(
    '/Users/ziyocode/Documents/workspaces/python/edwith_python/chapter07/mbox-short.txt')
inp = fhand.read()
print(len(inp))
