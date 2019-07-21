fhand = open(
    '/Users/ziyocode/Documents/workspaces/python/edwith_python/chapter07/mbox-short.txt')
count = 0
for line in fhand:
    line = line.rstrip()
    if line.startswith('From:'):
        print(line)
