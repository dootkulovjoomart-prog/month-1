

slovar_1={
    'q': 'й', 'w': 'ц', 'e': 'у', 'r': 'к', 't': 'е', 'y': 'н', 'u': 'г', 'i': 'ш', 'o': 'щ', 'p': 'з',
    'a': 'ф', 's': 'ы', 'd': 'в', 'f': 'а', 'g': 'п', 'h': 'р', 'j': 'о', 'k': 'л', 'l': 'д',
    'z': 'я', 'x': 'ч', 'c': 'с', 'v': 'м', 'b': 'и', 'n': 'т', 'm': 'ь',\


    'й': 'q', 'ц': 'w', 'у': 'e', 'к': 'r', 'е': 't', 'н': 'y', 'г': 'u', 'ш': 'i', 'щ': 'o', 'з': 'p',
    'ф': 'a', 'ы': 's', 'в': 'd', 'а': 'f', 'п': 'g', 'р': 'h', 'о': 'j', 'л': 'k', 'д': 'l',
    'я': 'z', 'ч': 'x', 'с': 'c', 'м': 'v', 'и': 'b', 'т': 'n', 'ь': 'm'
}
while True:
    slovo=input('enter your slovo(ctoby vyti exit):')
    if slovo.lower()=='exit':
        print('stop')
        break

    slovo = slovo.lower()
    converted=''.join(slovar_1.get(char, char) for char in  slovo)
    print('slovo obratnom',converted)

# def bally(test,homework):
#     if 75<= test  <= 100 and 65<= homework <= 80:
#         return 'Skidka 3000'
#     elif 55 <= test <= 74 and 65<= homework <=80:
#         return 'Skidka 2500(+8 poseshenie)'
#     elif 75 <= test <=74 and 65<= homework <=80:
#         return 'Skidka 2000'
#     elif 75 <= test <=100 and 45<=homework <=64:
#         return 'Skidka 2000'
#     elif 55 <= test <= 74 and 45<= homework <=64:
#         return 'Skidka 1000'
#     else:
#         return 'Skidka zhok'
# test=int(input('skoka test:'))
# homework=int(input('skoka homework :'))
# print(bally(test,homework))

