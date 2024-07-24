"============================ <Функции> ================================"
# Функция - это именнованный блок кода который может принимать аргументы и возврашать результат

# def my_sum(x, y):
#     return x + y

# res = my_sum(4, 5)
# print(res)


# def my_len(obj):
#     count = 0
#     for element in obj:
#         count += 1
#     return count
# res = my_len(['hello', 1, 2, 3, 4, True, False, [1, 2, 3]])
# print(len(['hello', 1, 2, 3, 4, True, False, [1, 2, 3]]))
# print(res)

# a = ['hello', 1, 2, 3, 4, True, False, [1, 2, 3]]
# count = 0
# for elemment in a:
#     count += 1
# print(count)


#Функции - Функции в Python — это один из основных инструментов для создания удобного и структурированного кода.
#  Они позволяют группировать набор инструкций, которые 
# выполняют определенную задачу, и использовать их многократно для программе.


"""
DRY - (dont repeat yourself - НЕ ПОВТОРЯТЬСЯ !), функции соблюдаеют этот принцип 

"""


"============================== <Аргументы и параметры> ==============================="
# Параметры это перемменые внутри функции значение которым  мы задаем при определении функциии

#Аргументы это переменные которые мы передаем при вызове функции

# def my_len(obj, num=10, *args):   # obj - параметры
#     count = 0
#     for element in obj:
#         count += 1
#     return count
# res = my_len(['hello', 1, 2, 3, 4, True, False, [1, 2, 3]])  # - Аргументы


"=============================== <Виды Параметров> ================================"

# 1) Обязательный параметр
# 2) Не обязательные
# 2.1) c Дефолтным значением 
# 2.2) *args (все позиционные аргументы, которые не попали в обязательные, и с дефолтным значением )
# 2.3) **kwargs (Все лишние именнованные агрументы)
"""                                 Виды аргументов                                         """
# 1) Позиционные (по позиции)
# 2) Именнованные (по названию (параметр - значение))


# Работа с Функцией  Анотация

# def add_or_add(num1:int, num2=10) -> int:
#     """
#     Складывает 2 числа
#     Если второе не передать, сложит первое с 10
#     """
#     return num1 + num2
# number = 5
# print(add_or_add(5))



"============================================ <*> ========================================"

# list1 = list(range(1,11))
# list2 = [*range(1, 11)]
# print(list1)
# print(list2)


# *:* (2 - Звездочки для  dict)

# dict1 =  {'a':1, 'b':2, 'c':3}
# dict2 = {**dict1}
# list1 = {*dict1}

# print(dict1)    #{'a': 1, 'b': 2, 'c': 3}
# print(dict2)    # {'a': 1, 'b': 2, 'c': 3}
# print(list1)    #{'c', 'b', 'a'}




# def func(a, b=10, *args, **kwargs):
#     print('a -', a)
#     print('b -', b)
#     print('args -', args)
#     print('kwargs -', kwargs)



# func(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, emaeuraaaaaaa=30, v=20, k=100)




# func(a=123213213, b=123213)


# *args - принимает Кортеж tuple
# **kwargs - принимает dict - dictionary






"======================== <lambda> ==========================="
# Это анонимная функция которая записываеться в одну строку
#Лямбда-функции – это анонимные функции, которые могут включать только одно выражение.
#Они обычно используются для выполнения простых операций, не требующих полного определения функции 
#с помощью ключевого слова def . Лямбда-функции могут принимать любое количество аргументов,
#но могут возвращать только одно значение.


# lambda_func = lambda x: x**10
# print(lambda_func(10))


"===================== <Калькулятор с помощью lambda> ==============================="

#Полноценный Калькулятор через функцию Lambda

# calc = {
#     '+':lambda n1, n2: n1 + n2,
#     '-':lambda n1, n2: n1 - n2,
#     '*':lambda n1, n2: n1 * n2,
#     '**':lambda n1, n2: n1 ** n2,
#     '/':lambda n1, n2: n1 / n2,
#     '//':lambda n1, n2: n1 // n2,
#     '%':lambda n1, n2: n1 % n2

# }

# def main():
#     try:
#         num1 = int(input("Введите первое число:         "))
#         num2 = int(input("Введите второе число:     "))
#         operators = input("Введите операцию:            ")
#         func = calc[operators]
#         res = func(num1, num2)
#         print(num1, operators, num2, '=', res)
#     except ValueError:
#         print("Введите число")
#     except KeyError:
#         print("Такой операции нет")
#     except ZeroDivisionError:
#         print("На ноль делить нельзя")

# while True:
#     main()
#     inp = input("Завершить (yes, no)   ")
#     if inp.lower() == 'yes':
#         break





db = [
    {'name': 'Nikita', 'password': hash('nikita123')},
    {'name': 'nikita2', 'password': hash('12345678')}
]

def in_database(name):
    for user in db:
        if user['name'] == name:
            return True
    return False

def register(name, password1, password2):
    if in_database(name):
        raise Exception('Пользователь с таким именем уже существует!')
    if password1 != password2:
        raise Exception('Пароли не совпали!')
    user = {'name': name, 'password':hash(password1)}
    db.append(user)
    return 'Вы успешно зарегистрировались!'

def login(name, password):
    if not in_database(name):
        raise Exception('Пользователь не найден!')
    for user in db:
        if user['name'] == name:
            if user['password'] != hash(password):
                raise Exception('Пароль не верный!')
    return 'Вы успешно вошли в систему!'

def main():
    print("Добро пожаловать:        ")
    while True:
        try:
            action = input("Register:1. login:2, Quit:3\n       ")

            if action == '3':
                break
            elif action == '1':
                name = input("Введите имя:      ")
                p1 = input("Введите пароль:     ")
                p2 = input("Повторите пароль")
                print(register(name, p1, p2))
            
            elif action == '2':
                name =  name = input("Введите имя:      ")
                password = input("Введите пароль:     ")
                print(login(name, password))
            else:
                print("НЕккоректный выбор:      ")
        except Exception as error:
            print(error)

main()

# 1 - Функция отвечает за 1 Логику.

































