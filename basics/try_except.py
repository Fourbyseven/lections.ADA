"==================================== Exceptions ==================================="
# Исключения (ошибки), обькты, которые прерывают работу кода, если не были обработаны 

SyntaxError
#Исключение которые выходит когда в коде допушенно синтаксическая ошибка Error

"""
(
SyntaxError: unexpected EOF while parsing
(когда мы не закрыли скобочку или кавычку)
"""

"""
a = 
SyntaxError: invalid syntax
(когда мы сделали что-то не правильно в синтаксисе)
"""

ZeroDivisionError
# print(000000000000000000000000000000000000000)
# print(9 / 0 )

NameError 
# Исключение которое выходит когда мы обращаемься к несуществующей переменной 
# print(emka2)
#NameError Invalid 

IndexError
# Исключение которое выходит когда мы обращаемься по несуществуюшему индексу
# my_num = [1, 2, 3, 4, 5]
# print(my_num[100])
# """
# IndexError: list index out of range
# """

# [1, 2, 3, 4, 5].pop(1000)
#IndexError: pop index out of range

# [].pop() #IndexError: pop from empty list

KeyError
# Исключение которое выходит когда обращаемься по несуществуюшему ключу
my_dict  = {1:'a', 2:'b'}
# print(my_dict['b'])#KeyError: 'b'
# print(my_dict.pop('3')) # KeyError: '3'
#KeyError - Служит только для Dict


ValueError
# Когда мы передаем в функцию не корректный для нее тип данных
# когда мы распоковываем итерируемый обьект на несколько переменных и кол-во переменных 
# не совпадает с кол-вом элемментов в итерируемым обьекте

# int('dawdwa') # ValueError: invalid literal for int() with base 10: 'dawdwa'
# a, b, c, = [1, 2] # ValueError: not enough values to unpack (expected 3, got 2)
IndentationError
# Выходит Ошибка, когда мы неправильно используем отступы
    # a = 5 IndentationError: unexpected indent


# for i in range(10):
# print(i)
#IndentationError: expected an indented block after 'for' statement on line 58

TypeError
"""
Возникает когда мы пытаемься использовать не свойственные какому-то типу данных
когда мы пытаемься передать функции больше или меньше аргументов чем 
принимает функции
"""
AttributeError
#AttributeError Это ошибка методов например
# на list вызвать неправильный метод или аттрибут
#my_list = [1, 2, 3, 4, 5]
#my_list.get(2)
#AttributError




# for i in 123:
#     ... TypeError: 'int' object is not iterable


# print('213 ' + 213) TypeError: can only concatenate str (not "int") to str

# print(5  + '5') # TypeError: unsupported operand type(s) for +: 'int' and 'str'
 
# {[1, 2, 3]: 21} # TypeError: unhashable type: 'list'

# input('hello', 1) # TypeError: input expected at most 1 argument, got 2

Exception 
# Исключение которое создали, чтобы вызвали

"============================== <Вызов исключений> ============================"

# raise NameError('my except') NameError: my except


"=========================== <Обработка Исключений> ========================="
# Чтобы код не прекрашал свою работу мы можем использовать конструкцию
# try-except - и обрабатывать вызванное исключение 

# try:
#     # Код который возмажно вызовить ошибку 
#     num = int(input("Введите число:     "))

# except ValueError:
#     print('Вы ввели не число:       ')#  Ошибка, которая может возникнуть

# else:
#     # Код который отработает только если ошибка не вышло
#     print('Error', num)
# finally:
#     #Который отработает в любом случае 
#     print("До свидания")


# try:
#     raise ValueError
# except(SyntaxError, NameError,):
#     print('Вышла Одна из Ошибок: SyntaxError, NameError,')



# try:
#     raise Exception
# except:
#     print("Отловлена любая ошибка:      ")


# try:
#     raise TypeError("Type error ")
# except Exception as error:
#     print("Ошибка", type(error).__name__)


#raise - это блок кода который может вызывать ошибку в коде
#Например:
            #raise Type Error
# В этом случае raise вызывает typeError(Ошибка типа) 
# raise может просто вручную вызывать ошибки с помощью raise

"========================================== <ЗАДАЧИ> =========================================="

# 1 
try:
    pass
except:
    pass
else:
    pass
finally:
    pass


# 2 Напишите код, который пытается вывести значение переменной,
#  не определенной ранее, и обрабатывает исключение, выводя сообщение "Такой переменной не существует!".


# a = 10
# b = 15
# try:
#     print(c)
# except NameError:
#     print("Такое переменной не существует:          ")



# #3Напишите код, который принимает два числа от пользователя и выводит результат их деления. Обработайте исключение,
# #  которое выйдет при делении на ноль, выводя сообщение "На ноль делить нельзя"

# num = int(input("Введите число:     "))
# num_2 = int(input("Введите второе число:        "))

# try:
#     num / num_2
#     res = num + num_2
# except ZeroDivisionError:
#     print("На ноль не делиться:     ")
# else:
#     print(f"Ответ {res}")


#4

# str_num = input("Введите число:     ")
# str_num_2 = input("Введите второе число:        ")
# try:
#     print(int(str_num) + int(str_num_2))

# except ValueError:
#     print("Введите число!!!!!!!!!!!!!!!!!!!!!!!!!")

#5Напишите код, который пытается получить значение по ключу из словаря.
#  Обработайте исключение, которое выйдет если такого ключа нет, выводя сообщение "Нет такого ключа!".

