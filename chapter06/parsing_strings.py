data = 'From stephen.marquard@uct.ac.za Sat jan 5'

atposition = data.find('@')
print(atposition)

spaceposition = data.find(' ', atposition)
print(spaceposition)

host = data[atposition+1:spaceposition]
print(host)
