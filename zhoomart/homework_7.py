#1 zadacha
def blizhaishee_chislo(numbers:[312 , 996, 31, 1991],target:1000):
    sorted_numbers = sorted(numbers, key=lambda x: abs(x - target))

    return target , sorted_numbers
print(blizhaishee_chislo([312 , 996, 31, 1991] , 1000))

#2 zadacha
names=['zhoomart','bekbol' , 'siymyk' , 'atay']
names_map = list(map(lambda word: f'handsome {word} kg' , names))
print(names_map)

names_map =list(filter(lambda word: word[0]=="z" , names))
print(names_map)

# 3 zadacha

def get_element(iterable=[1, 2, 3, 4, 5]):
    print("Итерируемый объект:", iterable)
    print(f"Допустимые индексы: от 0 до {len(iterable) - 1}")
    print("Для выхода введите -1")

    while True:
        try:
            index = int(input("Введите индекс элемента (или -1 для выхода): "))

            if index == -1:
                print("Выход из программы.")
                break

            print("Элемент:", iterable[index])

        except IndexError:
            print(f"Ошибка: Индекс вне диапазона. Доступные индексы: 0 до {len(iterable) - 1}.")

        except ValueError:
            print("Ошибка: Пожалуйста, введите корректное число.")











