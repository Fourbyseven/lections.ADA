"==================================== <Типы Данных> ======================================="
# Immutable - неизменяемые типы данных (int, float, str, None, Bool, tuple, frozenset)
# Muttable  - Изменяемые (list, set, dict)

"====================================== <numbers> ========================================="
# Числа это неизменяемые тип данных для хх==ранения числовых значений и проведения над ними арифметических действий
int     #Целые числа
float   # Тоже числа с плавающей точкой
#decimal Десятичные более точные
complex # Комплеексные числа
#long   Огромные числа
# print(dir(int()))
# У Int - тоже есть методы

# Строки -  неизменяемый тип данных  который представляет собой упорядочный тип данных 
# Который представляет собой символов, заключенных в одинарные и двойными кавычками

# str_ = 'emka'
# str_2 = 'hello'


"====================================== <Ииндексы> ==================================="
# string = 'hello world'
# string[1]
# string[-1]
# string[::-1]
# string[0:5]

# list_1 = ['hello', True, None, False, 34, [{'a':1, 'b':[213]}]]
# print(list_1[-1])


"================================ <list> ======================================"
# Список  - изменяемый, итерируемый, упорядоченный, тип данных который хранит в себе посследовательность 
# элемментов 

# list_1 = [1, 2, 3, 4, 5, 6, True, None, False]


"=============================== Tuple =================================="
#Кортеж - неизменяемый список, хранит в себе посследовательность элемментов

tuple_1 =  1, 2, 3, 4, 5 # (1, 2, 3, 4, 5)
tuple_2 = (1) # int
tuple_1 = (1,) #tuple
tuple1 = 1, #tuple


"=============================== < Set > ================================="
# Множество - изменяемый, неупорядоченный тип данных который хранит в себе только уникальные значения

# set_1 = {1, 2, 3, 4, 5, 4, 4, 4, 4, 4} # {1, 2, 3, 4, 5}
# print(set_1)
# Для set едница == True, 0 == False

# set_2 = {1, 0, True, False}
set_3 = {} # dict
set_4 = set() #set

"=================================== <Frozenset> ================================"
# Неизменяемыое множество
# f_set = frozenset([1, 2, 3, 4, 5, 6, 7, 8]) #{{1, 2, 4, 5, 7, 8}}
# # Все методы, которые были у set для изменения, во frozenset отсутствуют
# print(dir(f_set))


"==================================== < Словарь > ======================================"
# Dictionary  - Словарь - Изменяемый неупорядоченный тип данных, 
# для хранения данных в паре:       ключ:значения
# Ключ:  должен быть неизменяемым типом данных
# Если ключом будет tuple - то в нем тоже должны быть только неизменяемые типы данных
# Если ключ повторяеться то значение перезаписываеться на посследнее

# dict1 = {'a':1, 'b':5, 'a':3} # {'a':3, 'b':5}


"==================================== <Bolean> ===================================="
# Логический тип данных, с двумя значениями (True, False)

"==================================== < None > ======================================="
# None  - тип данных, для обозначения пустоты


"=============================== < Условные операторы > =============================="
# Условные - конструкция, которая позволяет выполнять или не выполнять какойто кусочек 
#        в теле который находиться в теле условия

# if True:
#     pass
# elif None:
#     pass
# else:
#     pass


"======================================== <Тернарный оператор > =================================="
# тернарный оператор - Условие написанное в одну строку кода, и возвращает одну из двух
# результатов в зависимости от условия
# my = 'res' if True else 'res2'
# print(my)




"========================================== < Циклы в Python> ===================================="
# Цикл - Конструкция которая позволяет циклично пройтись по итерируемому  обьекту(str, list, set, dict, tuple, range)
# В цикле for мы выполняем операции над каждым элемментам итерируемого обьекта 
# Итерация - одно прохождения цикла  
# Итерируемый обьект - по которому можно пройтись циклом For
# break - прерывает работу цикла
# continue - пропускает 1 (одну итерацию)


# list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for elem in list_1:
#     if elem % 2 ==0:
#         print(elem)

"=========================================== <While> =========================================="
# цикл - который повторяет код пока условие Истинно  True (может быть бесконечным)

# n = 10
# while n < 100:
#     print(n)
#     n += 1


"========================================= < Функции > ============================================"

# employees = [
#     {"name": "Alice", "salary": 3000, "overTime": 10},
#     {"name": "Bob", "salary": 2500, "overTime": 5},
#     {"name": "Charlie", "salary": 4000, "overTime": 0}
# ]

# def func(employees: dict) -> dict:
#     result = []
#     BONUS = 200
#     for employee in employees:
#         modfied_salary = employees['salary']  + employee['overTime'] * BONUS
#         employee.update({'salary': modfied_salary})
#         employee.pop('overTime')
#         result.append(employee)
#     return result
# print(func(employees))

# list_1 = [1, 2, 3, 4, 5, 6, 8, 9, 10, 'hello', 'world', 'my', 'is', 'nikita']
# def func2(ints_and_strs: list):
#     int_1 = []
#     str_1 = []
#     for i in ints_and_strs:
#         if type(i) == int:
#             int_1.append(i)
#         if type(i) == str:
#             str_1.append(i)
#     return int_1, str_1



# int_1, str_1 = func2(list_1)
# print(int_1)
# print(str_1)





# my_list = [5, 6, 8, 9, 10, 'hello', 'world', 'my', 'is', 'nikita']
# def func2(ints_and_strs: list):
#     int_1 = []
#     str_1 = []
#     for i in ints_and_strs:
#         if type(i) == int:
#             int_1.append(i)
#         if type(i) == str:
#             str_1.append(i)
#     return int_1, str_1



# int_1, str_1 = func2(list_1)
# print(int_1)
# print(str_1)



# products = [
#     {"title": "Apple Juice", "price": 2.5},
#     {"title": "Orange Juice", "price": 3.0},
#     {"title": "Grape Juice", "price": 4.0},
# ]
# def func3(products: list, title: str):
#     filterred_data  = [product for product in products if title.lower() in  product.get('title').lower() ]
#     return filterred_data
# print(func3(products, 'Apple juice'))








# my_list = ['hello', 'world', 'name']



# my_jpin = '|        '.join(my_list)
# print(my_jpin)



# my_list = list(range(1, 30))
# print(my_list)



# my_dict = {'emka': 'umetov', 1:'1'}
# my_dict.setdefault('umetov', 20)
# print(my_dict)








my_tuple = (['emka'], ['hello'])
print(my_tuple[0].append('hello'))
print(my_tuple)

































































































































































































































































































































































































