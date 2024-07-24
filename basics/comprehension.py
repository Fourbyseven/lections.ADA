"==================== <Comprehension> ============================"
#   Генератор с помощью которого мы можем создавать поссследовательность используя
#   for в одну строку 
"""
# 1 Результат for элеммент in посследовательность 
i for i in list1

# 2 результат for элеммент in посследовательность if фильтрация
i for i in list1 if i % 2 == 0

#3 Тело 1 if условие else тело2 for элеммент in посследовательность  - Условие 

#4 'четное' if i % 2 == 0 else 'нечетное' for i in  range(1, 11)
"""

# comprehansion = (i for i in range(1, 6))
# #<generator object <genexpr> at 0x7b6cd8022570>
# print(comprehansion)
#Генератор это итерируемый обьект, который не хранит в себе полностью всю
#посследовательность  данных, а создаст их когда требуеться 

# print(next(comprehansion)) # 1 
# print(next(comprehansion)) # 2
# print(next(comprehansion)) # 3
# print(next(comprehansion)) # 4
# print(next(comprehansion)) # 5
# print(next(comprehansion)) # StopIteration

# next() - Функция которая запрашивает у генератора текущее элеммент

"===================================== <Синтаксический caхар >=============================="
# list comprehension
# list_comprehension = list( (i ** 2 for i in range(1, 6))  )
# print(list_comprehension)   
# # [1, 4, 9, 16, 25]

# list_comprehension_2 = [i ** 22 for i in range(1, 7)]
# print(list_comprehension_2)
# #[1, 4194304, 31381059609, 17592186044416, 2384185791015625, 131621703842267136]

" Создайте список состаящий из четных чисел от 1 до 10 используя comprehension"
# my_comprehension = [i for i in range(1, 10) if i % 2 ==0]
# print(my_comprehension)
# list_comp = [i for i in range(2, 11, 2)]
# print(list_comp)



# list3 = []
# for i in range(1, 11):
#     if i % 2 == 0:
#         list3.append(i)
# print(list3)


"Создайте список состоящий из 5 строк 'hello', используя 'complehansion'"
# list1 = []
# for i in range(5):
#     list1.append('hello')
# print(list1)
# #['hello', 'hello', 'hello', 'hello', 'hello']

# list1 = ['hello' for _ in range(5)]
# print(list1) #['hello', 'hello', 'hello', 'hello', 'hello']
# "Создайте список состоящий из чисел от 1 до 10, но вместо чисел написать или нечетное."


# list2 = ['четное' if i % 2 == 0 else 'нечетное' for i in  range(1, 11)]
# print(list2)


# list2 = []
# for i in range(1, 11):
#     list2.append('четное' if i % 2 == 0 else 'нечетное')
# print(list2)



# "Создайте список из существующего списка оставив только строки"
# #Нужно выполнить 2 способами с использованием обычного и с comprehansion)
# list_1 = [1, 1, 213.12, 'emka', 'gmail', 'charlse_oliveira']


# # list_1  = [n for n in list_1 if type(n) == str] 
# # print(list_1)

# for n in list_1:
#     if type(n) == str:
#         list_1.append(n)
# print(list_1)

"=========================================== <Dict comprehension> ============================================="

# dict_ = dict((i, i ** 2) for i in range(10) )
# print(dict_)
# dict_2 = {i: i **2 for i in range(10)}
# print(dict_2)

"Дан Словарь создать его копию с помощью comprehension"
# dict1 = {'a':1, 'b':2, 'c':3}
# dict2 = {key: Value for key, Value in dict1.items()}
# print(dict1)
# print(dict2)


"Дан словарь поменяйте ключи со значениями при помощи comprehension"
# dict1 = {'a':1, 'b':2, 'c':3}
# dict2 = {Value: key for key, Value in dict1.items()}
# print(dict1)
# print(dict2)

"Дан словарь где значения это списки с числами, создайте словарь где значениями будут суммы этих чисел"


# dict1 = {
#     "a":[1,2,3,4],
#     "b":[10,15,16,17],
#     "c":[1,2,54]
# }


# dict1 = {key: sum(value) for key, value, in dict1.items()}
# print(dict1) # {'a': 10, 'b': 58, 'c': 57}

# "Дан словарь ключами где числа от 1 до 10 а значения эти же числа в виде строк"

# dict_ = {i:str(i) for i in range(1, 10)}

# print(dict_)



# dict_ = dict((i, i ** 2) for i in range(10) )
# print(dict_)
# dict_2 = {i: i **2 for i in range(10)}
# print(dict_2)

"Даны 2 списка, создайте словарь ключами будут элемменты 1 списка а значения элемменты 2 списка"


