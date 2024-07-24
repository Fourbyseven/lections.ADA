"=========================== <области видимости> ===================================="

# LEGB - local ecnclosed global built-in

"================================ <Built in> ========================================="
#Встроенные функции имен (list, sum, dict, print(), input)

"===================== <Global> =========================="
# Все переменные которые мы создали внутри одного файла
# Чтобы посмотреть все Глобальные переменные, Можно Использовать globals()

# a = 5
# b = 'hello'
# print(globals())

"=============================== <Локальная Область видимости> ============================="
#Локальная пространство имен - переменные, Созданные Внутри функции (цикла, Условия)
# def func(a, b):
#     print('GLOBALS', globals())
#     print("Locals", locals())
#     print(a, b)


# func(2, 6)


"======================== <Enclosed> ================================="
#Замкнутая Пространство имен это Лакальная пространство у которого есть Внутрнне локальное Пространство
# var = 'global'
# def func():
#     #Локальная пространство для глобального пространство 
#     # Замкнутая Пространство(потому что есть более локальное пространство)
#     var = 'enclosed'
#     def inner_func():
#         # Локальная пространство для пространство  func
#         var = ' local'
#         print(var) # 3) Local
#         print(func)  # enclosed
#     inner_func()


# print(var) # 1) global
# func()     



# a = 'hello '
# def abc():
#     a = '123'
# print(abc)
# print(a)


# count  = 1
# def increase_count():
#     global count
#     print(count)
#     count += 1

# increase_count()
# increase_count()
# increase_count()
# increase_count()
# increase_count()

# def count(i):
#     counter = 0

#     def increase_count():
#         nonlocal counter
#         #Доступ на изменения переменной  замкнутого пространства
#         print(counter)
#         counter += 1


#     for i in range(i):
#         increase_count()
    
# count()









































































