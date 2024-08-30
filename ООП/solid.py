#SOLID - это аббревиатура, для набора принципов проектирования, созданных для разработки ПО при помощи объектно-ориентированных языков. Принципы SOLID направлены на содействие разработки более простого, надежного и обновляемого кода

# При правильной реализации, это делает ваш код более расширяемым, логичным, и легким для чтения


# S (SRP)
"""
1) Single Responsibility Principle
(Принцип единственной обязанности)
Принцип единой обязанности требует того, чтобы один класс выполнял только одну работу. (Т.е. не надо создавать огромный класс который делает все)
"""

# Before
# class ExportCsv:
#     def __init__(self, raw_data) -> None:
#         self.data = self.prepare(raw_data)

#     def prepare(self, raw_data):
#         result = ''
#         for item in raw_data:
#             new_line = f"{item.get('name')}, {item.get('surname')}\n"  # Исправлено: двойные кавычки вокруг item['name'] и item['surname']
#             result += new_line
#         return result

#     def write_file(self, filename):
#         with open(filename, 'w') as f:
#             f.write(self.data)

# data = [
#     {
#         'name': 'Sherlock',
#         'surname': 'Holmes',
#     },
#     {
#         'name': 'John',
#         'surname': 'Watson',
#     }
# ]


# exporter = ExportCsv(data)
# exporter.write_file('out.csv')

#After 

class FormatData:
    def __init__(self, raw_data) -> None:
        self.data = raw_data

    def prepare(self, raw_data):
        result = ''
        for item in raw_data:
            new_line = f'{item['name']}, {item['surname']}\n'
            result += new_line
        return result
        



class FileWriter:
    def __init__(self, filename) -> None:
        self.filename  = filename
    
    def write_file(self, data):
        with open(self.filename, 'w') as f:
            f.write(self.data)


data = [
    {
        'name': 'Sherlock',
        'surname': 'Holmes',
    },
    {
        'name': 'John',
        'surname': 'Watson',
    }
]

formatter = FormatData(data)
formatted_data = formatter.prepare(data)



writer = FileWriter('out2.csv')
writer.write_file(formatted_data)



"""
Рассмотрим обькт "Выпивоха"
для выполнения принцип SRP разделим обязанности на троих
Один наоивает(PourOperation)
Один выпивает (DrinkUpOperation)
Один закусывает (TakeBiteOperation)
"""

"""
Плюсы:

1) Код стал предельно ясен на каждом уровне
2) код могут писать несколько разработчиков сразу (каждый пишет отдельный элеммент)
3) Упрощает автоматическая тестирования -тем проще элеммент тем проще тем легче кго тестировать

Минусы:

придется создавать больше обьектов 
"""

"""
2. О 

Open/closed principle
Принцип открытости и закрытости 

Программные сущности (классы, модули, Функции) Должны быть открыты для расширения но закрыты для модификации  
"""

                                                                                                                                                                                                                                                                                                                                                                                                                                                       

class Dicount:
    def __init__(self, customer, price) -> None:
        self.customer = customer
        self.price = price
        
    def give_discount(self):     # Скидку для обычных покупателей, одну для других другую если еще захотим добавить, то придется  дописывать логику
        if self.customer == 'fav':
            return self.price *0.2
        if self.customer == 'vip':
            return self.price * 0.4
        
"""
Чтобы следовать OCP, мы добавим новый класс который будет расширять Discoount.
И в этом новом кдассе реализируем требуемую логику 
"""




class Discount:
    def __init__(self, customer, price) -> None:
        self.customer = customer
        self.price = price

    def get_discount(self):
        return self.price * 0.2
    

class VOPDiscount(Dicount):
    def get_discount(self):
        return super().get_discount() * 2
    





"""
L - (LSP)
3.Liskov Substition Priciple
Принцип подстановки лисков

Главная идея, стоящая за LSP в том, что для любого класса клиент должен иметь 
возможность использовать любой подкласс базового класса, не замечая разницы между
ними, и следовательно без каких-либо изменений поведения программы при 
выполнения. Это Означает что клиент полностью изолирован и не подозревает об 
изменениях в иерархии классов

LSP - это основа хорошего обьектно ориентированного проектирования, ПО
потому что следует одному из базовых принципов ООП полиморфизм Речь отом чтобы создавать правильные 
Иерархии такие, что классы производные от базового класса являлись палиморфанные для их родителя 
по отношению к методам к их интерфейсом 

По простому - родительский класс можно заменить на дочерний не ломая логику, т.е 
Наследования должно быть логично что если родители и потомке есть какой то метод  этот метод должен принимать 
одинаковые количество аргументов примерно одной и той же логике следовать 


"""

