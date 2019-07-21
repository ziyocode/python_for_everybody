nums = [3, 41, 12, 9, 74, 15]

print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))
print(sum(nums)/len(nums))

numlist = list()
while (True):
    inp = input('Enter a number: ')
    try:
        if inp == 'done':
            break
        value = float(inp)
        numlist.append(value)
    except ValueError:
        print('{}는 숫자가 아닙니다.'.format(inp))
average = sum(numlist)/len(numlist)
print("Average : ", average)
