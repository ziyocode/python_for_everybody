fhand = open(
    '/Users/ziyocode/Documents/workspaces/python/edwith_python/chapter07/mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if line.find('@uct.ac.za') == -1:
        continue
    print(line)
