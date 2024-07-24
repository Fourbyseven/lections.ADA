"======================== Декораторы ============================"
# Функци высшего порядка - Фкнкция, которая принимает аргументы другую функцию
#Создает внутри себя функцию, вызывает функцию возврашает функцию
#Декортаор - Функция высшего порядка, которая нужна чтобы расширять функционал
#Функции, не изменяя ее (Функция обертка)


#1

# def decorator(func):
#     def wrapper(*args, **kwargs):
#         from datetime import datetime   #Внутри функции можно импортировать Модули
#         print('start', datetime.now())
#         func(*args, **kwargs)
#         print('finish:  ', datetime.now())
#     return wrapper

# @decorator  # Иcпользуеться @ - собачка
# def hello():
#     print("Hello world")
    
# hello()

# @decorator
# def my_sqrt(x):
#     print(x ** 0.5)
# my_sqrt(25)

# @decorator
# def my_sqrt(x):
#     print(x - 0.5)
# my_sqrt(25)


#2 

# def func_start_time(func):
#     def wrapper(*args, **kwargs):
#         from datetime import datetime
#         now = datetime.now()
#         correct_format = now.strftime('%d.%m.%Y %H:%M')
#         print("Функция Запущенна", correct_format)
#         func(*args, **kwargs)
#     return wrapper
# @func_start_time
# def func1():
#     print("hello")
# func1()


# 3

# def decorator(num):
#     def inner_decorator(func):
#         def wrapper(*args, **kwargs):
#             for n in range(num):
#                 func(*args, **kwargs)
#         return wrapper
#     return inner_decorator

# @decorator(100)
# def hello():
#     print("hello world")
# hello()

"======================================================================================================"

#Задачи


#Напишите Декоратор benchmark 

import requests
from time import time
def benchmark(func):
    def wrapper(*args, **kwargs):
        start = time()
        func()
        end = time()
        time_exec = end - start
        print(f"Время выполнения:      {time_exec}  секунд:")
    return wrapper
@benchmark          # Вызов через - @ - собачка  - Decorator


def fetch_webpage() -> None:
    webpage = requests.get('https://google.com')

fetch_webpage()

































































