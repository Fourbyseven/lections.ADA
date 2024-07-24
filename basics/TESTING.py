# try:
#     pass
# except:
#     pass
# else:
#     pass
# finally:
#     pass


# try:
#     my_num 
# except NameError:
#     print("Такой переменной не\n существует !")


# try:
#     my_num_1 = int(input("Введите число для деления 1:        "))
#     my_num_2 = int(input("Введите число для деления 2:      "))
#     my_num_1 / my_num_2
#     res = my_num_1 / my_num_2
# except ZeroDivisionError:
#     print("На ноль не делиться:     ")
# else:
#     print(f"Ответ:      {res}")
# finally:
#     print("Блок кода:       ")

# 4

# try:
#     my_str_1 = input("Введите число:   ")
#     my_str_2 = input("Введите число:    ")
#     my_num = (int(my_str_1) + int(my_str_2))
# except ValueError:
#     print("Введите число !!!!!!!!!!!!!!!!!!!!!!!!!!!      ")
# else:
#     print(f"Ваше число:      {my_num}")

# finally:
#     print("Блок кода Finally ")

# 5
# my_num = {1:'a', 2:'b', 3:'c' }
# try:
#     print(my_num[2])
# except KeyError:
#     print("Нет такого ключа")


#6

# my_list = [1, 2, 3, 4, 5]
# try:
#     print(my_list[3])
# except IndexError:
#     print("Нет такого Индекса")

# 7 

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


# 8
# try:
#     x = int(input("Введите число:       "))
#     y = int(input("Введите второе число"))
#     x / y
#     res = (x, y)
# except(ValueError, ZeroDivisionError) as Error:
#     print("Ошиба", type(Error).__name__)
# else:
#     print(f"Ответ Деления:      {x}")
# finally:
#     print("блок кода FINALLY:       ")


# 9

# try:
#     summa = int(input("Введите вашу сумму:      "))
#     if summa < -1:
#         raise ValueError("Сумма не может быти отрицательной:    ")
#     my_num = summa    
# except ValueError:
#     print("Ошибка:      ")


# else:
#     print(f"Ответ вашей суммы       {my_num}")

#10


# #1my_list = [1, 2, 3, 4, 5]
# try:

#     my_list.get(21)
# except AttributeError:
#     print("Неправильный метод:      ")




#11


# my_num = 10
# my_str = 'emka'
# try:
#     my_num + my_str
#     raise TypeError('Type Error')
# except TypeError:
#     print("Не явное конвертация ЧИСЕЛ")
# finally:
#     print("Блок кода Finally.")

# 12 

# my_num = [1, 2, 3, 4, 5]
# try:
#     my_num.extend(my_color)
# except NameError:
#     print("Ошибка Переменной")

















