#Функции:виды параметров, возвращение данных,виды аргумент.
#'из чего состоит функцмя '
#def
# def some_name(name,surname='ne ukazano'):
#     return {'name':name.title(),'surname':surname.title()}
# result1=some_name('chyngyz',surname='aitmatov')
# print(result1)
    #print(f'name:{name} surname: {surname}')
# some_name('zhoomart','dootkulov')
# some_name(name='aaly',surname='tokombaev')
# 'написать функцию'
# def some_nam(a:int= 0, b:int= 0 ):
#     if type(a) == int and type(b) == int:
#         return a + b
#     else:
#          return "Error"
# print(some_nam(56,45))
# print(some_nam('rwdfs','tfdgf'))
def get_square(length: int , width: int) -> int :
    """Длину и ширину умножаем и в результате получим площадь квадрата"""
    return length * width
print(get_square(34, 56))

print(get_square.__doc__)
