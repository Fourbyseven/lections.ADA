"================================== <SET> ==========================="
# set(множества) - изменяемые, неупорядочный,итеррируемый,  неиндексируемый тип данных который предназначен для хранения
# уникальных значений, Множества могут хранить в себе значения, Множества могут хранить в себе только неизмеяемый тип данных
# если вы используете Tuple то в них должны быть неизменяемые типы данных 

"""
FIFO
LIFO
"""



# set_1 = {1, 2, 3, 4, 5}
# set_2 = {1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, }
# set_3 = {(1, 2, 3), (1, 2, 3), (1, 2, 3), (4, 5, 6)}
# print(set_1)
# print(set_2)
# print(set_3)

"================================== <Методы set> ===================================="

# print(dir(set_3))

# .add() - Добавляет элемменты в set.

# set1 = {1, 2, 3, 4, 5}
# set1.add(6)
# set1.add(7)
# set1.add(True)
# print(set1)     #{1, 2, 3, 4, 5, 6, 7}



# .pop()    -   Удаляет Случайнный (РАНДОМНЫЙ) элеммент из set (но есть приницип FIFO):

# set2 = {1, 2, 3}
# popped = set2.pop()
# popped = set2.pop()
# popped = set2.pop()
# print(popped)
# print(set2)

# Если множества пустое то нельзя удалять set - #Key Error


# .remove() - Удаляет из set по значению (по ИМЕНИ)
# set3 = {1, 2, 3, 4, 5}
# set3.remove(3)
# set3.remove(4)
# set3.remove(2)
# # set3.remove(10) # Если указать не существующий элеммент: KeyError: 10
# print(set3) # {1, 5}



# .difference() (-)  - Метод difference выводит элементы, которые присутствуют
#  в одном множестве, но отсутствуют в другом.
# set_1 = {1, 2, 6}
# set_2 = {3, 4, 6}
# print(set_1 - set_2) # {1, 2, 6}
# print(set_2 - set_1) # {3, 4, 5}


# # .symmettric_difference() - это обьединение множеств(set)
#  - С удалением дубликатов и созданием новой переменной
# set_1 = {1, 2, 3}
# set_2 = {3, 4, 5}
# print(set_1.symmetric_difference(set_2))



# .intersection() - (&)     -  Этот метод возвращает пересечение двух множеств,
#  то есть множество элементов, которые присутствуют в обоих множествах A и B. 

# set1 = {1, 2, 3, 4, 5, 6, 7, 8}
# set2 = {4, 5, 6, 7, 8, 9,10}
# print(set1.intersection(set2))
# print(set1 & set2)



# .clear() - Очищяет множества.
# set1 = {1, 2, 3, 4, 5}
# set1.clear()
# print(set1)



# .union() - Он возвращает множество которое содержит все элемменты из всех переданных множеств 
#(Обьединения через Создании новой Переменной)

# set_1 = {1, 2, 3, 4, 5}
# set_2 = {True, False, (1, 2, 3)
# }
# set3 = {4, 5, 6, 7}
# result = set_1.union(set_2, set3)
# print(result)   # {False, 1, 2, 3, 4, 5, 6, 7, (1, 2, 3)}
# print(set_1.union(set_2, set3))



# .issubset()     -    проверяет, являеться ли одно множество, подмножеством другого (если все элемменты
# одного множества присутствует в другом, то вернеться true)
# set1 = {1, 2}
# set2 = {1, 2, 3, 4,5 }
# print(set1.issubset(set2))  #True



# .issuperset() - проверяет являеться ли множество надмножество другого множество

# set1 = {1, 2}
# set2 = {1, 2, 3, 4,5 }
# print(set1.issuperset(set2))
# print(set2.issuperset(set1))


# isdisjoint()  -  проверяет, не имеют ли 2 множества общих элемментов,
# Возвращает True/False

# set1 = {1, 2, 3}
# set2 = {4, 6, 4, 5}
# print(set1.isdisjoint(set2)) # true

#Возвращает True когда 2 множества не пересекаються друг у другу

# .discard() - Удаляет элеммент по указанному значению, если элеммент отсутствует, 
#то ошибка не вызываеться| Удаляет если указать неправильный значение то Ошибка не вызыветься.

# set1 = {1, 2, 3, 4}
# set1.discard(4)
# print(set1)

