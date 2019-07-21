stuff = 'Hello World'
print(type(stuff))
print(dir(stuff))


word = 'banana'
newWord = word.upper()
print(newWord)

index = word.find('a')
print(index)
print(word.find('na'))
print(word.find('na', 3))

# remove white space
line = '   Here we go  '
print(line.strip())

# startswith()
line01 = 'Have a nice day'
print(line01.startswith('Have'))
