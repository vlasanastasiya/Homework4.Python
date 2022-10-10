# Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
from random import randint 

def new_list_1(k, a, b):
    return [randint(a, b) for i in range(k + 1)]

def polynomial(inlist):
    polinomial_list = []
    for i in range(len(inlist)):
        if inlist[-1 - i] !=0:
            polinomial_list.insert(0, str(inlist[-1 -i]) + "*x^" + str(i))
    polystr = " + ".join(polinomial_list)
    polystr += " = 0 "
    polystr = polystr.replace(" 1* ", " ")
    polystr = polystr.replace("^1", "")
    polystr = polystr.replace("x^0", "1")
    polystr = polystr.replace("*1", "")
    if polystr[0] == "1" and polystr[1] == "*":
        b = 2
        polystr = polystr[b:]
    return(polystr)


k = int(input('Введите степень: '))
a = int(input('Введите границу числа'))
b = int(input('Введите вторую границу числа'))
inlist = new_list_1(k, a, b)
polynomial_list = polynomial(inlist)

print(inlist)
print(polynomial(inlist))

with open('file1.txt', 'a') as data:
    data.write(polynomial(inlist))
