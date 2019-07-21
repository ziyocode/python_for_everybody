cheeses = ['cheddar', 'edam', 'Gouda']
numbers = [17, 123]

for cheese in cheeses:
    print(cheese)

# same
for i in range(len(cheeses)):
    print(cheeses[i])

for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2
print(numbers)
