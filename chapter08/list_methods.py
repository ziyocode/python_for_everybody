t = ['a', 'b', 'c']
t.append('d')
print(t)

t1 = ['a', 'b', 'c']
t2 = ['d', 'e']
print("extend: ", end=" ")
t1.extend(t2)
print(t1)


t = ['d', 'c', 'e', 'b', 'a']
t.sort()
print(t)


# append 는 뒤에 한 요소로 추가 ex > 뒤에 리스트를 넣으면 [...] 포함
# extend 는 [] 포함 없이 추가
