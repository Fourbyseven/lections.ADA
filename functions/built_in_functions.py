"===================================== <Встроенные функции> ====================================="
# map, filter, reduce, zip, enumerate
#reduce - Надо обязательно Импортировать

#zip - Соединяет несколько посследовательностей (получаем генератор, в котором элемменты tuple)


# list1 = [1, 2, 3, 4, 5]
# list2 = ['a', 'b', 'c']
# list3 = [10.5, 20.6, 100.6]


# zipped = zip(list1, list2, list3)
# for el in zipped:
#     print(el)


# list1 = [1, 2, 3, 4, 5]
# list2 = ['a', 'b', 'c', 'd', 'e']
# dict_1 = dict(zip(list1, list2))
# print(dict_1)



"=============================  enumerate ==========================="
#enumerate - нумеруует посследовательности (по дефолту с 0) (также получаем генератор)
# enumerated = enumerate("hello")
# print(enumerated)

# for el in enumerated:
#     print(el)

# string = 'hello world'
# print(list(enumerate(string[5:])))

"================================= <map >======================================"
# map - принимает функцию и посследовательность (записывает в новую посследовательность)
#результат функции, в которую передаються элемменты посслдеовательности)

my_dict = frozenset([1, 2, 3, 4, 5])
print(my_dict)
# list1 = [
# '1', '2', '3', '4', '5'
# ]
# mapped = list(map(int, list1))
# print(mapped)

# string = 'hello world'
# res = ''.join(map(lambda x: x.upper(), string))
# print(res)

# list_ = [1, 2, 3, 4, 5]
# list_2 = list(map(lambda x: x**2, list_))
# list_3 = list_2
# print(list_2)
# print(list_3)

# list_ = [1, 2, 3, 4, 5]
# def to_2_degree(x):
#     return x ** 2
# print(list(map(to_2_degree, list_)))


# Lambda Функцию удобнее при легких ЗАДАЧ
# Def функция удобнее при больших ЗАДАЧ



"====================================== <Filter> ================================="
#filter - Возврашает генератор с элемментами прошедшими Фильтр(какое-то условие)
#Принимает в себя функции. и посследовательность
# list_1 = [1, 0, -2, -3, -4, 5, 10]
# filterred = list(filter(lambda x:x > 0, list_1))
# print(filterred)
# В этом случае filter фильтрирует и выводит только те числа которые больше (0)


# users = [
# {'name':'nikita', 'age':12,
#   'name ':'nastya', 'age':20, 
#  'name': 'artem', 'age':19}
# ]
# Оставить пользователей которые старше 18
# res = list(filter(lambda users: users['age'] > 18, users
# ))
# print(res)

"""
Вывести только имена пользователей которые младше 15
"""
# result = list(map(lambda x: x['name']))


"======================== <reduce> =========================="

from functools import reduce
# # reduce - принимает функцию и посследовательность, возвращает 1 результат 
# #(передаваемая функция должна принимать 2 аргумента)
# list_01 = [1, 2, 3, 4, 5]
# res = reduce(lambda x, y: x *y, list_01)
# print(res)


# string = 'hello'
# res = reduce(lambda x, y: x + '$' + y, string)
# print(res)

# # x = 'h', y = 'e' -> h$e
# # x = 'h$e', y = 'l' -> h$e$l
# string_1 = 'hello world'
# print(reduce(lambda x, y: string_1.replace(x, y), string_1)) # heddo wordd


# list_10 = [1, 4, 2, 5, 3, 6, 0, 123, 51, 21421, 124, 512]
# #Выведите самое маленькое число с помощью reduce
# res_1 = reduce(lambda x, y,: x if x <y else y, list_10)
# print(res_1)



users = [
{
'name ':'nastya', 'age':20, 
'name': 'artem', 'age':19,
'name':'nikita', 'age':12,}
]
#Выведите самого младшого пользователя с помощью reduce

# def min_dict(dict1, dict2):
#     if dict1['age'] < dict2['age']:
#         return dict1    
#     return dict2
# res = reduce(min_dict, users)
# print(res)

#Решение через lambda

# result = reduce(lambda x, y: x  if x['age'] < y['age'] else y, users)
# print(result)





a = ['1', '2', '3']
a = list(map(int, a))
print(a)