# list1 = [1, 2, 3, 4, 5]
# list2 = ['a', 'b', 'c', 'd', 'e']

# # 1-Способ 
# dict_ = {}
# for ind in range(len(list1)):
#     key = list1[ind]
#     value = list2[ind]
#     dict_[key] = value
# # print(dict_)

# # Итерация это прохождения врашения в этом случае 5 итерации сработало

# # 2 способ
# dict_ = {list1[ind]: list2[ind] for ind in range(len(list1))}
# print(dict_)
# # Comprecasion - Упрощяет и служит в Циклом


# # 3 - Способ

# dict_1 = dict(zip(list1, list2))
# print(dict_1)

"=================================== <Вложенные comprecension> ========================================="
"Создайте словарь где ключами будут числа от 1 до 5, а значениями - списки "
"числами от 1 до этого числа"

# 1 способ

# dict__ = {}
# for i in range(1, 6):
#     key = i
#     print(key)
#     value = [j for j in range(1, i+1)]
#     print(value)
#     dict__[key] = value
#     print(dict__)



# 2 способ 

# dict_1 = {i: [j for j in range(1, i+1)]for i in range(1, 6)}
# print(dict_1)



# # 3 способ 
# dict_ = {i: list(range(1, i+1)) for i in range(1,6)}
# print(dict_)


# "Создать список, состоящий из 10 списоков в которых строка hello world повторяеться по 5 раз"
# list1 = []
# for i in range(10):
#     inner_list = []
#     for j in range(5):
#         inner_list.append("hello world")
#     list1.append(inner_list)
# print(list1)



# # 2 - способ


# 3 способ
# list1  = [['hello world']* 5 for i in range(10)]
# print(list1)

# 4 Способ

# list1 = [['hello world']*5] * 10
# print(list1)


"""Создать список состоящий из 10 списков в которых будут числа от 1 до 5"""
# list1  = [[1, 2, 3, 4, 5] for i in range(1, 11)]
# print(list1)





            # Все Comperhension в python:

# Списковые компрехеншны (List Comprehensions)
# Множественные компрехеншны (Set Comprehensions)
# Словарные компрехеншны (Dictionary Comprehensions)
# Генераторные выражения (Generator Expressions)



# Способ  
# dict_ = {}

# for i in range(1, 6):
#     inner_dict = {}
#     for j in range(1, i+1):
#         list_ = []
#         for key in range(1, j + 1):
#             list_.append(key)
#         inner_dict[j] = list_
#     dict_[i] = inner_dict

# print(dict_)


# 2 Способ

# dict2 = {
#     i:{
#         j:[k for k in range(1, j+1)] for j in range(1, i + 1)
#     }
#     for i in range(1, 6)
# }
# print(dict2)



# # Дан словарь:
# dict1 = {"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Miivan": 1600, "Vann": 2400, "Semi": 13600, "Bicycle": 7, "Motorcycle": 110}
# # Создайте словарь dict2:
# # - Ключи должны быть те же, что и в первом словаре, но каждый символ 'i' замените на ''
# # - Значением должно быть количество повторений символа 'i' в этом ключе


# dict_2 = {k.replace('i', ''): k.count('i') for k in dict1}
# print(dict_2)


# Используя приведенный словарь dict_, создайте список из id, 
# которые хранятся под ключом comments. Берите только те комментарии, 
# количество которых больше 3
dict_ = {
    'Dasha': {
        'likes': 15,
        'comments': [
            {'id': 1, 'text': 'some text'},
            {'id': 2, 'text': 'some text'},
        ],
        'rating': 2
    },
    'Luna': {
        'likes': 12,
        'comments': [
            {'id': 1, 'text': 'some text'},
            {'id': 2, 'text': 'some text'},
            {'id': 3, 'text': 'some text'},
        ],
        'rating': 1
    },
    'Rena': {
        'likes': 26,
        'comments': [
            {'id': 1, 'text': 'some text'},
            {'id': 2, 'text': 'some text'},
            {'id': 3, 'text': 'some text'},
            {'id': 4, 'text': 'some text'},
            {'id': 5, 'text': 'some text'},
            {'id': 6, 'text': 'some text'},
        ],
        'rating': 2
    }
}


#  Способ 
# ids = []

# for inner_dict in dict_.values():
#     print(inner_dict)
#     comments = inner_dict['comments']
#     if len(comments) > 3:
#         print(comments)
#         print(len(comments))
#         for comment in comments:
#             print(comment, '---------------------------------')
#             ids.append(comment['id'])

# # 2 Способ 
# print(ids)



# ids = [comment['id'] for inner_dict in dict_.values() for comment in inner_dict['comments'] if len(inner_dict['comments']) > 3]
# print(ids)


