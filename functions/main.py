#Функции
#Это именнованные блоки с кодом которые служат для выполнения конкретной задачи
#Обьеденении код функцию вам больше не придеться перепечатывать код, вы можете многократно вызывать функцию в нужном месте
#Использование функций упрощает как написание и чтение кода так и тестирование и исправление ошибок


"Обычный пример областей видимостей задачи"
# x = 10
# def fun():
#     return x ** 2
# sum = fun()
# print(sum)



#Функция начинаеться с ключевого слово
# def  - define - Определять


# say_hello()  Ошибка вызывания функций при Глобальной области видимости

# def say_hello(user_name, age):
#     """Функция приветствия пользователя"""
#     print(f"Hello friend:       {user_name} ")
#     print(f"Youre age  {age}")
#     print('-' * 40)
#     return user_name, age
# say_hello('emka', 16)
# say_hello('Nikita', 25)
# say_hello('Akbar', 16)
# say_hello('Kutman', 17)
# say_hello('Amir', 17)


# если мы уже Добавили в Функцию параметр то должны мы и его его вызвать через Аргумент
# Именнованный Аргумент представляет собой {Аргумент-ИМЯ}
# Первыми в функции идут параметры без значения  (Обязательные параметры)
# def number_sum(user_name , num1 = 1, num2 = 2):
#     num1 += 1
#     num2 += 1
#     print(f"Имя {user_name}")
#     print(num1 + num2)
#     print('__' * 20)


# number_sum(user_name='olgan', num1=2, num2=7)

# number_sum(user_name='emka', num1=7, num2=7)

# number_sum(user_name='Nikita-', num1=16, num2=7)


# def number_sum(user_name , age=0):
#     if user_name >= 30:
#         print("Welcome To Gus")
#     else:
#         print("Fuck")
#     return user_name, age
# res = number_sum(1, 2) # Главное имя Функцию можно обернуть в переменные и вызывать через:::::
# print(res)          # Переменные

















                                        # *args, **kwargs:
#**args и **kwargs — это специальные параметры в Python функциях,
#которые позволяют передавать переменное количество аргументов в функцию.

# *(одна звездочка в Python называеться Распоковкой как в примерее)
# my_list = [1, 2, 3, 4, 5]
# print(*my_list) # 1, 2, 3, 4, 5 - в Этот раз произошла распоковка list стал распокаванным


#*args:
#Это параметр функции, который используется для передачи
#  переменного количества позиционных аргументов.




#*args - Состоит из Tuple() - Кортежа()
#**kwargs - Состоит из dict{} - Словаря{}

# def crate_plate(color, *args, **kwargs):
#     print(f"Цвет:       {color}")
#     print(f"Характеристика:     {args}")
#     for values in kwargs:
#         print(F"Имя  {kwargs.keys()}")
    
# crate_plate('grenn',  n='Круглой',  c='Овальной', cp='С Узором')

# def my_function(ny, n1, n2, n3, *args):
#     return args

# res = my_function(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# print(res)






                            #lamda - Мини функции

# lambda - Это мини функции которые пишуться в одну строку кода и которые нужны для маленьких задач

# lambda арг1,арг2,...: Выражение

# my_lambda_2 = lambda x: x ** 2
# print(my_lambda_2(10))
#Простой приме с Возведение в степень lambda



"1)"
# def perimetr(a, b, c):
#     return a + b + c
# res = perimetr(10, 20, 30)
# print(res)
# Пример с Функцией def 


"2)"
# per = lambda a, b, c: a+b+c
# print(per(10, 5, 20))
#Пример с функцией lambda

"()"
# h = lambda : 'hello'
# print(h())

#Можно ли вы lambda указывать циклы напиши одним словом
# Да, это называется "map".


"Способ решения функция и lambda"
"1)"
# def f(x):
#     if x >= 10:
#         return "positive"
#     else:
#         return 'negative'
# res = f(0)
# print(res)
"2)"
# res1 = lambda x: 'positive' if x >= 0 else 'negative'
# print(res1(1))


#ИСполбзование Lambda



# a = [21, 2, 124, 77000, 12, 20000000, 211]
# a.sort(key=lambda x: x //   10)
# print(a)

# def linear(k, b):
#     return lambda x: x * k+b
# gread =linear(2, 5)

# print(gread(3))


"============================= <Области Видимости python> =================================="

#Если создать переменную внутри функции ана называеться Локальной области видимости
#если Создать переменную вне функции в (другом месте) то ана называеться Глобальной Областью видимости
#ChatGPT

# В Python область видимости определяет, где и как можно
# использовать переменные в программе. Существуют четыре основных типа областей видимости функций:


# def s():
#     "local"
#     a, b, c = 1, 2, 3
#     print(a, b, c, 'local')
    
# "Global"
# a = [1, 2, 3, 4, 5]
# b = 12
# c = 10
# s()
# print(a, b, c,  "Global")
#s() - Эта функция s(была создана в Глобальной области видимости)
# nonlocal - Меняет Глобальную возвращая к локальному




# Область видимости замыкания (Enclosing scope):

