"=================================<list>==============================="

#  Списки - это изменяемый,
#  индексируемый, упорядоченный, итерируемый тип
#  данных, который предназначен для хранения любых данных в определенном порядке

list_1 = [1, 2, 3,  'hello', [1, 2, 3], [[[1, 2, 3]]], None, True, False,
 (1, 2, 3), {1: 2, 3: 4}]

print(list_1[1])
print(list_1[3][-1])
print(list_1[-1])
print(list_1[4][2])
print(list_1[8])

new_list = list('hello world')
print(new_list)

# # range() - задает диапозон чисел, принимает 3 аргумента, 
# 1 - начало диапозона, 2 - конец, 3 - шаг

list2 = list(range(1, 11))
print(list2)

list_3 = [1] *10
print(list_3)

"======================= <Методы списков> ================================"

#print(dir(list_3))

print("__________________________________________________________________________________________")
# append() - добавляет элеммент в конец списка 
list_ = []
list_.append(1)
list_.append(2)
list_.append(3)
list_.append('hello')
list_.append(True)
print(list_)

# .pop - Он удаляет элеммент из списка по индексу
# И результатом метода будет удаленный элеммент (метод возвращает уделенный элемент)
# если не указать вызываеться ошибка
poped_el = list_.pop(4)
print(poped_el)
print(list_)
poped_el = list_.pop(-1)
print(poped_el)
#list_2.pop()

# remove() - Удаляет элеммент из списка по значению

#list2 = [1, 2, 3, 4, True, 'hello']
#list2.remove(2)
#list2.remove('hello')
#print(list2)

#list2 = new_func()
#[1, 3, 4, True]

#count() - Считает количество принятого элеммента в списке
#print(list2.count(1))
list3 = ['hello', 'hello', 'hello']
print(list_3.count('hello'))


# .index() - Возвращает index - первого вхождения принятого элеммента


list2 = ['hello', 'hello', 'hello', None, 6, 7, 8, 9, 10]
print(list2.index('hello'))
#print(list2(1000))     #TypeError

# insert() - Добавляет элеммент в список по Индексу
list2 = ['hello', 'hello', 'hello', None, 6, 7, 8, 9, 10]
list2.insert(0, 'WORLD')
list2.insert(5, False)
print(list2)

# extend() - добавления элемменты принятого списка в первый список изменяя его
#Расширения списка

list_4 = []

list_4.extend(list2)
#print(list2 + list_4)
print(list2)

# reverse() - изменяет список, раставляя его элементы в обратном порядке 
list_4.reverse()
print(list_4)

# .sort() - сортирует список, состоящий из элемментов одного типа данных
list_01 =  [10, 6, 5, 7, 8, 9, 4, 1, 2, 3]
list_01.sort()
print(list_01)

#list5 = [1, 2, 3, 100, 1231, 211, 22131313, 2000]
#list5.sort()
#print(list5)

list5 = ['a', 'b', 'c', 'd', 'A', 'B', 'hello']
# list5.sort()
# print(list5)





# clear() - Очищяет список 
list5.clear()
print(list5)


#   len() - считает количество элемментов в посследовательности 
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, [1, 2, 3]]
print(len(list1))
len(list1)

#Множествонное присваивания
a, b, c = 1, 2, 3
print(a,)
print(b)
print(c)

a,b = [1, 22]
print(a)
print(b)


name, age, city = ['emka', 16, 'Bishkek']
print(name)
print(age)
print(city)


"====================================== <Конец> =================================="



