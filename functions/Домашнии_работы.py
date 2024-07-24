
# Задачи по встроенным функциям:

# 1) Напишите программу, которая принимает строку "hello" и выводит кортеж,
#  содержащий индекс и соответствующий символ для каждого символа строки, используя встроенные функции

# string = 'hello'
# num = tuple(enumerate(string))
# print(num)




# 2) Напишите программу, которая принимает список чисел list1
#  =  [-7, -2, 12, 32, 432, 23, 37, 11, 76, 0, -23, 45, -32, -56]
#  и выводит новый список, содержащий абсолютные значения этих чисел.

# my_list = [-7, -2, 12, 32, 432, 23, 37, 11, 76, 0, -23, 45, -32, -56]
# my_num = list(filter(lambda x: x > -0, my_list))
# print(my_num)



# 3) Напишите программу, которая принимает список list1
#  = ["hello", 123] и выводит новый список, содержащий тип каждого элемента исходного списка.

# list1 = ["hello", 123]
# str_1_int_1 = ['type-str', 'type-int']
# my_num = list(zip(list1, str_1_int_1))
# print(my_num)


# 4) Напишите программу, которая принимает список имен name_list
#  = ["rauchel", "john", "peter", "jessica", "steven123", "dandy34",
#  "kamest", "potter"] и выводит новый список, в котором к каждому имени добавляется строка 
# " Python", если длина имени больше 5 символов, и строка " JavaScript", если длина имени 5 
# символов или меньше. (Используйте функцию map() и f строки для форматирования и добавления
#  к имени новых слов)



# name_list= ["rauchel", "john", "peter", "jessica", "steven123", "dandy34",
# "kamest", "potter"] 

# mapped = list(map(lambda x: 'python' if len(x) > 5 else 'javascript', name_list))
# print(mapped)





# 5) Напишите программу, которая принимает список строк email_list
#  = ["123hello@gmail.com", "123", "hello"] и выводит новый список, в
#  котором строка остается неизменной, если она заканчивается на "@gmail.com", а если нет, то заменяется
#  на "Not valid email" (используйте map(), и метод строк .endswith(), если что посмотрите в лекции 
# по строкам как он использовался)

# email_list  = ["123hello@gmail.com", "123", "hello"]
# new_list = list(map(lambda x:x if x.endswith("@gmail.com") else 'Not valid email',  email_list))
# print(new_list)




# 6) Напишите программу, которая проверяет, является ли список list1
#  = ['a', 'n', 'n', 'a'] палиндромом, и выводит "YES", если это так, и "NO", если нет.

# from functools import reduce

# list1  = ['a', 'n', 'n', 'a']
# my_list = reduce(lambda x, y:'YES' if x == y else 'NO', list1)
# print(my_list)
# Чуть не понятно была




