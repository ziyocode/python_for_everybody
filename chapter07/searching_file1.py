fhand = open(
    '/Users/ziyocode/Documents/workspaces/python/edwith_python/chapter07/mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From:'):
        continue
    print(line)
