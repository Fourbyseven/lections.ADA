# "========================== <Словари> =============================="
# # dict -  изменяемый итерируемый неупорядочный и неидексируемый тип данных, для
# #хранения данных в паре {'ключ': 'значения'}

# user_ = {
# 'bool': True,
# 'country': 'Kyrgyazstan',
# 'city': 'BISHKEK'
# }

# print(user_['country'])
# print(user_['city'])

# # Ключами в словаре могут быть только неизменяемые типы данных

# dict1 = {
#     'a': 1, 
#     'b': 2,
#     'c': 3,
#     'a': 4,
# }
# print(dict1['a']) #4,  Если ключи одинаковые, то сохраниться только посследнее значение

# #print(dict1['d']) # KeyError - ошибка ключа


# dict3 = dict(["he", "cd", "ef"])
# print(dict3)

# dict4 = {}
# dict4['name'] = 'emka'
# dict4['city'] = 'bishkek'
# dict4['name'] = 'nikita' # Меняния местами 
# print(dict4['city'])
# print(dict4['name'])


"=============================== Методы словарей =================================="
#print(dir(dict4))

# МЕТОД_.get() - возвращает значение по ключу , если такого метода нет то возвращает None,
# Или дефолтное значение, Возвращает значение без ошибок 


user_ = {'name': 'emka',
         'city': 'bishkek',
         'country': 'Kyrgyzstan'
}
# print(user_['name'])
# print(user_['country'])
# print(user_['city'])


print(user_.get('id'))
print(user_.get('name'))
print(user_.get('country'))

# #.pop() - Метод который удаляет пару по ключу и возврашает значение 

# dict_1 = {'a': 1, 'b': 3, 'c': 5}
# popped = dict_1.pop('a')
# popped = dict_1.pop('b')
# print(dict_1)
# print(popped)


# # .popitem() - Метод который удаляет посследнюю пару и возвращает значение
# dict5 = {'a': 1, 'b': 3, 'c': 5}
# popped = dict5.popitem()
# print(dict5)

# dict0 = {}
# print(dict0.popitem()) # KeyError
# Key Error

# .update() - Расширяет словарь парами из второго словаря

# dict__1 = {1: 'a', 2: 'b', 3: 'c'}
# dict__2 = {2: 'c', 4: 'd'}
# dict__1.update(dict__2)
# print(dict__1)


# .clear() - удаляет все пары в словаре
# #1: 'a', 2: 'b', 3: 'c', 2: 'c', 4: 'd'}
# dict__1.clear()
# print(dict__1)
# # {}


# .fromkeys() - Метод для создания нового словаря, используя список ключей

# dict__1 = dict.fromkeys("hi")
# print(dict__1) # {'h': None, 'i': None}

# dict2 = dict.fromkeys([1, 2, 3, 4, 5])
# print(dict2)

# dict3 = dict.fromkeys([1, 2, 3], 'hello')
#  print(dict3)


"====================================================================================================="
# keys, values, items
#keys - метод который возвращает ключи
#values - метод который возвращает значение
#items - метод который возвращает пары  ключ - значение, в виде tuple



# user = {
# 'name': 'emka',
# 'city': 'bishkek'
# }
# print(user.keys()) # dict_keys(['name', 'city'])
# print(user.values()) # dict_values(['emka', 'bishkek'])
# print(user.items()) # dict_items([('name', 'emka'), ('city', 'bishkek')])

"========================= Итерирование словарей ============================="
# Работа с Циклами

# user = {
# 'name': 'emka',
# 'city': 'bishkek',
# 'country': 'Kyrgyz'
# }

# for key in user:
#     print(key)
#     # name
#     # city
#     # country
#     # При словаря будут приходить ключи

# for key in user.keys():
#     print(key)
#     # name
#     # city
#     # country
#     # name
#     # city
#     # country
#     # При итерации dict_keys тоже проходят ключи

# print("---------------------------")


# for values in user.values():
#     print(value) 
#     # emka
#     # bishkek
#     # Kyrgyz
#     # при итерации dict_values приходит значения

print("___________________________________________")

# for items in user.items():
#     print(items)
#     #('name', 'emka')
#     #('city', 'bishkek')
#     #('country', 'Kyrgyz')
#     #При итерации dict_items приходят пары (ключ - значение) в tuple  в ввиде



"_______________________________________ КОНЕЦ______________________________________________"


my_dict = {1: 'a', 2: 'b'}
my_dict_2 = {}

for keys, value in my_dict.items():
    my_dict_2[value] = keys

print(my_dict_2)
















