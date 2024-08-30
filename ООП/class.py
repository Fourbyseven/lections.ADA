'=======================================OOP======================================='
# OOP - Объектно-ориентированное программирование (Парадигма)



class Person:
    # Переменные внутри класса (объекта) - аттрибуты класса
    arms = 2
    legs = 2
    brain = 1
    
    def __init__(self, name, age):
        # __init__ - метод, который будет добавлять в объект те аттрибуты, которые отличаются у разных объектов
        # self - ссылка на объект, который только что создался
        # аттрибуты экземпляра класса
        self.name = name
        self.age = age

    def walk(self):
        print(f'{self.name} ходит')

    def happy_birthday(self):
        print(f'{self.name}, Happy birthday!')
        self.age += 1
        return 'Подарок'


obj1 = Person('Nikita', 1)
print(obj1.name)
print(obj1.age)
print(obj1.arms)
obj1.walk()
obj1.happy_birthday()
print(obj1.age)
# print(obj1.hello) # AttributeError: 'Person' object has no attribute 'hello'
obj1.happy_birthday()
"=======================================Объекты класса==========================="
# объекты, экземпляр, instance класса - объект, созданный по шаблону класса (он перенимает все аттрибуты и методы класса)

'===================================Аттрибуты и методы==========================='
# аттрибуты - переменные
# методы - функции

class A:
    var1 = 'Переменная класса'

    def __init__(self) -> None:
        self.var2 = 'Переменная объекта'

print(dir(A))
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'var1']
# нет var2
obj2 = A()
print(dir(obj2))
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'var1', 'var2']
# var2 есть

# class Calculator:
#     def add(self, a, b):
#         'Функция сложения'
#         return a + b
    
#     def sqrt(self, num, ndigits=2):
#         'Функция нахождения квадратного корня числа с округлением'
#         import math
#         sqrt_num = math.sqrt(num)
#         return round(sqrt_num, ndigits)
    
#     def percent(self, total, percent):
#         'функция нахождения процента от числа'
#         return (total * percent) / 100
    
#     def super_func(self, string):
#         'Функция которая выполняет вычисления в строке'
#         return eval(string)
    

# calc = Calculator()
# print(calc.add(10, 10))
# print(calc.sqrt(5, 10))
# print(calc.percent(1000, 10))
# print(calc.super_func('(5-7)**2 - 10'))


class Sniper:
    health = 100

    def __init__(self, name) -> None:
        self.name = name

    def shoot(self, sniper2):
        sniper2.health -= 20
        print(f'Атаковал {self}')
        print(f'У {sniper2} осталось {sniper2.health}')

    def __str__(self) -> str:
        # когда принтим объект
        # когда оборачиваем в строку
        return self.name
    
sniper1 = Sniper('Nikita', 8)
sniper2 = Sniper('Sniper')

import random
while sniper1.health and sniper2.health:
    choice = random.randint(1, 2)
    if choice == 1:
        sniper1.shoot(sniper2)
    else:
        sniper2.shoot(sniper1)

if sniper1.health:
    print(f'Победил {sniper1}')
else:
    print(f'Победил {sniper2}')

