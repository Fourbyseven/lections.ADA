"===================================== <Модули и пакеты> =================================="
# Любой файл с расширением .py - это модуль 
# Пакет - набор модулей (Обязательно должен быть файл  __init__.py)


"====================================== <Работа с Файлами> ======================================"
# open() - Функция которая открывает файл в определенном режиме


'Режим'
# r - read (только для чтения)
# w - write (только для записи если такого файла нет то он его создаст. Каждый раз файл очищяеться)
# a - append (только для запии, данные добавляються в конец)
# x - Создаст файл, но если файл существует выйдет ошибка
# b - binary (в бинарном виде)




"================================= <Read> ===================================="
file = open('test.txt', 'r')
# print(dir(file))
# print(file.writable())  # False (Проверяет можно ли записывать что-то в файл)
# print(file.readable()) # True
# print(file.read())  # Потому что коретка находиться в конце
# file.seek(0)        # Метода переносит коретку в самое начало
# print(file.read())
# print(file.read(5))
# file.seek(0)
# print(file.readline()) #hello (Читает Одну строку )
# print(file.readline()) # world
# print(file.readline())# ADA
# print(file.readline())# effe

# file.seek(0)
# print(file.readlines()) # Выводит строку ввиде List

#\n  - Отступ на нижний отступ














file.close()


# print(file.readlines()) #  Ошибка -     ValueError: I/O operation on closed file.



"=====================================================Write ================================================="


file = open('test2.txt', 'w')
# Если такого файла нет то он его создаст 
# print(file.readable())
# print(file.writable())
# file2 = open('test.txt', 'w')
#  Стерает данные существуюшего файла есл они там есть

# file.write("hello\n") # Принимает строку и записывает его файл

# file.write('World\n')
# file.writelines(['hello', ' world\n']) #  Принимает список строк




file.close()


"===================================== <Append> ========================================="
# file = open('test3.txt', 'a')

# # print(file.writable()) # True
# # print(file.readable()) # False
# file.seek(0)
# file.writelines(['hello\n', 'hello\n', 'hello\n'])



# file.close()


"============================== <Контекстный менеджер > ======================================"
# Конструкция with ... as ...

# try:
#     file = open('wadwad', 'w')
#     file.read()
# finally:
#     file.close()
#Контекстный менеджер под копотом

with open('test.txt', 'r') as file:
    file.seek(0)
    print(file.read())

print(file.closed)  # True












