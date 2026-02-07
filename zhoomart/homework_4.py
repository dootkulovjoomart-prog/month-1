data_tuple = ('h', 6.13, 'c', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')
letters = []
numbers=[]
for spisok in data_tuple:
    if type (spisok)==str:
        letters.append(spisok)
    else:
        numbers.append(spisok)
numbers.remove(6.13)

numbers.insert(1,2)
numbers.sort()
numbers.remove(True)
letters.append(True)
letters.reverse()
numbers=[i**2 for i in numbers]
letters=['G' if i =='g' else i for i in letters]
letters=['C' if i =='c' else i for i in letters]
print(letters)
print(numbers)