#     Вложенные функции имеют доступ к переменным в области видимости их внешней функции.
#     Эта область видимости называется областью видимости замыкания (enclosing scope).
#     Переменные в этой области видимости доступны как для внутренней функции, так и для внешней.






# """============================== <Вcтроенные функции python> ========================================"""


# # map, filter, reduce, zip, enumerate

# #zip - Соединяет несколько посследовательностей (получаем генератор, в котором элемменты tuple)



# # list1 = [1, 2, 3, 4, 5]
# # list2 = ['a', 'b', 'c', 'd', 'e']
# # res = dict(zip(list1, list2))
# # print(res)




# # list1 = [1, 2, 3, 4, 5]
# # list2 = ['a', 'b', 'c', 'd', 'e']
# # dict_1 = dict(zip(list1, list2))
# # print(dict_1)



# "=============================  enumerate ==========================="
# #enumerate - нумеруует посследовательности (по дефолту с 0) (также получаем генератор)
# # enumerated = enumerate("hello")
# # print(enumerated)


# hello = 'hello world'
# enumerated = dict(enumerate(hello))
# print(enumerated[0])


# # for el in enumerated:
# #     print(el)

# string = 'hello world'
# print(list(enumerate(string[5:])))

"================================= <map >======================================"
# map - принимает функцию и посследовательность (записывает в новую посследовательность)
#результат функции, в которую передаються элемменты посслдеовательности)

# list1 = [
# '1', '2', '3', '4', '5'
# ]
# mapped = list(map(int, list1))
# print(mapped)


# my_list = [
# 1, 2, 3, 4, 5
# ]
# mapped = list(map(float, my_list))
# print(mapped)



# string = 'hello world'

# mapped = ''.join(map(lambda x: x.upper(), string))
# # print(mapped)


# my_list = [1, 2, 3, 4, 5]
# mapped = list(map(lambda x: x ** 2, my_list))
# list1 = mapped
# list2 = list1
# print(list1)
# print(list2)
# list_ = [1, 2, 3, 4, 5]
# list_2 = list(map(lambda x: x**2, list_))
# list_3 = list_2
# print(list_2)
# print(list_3)


# def my_fn(x):
#     return x ** 2
# res = list(map(my_fn, my_list))
# print(res)

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


# my_list01 = [1, 2, 3, -3, 0, -21]
# my_lum = list(filter(lambda x: x > 0, my_list01))
# print(my_lum)

# users = [
# {'name':'nikita', 'age':12,
#   'name ':'nastya', 'age':20, 
#  'name': 'artem', 'age':19}
# ]
# Оставить пользователей которые старше 18
# res = list(filter(lambda users: users['age'] > 18, users
# ))
# print(res)


# my_list = [1, 2, 3, 4, 5, 6, 7,-213, -231, -213]
# my_list_2 = list(filter(lambda x:x >= -1, my_list))
# print(my_list_2)
# result = list(map(lambda x: x['name']))


"======================== <reduce> =========================="

from functools import reduce

# reduce - Надо сначала Импортировать import потом вызывать 
# # reduce - принимает функцию и посследовательность, возвращает 1 результат 
# #(передаваемая функция должна принимать 2 аргумента)
# list_01 = [1, 2, 3, 4, 5]
# res = reduce(lambda x, y: x * y, list_01)
# print(res)

# list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# res = reduce(lambda x, y: x*  y, list_1)
# print(res)


# string = 'hello'
# res = reduce(lambda x, y: x + '$' + y, string)
# print(res)

string = 'hello world'
my_num = reduce(lambda x, y:x + '       $      ' + y, string)
print(my_num)


# # x = 'h', y = 'e' -> h$e
# # x = 'h$e', y = 'l' -> h$e$l
# string_1 = 'hello world'
# print(reduce(lambda x, y: string_1.replace(x, y), string_1)) # heddo wordd


# list_10 = [1, 4, 2, 5, 3, 6, 0, 123, 51, 21421, 124, 512]
# #Выведите самое маленькое число с помощью reduce
# res_1 = reduce(lambda x, y,: x if x <y else y, list_10)
# print(res_1)

list_10 = [1, 4, 2, 5, 3, 6, 0, 123, 51, 21421, 124, 512]
res = reduce(lambda x, y:x if x  <y else y, list_10)
print(res)


# users = [
# {
# 'name ':'nastya', 'age':20, 
# 'name': 'artem', 'age':19,
# 'name':'nikita', 'age':12,}
# ]
#Выведите самого младшого пользователя с помощью reduce


users = [
{
'name ':'nastya', 'age':5, 
'name': 'artem', 'age':19,
'name':'nikita', 'age':12,}
]

number = reduce(lambda x, y: x if x['age'] > y['age'] else y, users)
print(number)




# def min_dict(dict1, dict2):
#     if dict1['age'] < dict2['age']:
#         return dict1    
#     return dict2
# res = reduce(min_dict, users)
# print(res)

#Решение через lambda

# result = reduce(lambda x, y: x  if x['age'] < y['age'] else y, users)
# print(result)




