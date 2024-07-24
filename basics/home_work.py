# 1) Домашнее задание про тип type - нахождения типа:
a = 10
b = int("120")
print(type(a))
print(type(b))

# 2) Домашнее задание про функцию len: 
a_1 = [1, 2, 3, 4, 5]
b_1 = 'Heloo worlds'
print(len(a_1))
print(len(b_1))

# 3) Домашнее задание про функццию id:
a_2 = 1
b_2 = [1, 2, 3, 4, 5]
print(id(a_1))
print(id(b_2))

#4) Binary - bin
Forbs = int("213213")
print(bin(Forbs))

Forbs_2 = 12
print(bin(Forbs_2))


# 5)abs отрицательное и положительное

a_3 = -21
b_3 = -123
c_3 = -213
print(abs(a_3))
print(abs(b_3))
print(abs(c_3))

#round - Окруление float:
a_4 = 12.12
b_4 = 14.12
c_4 = 1.5
print(round(a_4))
print(round(b_4))
print(round(c_4))

#sqrt - нахождения квадратного корня числа
from math import sqrt
print(sqrt(25))
print(sqrt(12))
print(sqrt(122))
print(sqrt(59))

#pow - Возведение в степень
print(pow(123, 11))
print(pow(1,4))

#divmod - Фунция которая возвращает 2 числа, где 1 число - целая часть от деления 2 число осттаток от деления
print(divmod(8, 4)) # (2, 2)
print(divmod(5, 2)) # (2, 1)
print(divmod(17, 3))# (5, 2)


#input - Введение в терминал: 
number_1 = float(input("Введите первое число:       "))
number_2 = float(input("Введите второе число:       "))
res = number_1 + number_2
print(f"Сумма  двух (2) вывода равна:       {res}")















