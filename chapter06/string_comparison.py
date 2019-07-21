InputWord = input("put in the your word: ", )

if InputWord < 'banana':
    print('Your word, ' + InputWord + ', comes before banana.')
elif InputWord > 'banana':
    print('Your word, ' + InputWord + ', comes after banana.')
else:
    print('All right, bananas.')