# before

# class Bird:
#     def fly(self):
#         return 'i can fly'

# class Pengvin(Bird):
#     def fly(self):
#         raise NotImplementedError("Pingvins cant fly")

# def  make_bird_fly(bird: Bird):
#     return bird.fly()

# crow  = Bird()
# print(make_bird_fly(crow))

# penguin = Pengvin()
# print(make_bird_fly(penguin))

# class Bird:
#     def sound(self):
#         return 'I am a bird'
# class FlyingBird(Bird):
#     def fly(self):
#         return 'i can fly'
    
# class Penguin(Bird):
#     def swim(self):
#         return ' i can swim'
    
# def make_bird_fly(bird: Bird):
#     if isinstance(bird, FlyingBird):
#         return bird.fly()
#     return ' This bird cant fly'

# crow = FlyingBird()
# print(make_bird_fly(crow))

# penguin = Penguin()
# print(make_bird_fly(penguin))




"""
4. I - (ISP)
interface Segregation Principle
Принцип разделения Интерфейсов 

Создавайте тонкие интерфейсы которые оринетированны на клиента. Клиенты не должны 
зависеть от интерфейсов  (Или же методов которые не использует), которые они не изпользуют 
этот принцип устраняет недостатки реализации больших интерфейсов

Пример:  Если есть интерфейс который требует реализовать 100-методов но обьекту 
нужны только 2 из них то лучше разделить интерфейс на несколько маленьких
"""

#   before 
# class Worker:
#     def work(self):
#         raise NotImplemented

#     def eat(self):
#         raise NotImplemented
# class Developer(Worker):
#     def work(self):
#         print(' writing code')

#     def eat(self):
#         print('Eating food')

# class Robot(Worker):
#     def work(self):
#         print('Assembling parts')
    
# def manage_worker(worker:Worker):
#     worker.work()
#     worker.work()
    
# develloper = Developer()
# manage_worker(develloper)


# after

class Workable:
    def work(self):
        raise NotImplementedError

class Eatable:
    def eat(self):
        raise NotImplementedError

class Developper(Workable, Eatable):
    def work(self):
        return 'writing code'
    
    def eat(self):
        return 'eating food'
    
class Robot(Workable):
    def work(self):
        return "Assembling parts"
    
def mange_worker(worker: Workable):
    print(worker.work())

def manage_eater(eater: Eatable):
    print(eater.eat())

developper = Developper()
mange_worker(developper)
manage_eater(developper)
robot = Robot()
mange_worker(robot)




"""
D- (DIP)
Dependency Inversion Principle
(Принцип Инверсии  зависимостей)

Зависимость должна быть от абстрацией,   а не от конкретки. Модули верхних уровней
не должны зависеть от модулей нижних уровней. Классы вврехних нижних урровней 
должны зависеть от одних и тех же абстракций. Абстракция не должны зависеть от 
деталей детали должны зависеть от абстраций 
"""

# before 

# class My_SQLConnection:
#     def connect(self):
#         return 'Connected to MYSQL'

# class PasswordReimainder:
#     def __init__(self) -> None:
#         self.db_connection = My_SQLConnection
    
#     def remind(self):
#         return self.db_connection.connect()
# remmeinder = PasswordReimainder()
# print(remmeinder.remind())


#after 

from abc import ABC, abstractclassmethod
class DBConnectionInterface(ABC):
    def connect(self):
        ...

class MySQLConnection(DBConnectionInterface):
    def connect(self):
        return 'Connected to MYSQL'

class PostgreSQLConnection(DBConnectionInterface):
    def connect(self):
        return 'Connected to PostgreeSQL'
    
class SQLliteConnection(DBConnectionInterface):
    def connect(self):
        return 'connected to SQLLite'
class PosswordRedimer:
    def __init__(self, db_connection: DBConnectionInterface) -> None:
        self.db_connection = db_connection

    def remind(self):
        return self.db_connection.connect()
    
my_sql_connection = MySQLConnection()
posgrespl_connection = PostgreSQLConnection()
sqlite_connection  = SQLliteConnection


reminder = PosswordRedimer(my_sql_connection)
print(reminder.remind())



























































