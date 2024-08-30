# "================================ <Строки> ================================"
# # Строки это неизменяемые тип данных, которые предназначены для хранения текста 
# # заключенного в одинарные или двойные кавычки

# str_1 = 'Строка с одинарными кавычками'
# str_2 = "Строка с двойными кавычками"
# #errror_strings = 'неправильная строка "
# str_3 = """
# Многострочный текст в двойных кавычках, можно использовать  'любые' == "кавычки" 
# """
# str_4 = 'Dont\'t'
# str_5 = "Dont't"

# "====================   < Конкетенация>    ================"
# name = "emka"
# last_name = "Umetov"
# full_name = name + ' ' + last_name
# print(full_name)

# print('hello' * 10) #Строки поддерживают умнажения:


# "============================ <Экранизация> ======================"

# #'\n' - переносит строку на новую строку - (начинает с красной строки)
# print('hello\nworld')
# #print('hello')
# #print('world')

# #\t - табуляция
# print('hello\tworld')


# # '\'' отоброжение одинарной кавычки 1х'
# # "\"" - отображение двойной кавычки 2х"

# # \v - перенос на новую строку со смещением на право
# # на длину предедущей строки 

# print("hello\vworld\vmy\vname\vemka")


# #\r - отвечает за перенос каретки на начало строки
# print("Hello\r")


# "======================== <Форматирование строк> ======================="

# title = 'iphone 15'
# price = 1000
# print(f"Название: {title}\nЦена: {price}")


# format_2 = "Название: {}\n Цена {}"
# print(format_2.format('iphone 15', '10000'))


# "===================== <Методы - строк> ==============="
# # Методы это функции, которые относятся
# # к определенному классу (типу данных) ним мы обращаемься через точку

# print(dir(str)) # dir() - показывает все методы определенного типа данных (класса)

# string_1 = 'hello'
# print(string_1.upper()) #Переводит все символы в верхний регистр
# #HELLO

# string_2 = 'HELOO'
# print(string_2.lower()) #Переводит все символы в нижний регистр
# #hello

# print('HELloo'.swapcase()) # противоположный регистр
# #helLoo

# string_3 = string_1
# print(string_3)

# print('hello world, my name, is EMka'.title()) # Переводит первый символ за главную букву каждого слова на верхний регистр

# a_01 = "hello world"
# print(a_01.title())
# #Hello world


# print('hello world'.capitalize()) # Переводит только первую букву первого слова в верхний регистр 
# #остальные слова остаютсья неизменимым


# print('Python Developper'.center(20, '-')) #центрует нашу строку по указанному ограничителю
# #(1 - значение - ограничение 2 - значение - разделитель)
# print('worldd'.count('d')) # Возвращает количество вхождений заданного символа 


# #startswith() - проверяет заканчиваеться ли строка заданным 
# #Символом/символами, возвращает True/False
# print('hello'.startswith('')) # Проверяет начинаеться ли строка с заданного  символая, возвращает True\False
# print('Hello'.startswith('h')) # Вернет False
# print('hello'.startswith('hello')) # True

# #.islower() - проверяет находиться ли строка полностью в нижнем регистре
# print('hello world'.islower()) #True
# print('hello worOds'.islower()) #False

# #.isupper() - проверяет находиться ли строка полностью в вверхнем регистре
# print('HELLO WORDS'.isupper()) #True
# print('hello worOds'.isupper()) #False

# #isdigit() - проверяет состоит ли строка полностью из чисел:
# print('21313123'.isdigit()) #True
# print('уфа213123123'.isdigit()) #False

# #isalpha() - проверяет состоит ли строка только из букв
# print('hello'.isalpha()) #true
# print('hello 213'.isalpha()) #false

# #isalnum() - используется для проверки того, состоит
# #  ли строка только из буквенно-цифровых символов 
# print('hello213'.isalnum()) #True
# print('hello'.isalnum()) #True

# #split() - Делает весь код на list
# #Возвращает список, который разделил по заданному разделителю на отдельные строки
# print('Hello world my name is Emka'.split())


# #join() - соединяет список по указанному разделютелю
# print('-'.join(['hello', 'worlds', 'my', 'name']))
# #hello-worlds-my-name


# #Strip() - Уберает пробелы слева и справа_
# string_color = '              hello'
# print(string_color.strip())


# string_123 = 'hello      '
# #lstrip() - Уберает все пробела слева
# print(string_123.lstrip())

# # rstrip() - Убирает все пробелы справа
# print(string_123.rstrip())

# print("_____________________________________________________________________________________________")

# "================================== <Индексы> ====================================="
# #Индекс порядковый номер в посследовательности
# #(символа в строке), (индексация начинаеться с нуля)


# 'h e l l o w o r l d'
# #0 1 2 3 4 5 6 7 8 9
# #-9-8-7-6-5-4-3-2-1

# string_1_1 = 'hello world'
# print(string_1_1[10])
# print(string_1_1[6])
# print(string_1_1[1])

# # срез - подстрока нашей подстроки 
# print(string_1_1[0:5]) #hello
# print(string_1_1[0:4]) #hell
# print(string_1_1[5:11]) #world
# print(string_1_1[6:]) #world

# print(string_1_1[::-1]) #dlrow olleh




"============================= <<<<<<<<<<<<<<<<<<<  |КОНЕЦ - The END | >>>>>>>>>>>>>>>>>>>>>>>>>> ============================="










a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)