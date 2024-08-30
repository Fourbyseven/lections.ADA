# Напишите программу которая суммирует все элемменты в списке 
#используя какую-то функцию
from functools import reduce

# list_1 = [1, 1200, 213, 124, 51214, 21213]

# new_list = reduce(lambda x, y: x + y, list_1)
# print(new_list) #73965


# Напишите программу которая возводит в квадрат каждый жлеммент списка

# list_1 = [1, 1200, 213, 124, 51214, 21213]

# res = list(map(lambda x: x**2, list_1))
# print(res) # 


# Напишите программу которая отберает только четные числа из изходного числа
# list_1 = [1, 1200, 213, 124, 51214, 21213]

# res = list(filter(lambda x: x % 2 == 0, list_1))
# print(res) # [1200, 124, 51214]




# Напишите программу которая отбирает слова длинна которых больше 7 из исходного списка

# list_ = ["inheritance", "solid", "polymorphism", "dry", "yagni"]

# res = list(filter(lambda word: len(word) >7, list_))
# print(res)


# Напишите программу которая считает количество четных и нечетных чисел в списке
# и выводит их количество в формате строки

# list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# list2 = len(list(filter(lambda x: x % 2 != 0, list_1)))
# list3 = len(list(filter(lambda x: x % 2 == 0, list_1)))
# res = f"Нечетные:  {list2}, четные:   {list3}"
# print(res)




#Напишите программу которая находит самое длинное имя в списке

# list1 = ["Paul", "George", "Ringo", "John"]
# res = reduce(lambda x, y: x if len(x) > len(y) else y, list1)
# print(res)

#Напишите программу которая меняет число на 'fizz' если оно делитьсяна на 3,  и на строку 'buzz'
# Если не делиться в диапозоне чисел от 1 до 50 включительно

# list1 = [x for x in range(1, 51)]
# list_2 = []
# for x in list1:
#     if x %

# res = list(map(lambda x: 'fizz' if x %3 ==0 else 'Buzz', range(1, 51)))
# print(res)

#Напишите программу которая находит минимальное значение у элеммента  в списке
list_1 = [1, 2, 3, 4, 1221, 122, 212, -123, 342, 654]
res = reduce(lambda x, y: x if x < y else y, list_1)
print(res)