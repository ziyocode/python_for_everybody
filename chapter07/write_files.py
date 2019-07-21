fout = open('chapter07/output.txt', 'a')
line1 = "This here's the wattle, \n"
fout.write(line1)
fout.close()

fout = open('chapter07/output.txt', 'r')
for line in fout:
    print(line)
fout.close()
