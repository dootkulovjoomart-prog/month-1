'Задание №1'
# while True:
#     цвет = input("Введите цвет (Чтобы остановить:выход): ").lower().strip()
#     print(f'цвет сфетафора:{цвет}')
#     if цвет=='выход':
#         print('Программа остановлено')
#         break
#
#     if цвет == 'красный':
#         print('стоп')
#     elif цвет == 'зеленый':
#         print('иди')
#     elif цвет == 'желтый':
#         print("готовся")
#     else:
#         print("ошибка")


'Задание №2'
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
sany_1=[]

for day in days:
    sany=int(input(f'trata {day}:'))
    sany_1.append(sany)


summa= sum(sany_1)
sredny=summa//len(sany_1)
print('Obshaya trata:',summa)
print('srednya trata :',sredny)