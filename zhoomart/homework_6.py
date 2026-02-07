# первая функция
def parol(надежный_пароль):
    digits = 0
    upper = 0
    lower = 0
    special = 0

    symbols=  "!@#$%^&*?/"
    for parol_1 in надежный_пароль:
        if parol_1.isdigit():
            digits += 1
        elif parol_1.isupper():
            upper += 1
        elif parol_1.islower():
            lower +=1
        elif parol_1 in symbols:
            special += 1

    if len( надежный_пароль) >= 6 and digits >=1 and upper>=1 and lower>=1 and special >=2 :
        return True
    else:
        return False


надежный_пароль=input('Введите пароль:')

if parol(надежный_пароль):
    print("Пароль надежный ")
else:
    print("Пароль ненадежный ")



# вторая функция

def Ближайшее_Число(числа,целевое_число=0):
    Близкое = числа[0]

    for чис in числа:
        if abs(чис - целевое_число) < abs(Близкое - целевое_число):
            Близкое=чис

    return Близкое

print(Ближайшее_Число([1,2,3],5))
print(Ближайшее_Число([0.5,1.5,2.5],5))
