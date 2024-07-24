"================================== <TUPLE> =============================="
# Кортеж(tuple) - неизменяемый, индексируемый, Упорядочный, итерируемый тип данных
# предназначенный для хранения любых данных в определенном порядке
# (в Целом не отличаеться от списков, просто он не изменяемый ,
# поэтому занимает меньше памяти)

tuple1 = (1, 2, 3)
print(tuple1)
print(type(tuple1)) # <clas tuple>
tuple2 = (5) #<class 'int'>
print(type(tuple2))

# Обозначения tuple - это запятые 
tuple3 = 1, 2, 3
print(tuple3)
print(type(tuple3)) # <class 'tuple'>

tuple4 = (1, 2, 3, 4, [1, 2, 3])
tuple4[-1].append('hello')
print(type(tuple4[-1])) #<class 'list'>
print(tuple4[-1])
print(tuple4)

tuple5 = tuple([1, 2, 3, 'hello'], 2)
print(tuple5)
print(type(tuple5))

print(dir(tuple4))
# .count() - считает количество принятого эдеммента в кортеже (tuple)
tuple_ = (1, 1, 1, 1, 2, 3, 4, 5, 6, True, False)
print(tuple_.count(1))
tuple6 = ('hello', 'hello', 'hello')
print(tuple6.count('hello'))


# .index() - Возвращает индекс первого вхождения принятого элеммента 
tuple_8 = 1, 2, 3, 4, 5, 6, 'hello', 100
print(tuple_8.index(100))



"==================================== <КОНЕЦ> ================================="