# dict1 = {1:'a', 2:'b', 3:'c'}
# try:
#     print(dict1[5])
# except KeyError:
#     print("Такого ключа нету")
# finally:
#     print("Блок кода Finally")

# 6 - напишите код, который пытается получить элемент списка по индексу. Обработайте исключение 
# которое выйдет если такого индекса нет, выводя сообщение "Нет такого элемента!".

# my_list = [1, 2, 3, 4, 5]
# try:
#     print("Индекс:      ", my_list[6])
# except IndexError:
#     print("Такого Индекса нету:     ")
# finally:
#     print("Блок кода Finally")


# 7 Напишите код, который принимает возраст от пользователя и выбрасывает исключение ValueError с сообщением
#  "Доступ запрещён", если возраст меньше 18. Обработайте это исключение, выводя сообщение "Введён некорректный
#  возраст". Используйте блоки else и finally для вывода сообщений "Спасибо" и "До свидания!" соответственно.



# try:
#     age = int(input("Введите ваш возраст:       "))
#     if age <= 18:
#         raise ValueError('Доступ Запрешен')
# except ValueError:
#     print("Введен некооректный возраст:     ")
# else:
#     print("Спасибо за ответ:        ")
# finally:
#     print("Досвидания:      ")


# 8     Напишите код, который принимает два числа от пользователя и выводит результат их деления. Обработайте исключения 
# ValueError и ZeroDivisionError, выводя сообщение "Произошла ошибка!".
# try:
#     num_1 = int(input("Введите первое число:        "))
#     num_2 = int(input("Введите второе число:        "))
#     num_1 / num_2
#     res = num_1 = num_2
# except (ValueError, ZeroDivisionError) as error:
#     print("Произошла Ошибка:        ",type(error).__name__)
# else:
#     print(f"Ответ {res}")


#9 Напишите код, который принимает сумму денег от пользователя и выбрасывает исключение ValueError 
# с сообщением "Сумма не может быть отрицательной!", если сумма меньше 0. Обработайте это 
# исключение и выведите сообщение ошибки. Если исключение не возникло, выведите сумму.

# try:
#     num_1 = int(input("Введите вашу сумуу на Банкомат:      "))
#     if num_1  <= -1:
#         raise ValueError("Сумма не может быть отрицательной!")

# except ValueError:
#     print("Ваша сумма меньше нуля:  :(")
# else:
#     print(f"Результат Вашей суммы:      {num_1}")
# finally:
#     print("Блок кода FINALLY:       ")

#10
#Напишите код, который пытается вызвать метод get для списка. Обработайте исключение AttributeError,
#не выполняя никаких действий при возникновении ошибки.

# try:
#     my_set = [1, 2, 3, 4, 5]
#     print(my_set.get(30))
# except AttributeError as error:
#     print("Ошибка", type(error).__name__)
# finally:
#     print("Блок кода Finally:       ")

# 11 
# try:
#     num = 12
#     my_str = 'emka'
#     num + my_str
#     raise TypeError
# except TypeError as error:
#     print("Unsupported option", type(error).__name__)

# finally:
#     print("Блок кода Finally")





"""
=============================================================================================================
                                        <   Сложные ЗАДАЧИ TRY-EXCEPT    >
=============================================================================================================
"""

# 12 


# try:
    
#     my_list.extend(range(10))

# except NameError:
#     print('list does not exist')


#13
#Напишите код, который перебирает элементы списка, превышая его длину.
#  Обработайте исключение IndexError, не выполняя никаких действий при возникновении ошибки.
# list_ = [1, 2, 3, 4, 5, 6, 7]
# try:
#     for i in range(0, len(list_) + 1):
#         print(list_[i])
# except IndexError:
#     print("Ошибка")
 




#14 
#
# password = '12345'
# if len(password) < 6:
#     raise ValueError("Ошибка")



# try:
#     password = int(input("Введите пароль:       "))
#     if len(str(password)) < 6:
#         raise ValueError("Длина пароля не должна быть меньше 6 символов")
# except ValueError:
#     print("Пароль Должен из чисел:      ")

# 15
# warehouse = [
#     [[1], [2], [3]],
#     [[1, 2, 3], [1, 2, 3, 4, 5], {'hello': 'world'}],
#     ['1', '2', '3'],
#     [1, 2],
#     [[1], [2], [3]],
#     [[1, 2, 3], [1, 2, 3, 4, 5], {'hello': 'world'}],
#     [[1], [2], [3]],
#     [[1, 2, 3], [1, 2, 3, 4, 5], {'hello': 'world'}],
# ]

# if len(warehouse) > 10:
#     raise ValueError('На складе не должно быть более 10 коробок')

# for box in warehouse:
#     if len(box) > 3:
#         raise ValueError("В Коробке не должно быть более 3 > Элемментов")

# print(warehouse)



# 16

# try:
#     import lamabingo
# except ImportError:
#     print("Такого модуля не существует:     ")




# 17
# n = 10000000000000000
# try:
#     while n > 1:
#         n -= 1

# except KeyboardInterrupt:
#     print("Nope")



# 18


# my_input = input("Введите строку:       ").split()
# print(my_input)
# my_color = []

# for element in my_input:
#     try:
#         my_color.append(int(element))
    
#     except ValueError:
#         print("Данный элеммент не являеться числом:     ")
# print(my_color)





























































































































































































