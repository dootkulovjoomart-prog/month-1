#списки,кортежи.Индексы и срезы.
#встроенные функции к наборам элементов
#списковые включение List comprehesion
#
# 'Индексы'
# numbers=[1,2,3,4,5]
# print(numbers)
# 'Индексы'
# print(numbers[0])
# print(numbers[3])
# print(numbers[-1])
# print(numbers[-2])
#
# 'Срезы [start:stop:step]'
# print(numbers[1:4:1])
# print(numbers[0:])
# print(numbers[-2:])
# print(numbers[::-1])
# 'добавление'
# numbers.append(6) #добавление
# numbers.insert(3,3.5)
# numbers.extend([7,8,9])
# print(numbers)
#
# 'изменение'
# numbers.sort()
# numbers.reverse()
# numbers[0]=63
# numbers[-2]=numbers[-1]
# print(numbers)
#
# 'Удаление'
# numbers.pop(0)
# del numbers [1:3]
# print(numbers)
# numbers.remove(3.5)
# numbers.clear()t
# print(numbers)
#
# name="zhoomart"
# print(name[-3:])
# "Встроенные фуекции к набором элементов"
# print(len(numbers))
# print(min(numbers))
# print(max(numbers))
# print(sum(numbers))

# Список_городов=['Лондон','Бишкек','Гамбург','Рим','Вашинктон']
# print(len(Список_городов))
# Список_городов.sort()
# print(Список_городов[0][0])
#
#
# for города in Список_городов:
#     print(города)
# cities = ['tokmok', 'bishkek', 'karakol', 'kemin' ,'balykchy','abudabi']
# print(cities)
# cities_new=[city.title() for city in cities if city[0]=='b']
# print(cities_new)
#data=[]
# while True:
#    time = input("Enter time: ").lower()
#    if time == "stop":
#        break
#
#    if time in ("morning", "utro"):
#        print("Good morning")
#    elif time in ("afternoon", "den"):
#        print("Good afternoon")
#    elif time in ("evening", "vecher"):
#        print("Good evening")
#    else:
#        print("Hello")
#    data.append(time)
#    print(data)


