______________________________________________________
PostgreSQL - это мощная обьекто реалиционная система управления базами данных (СУБД) с открытым исходным кодом. Она поддерживает сложные запросы, транзакции и высокую степень согласованности данных PostgreSQL широко используеться для хранения и управления структурированных данными обеспечивает масштабируемость и гибкость поддерживает различные типы данных и расширения

Также все типы данные рание такие как(Числовые, Строковые, Булевые все они инструменты PostgreSQL)

______________________________________________________
                        Основные комманды psql

\c - показывает к какой бд(база данных) подлючены и через какого user - пользователь
\c <name_of_db> -подключает к указанной бд
\l - показывает список всех бд 
\du  - показывает список всех user - с их правами
\dt  - показывает список таблиц в текущей бд
\d+ - показывает более подробную информацию о таблице
\d+ <name_of_table> - показывает более подробную информацию о указанной таблице 
\q - выход из  СУБД (из оболочки psql)
psql - Комманда для входа оболочку postgresql

_______________________________________________________
ПОДКЛЮЧЕНИЕ К БАЗЕ ДАННЫХ:
\c test_db



СОЗДАНИЕ ТАБЛИЦ В БД:
__________________________________________________
CREATE DATABASE name_of_db; - Создание базы данных 
DROP DATABASE name_of_db;   - Удаление базы данных
CREATE TABLE - Создание таблицы

DROP DATABASE имя_базы_данных; - Удаление база данных


ТИПЫ ДАННЫХ  POSTGRESQL:

Числовые типы данных:
1) smallint - хранит маленькие числа в диапозоне от -32767 до + 32767, в памяти занимает 2 байта,

2) integer - хранит числа в более широком диопозоне занимает 4 байта хранит средние значение 

3) bigint - хранит числа в самом большом дипозоне -23132138521491949214921 до  +2132149249219214921949124
занимает 8-байт

4) serial - числовой тип данных у которого есть автоинкремент 


СТРОКОВЫЕ ТИПЫ ДАННЫХ:
1) char(character) - используеться для строк, имеет фиксированную длину обязательно нужно указывать ограничение по символам

2) character varying(n) (VARCHAR) - такой же тип данных для строк, но имеет переменную  длину 
-
3) text - Тип TEXT позволяет хранить строки любой длины, что делает его очень гибким для хранения текстовой информации без необходимости заранее определять максимальное количество символов.
Также text - нету ограничения можно бесконечно записывать

Типы данных для работы со временем и датой

1) date - предостовляет дату  от 4713. до н. э. до 5215005 г н. э. занимает 4 байта в памяти
время - (год, месяц, день)

2) time -  хранит всемя с точностью до 1 микрасекунды без указания часового пояса. Принимает значения от 00.00.00, до 24.00.00, занимает 8 байт
время(час, минута, секунда)

Булевые значения:

boolean - хранит одно из двух значений: True, False

Вместо true - можно записать следующие значения: TRUE, 't', 'true', 'y', 'yes', 'on', '1'

Вместо false - записать следующие значения - FALSE, 
'f', '0', 'false', 'no', 'off'

json - хранит данные как javascript  - в текстовом виде:



Комманды для создания таблицы:

CREATE TABLE name_of_table (
    column1 data_type1, 
    column2 data_type2
    ...
);

-- Создает таблицу с полями 

Комманда для Удалаения таблицы:

DROP TABLE name_of_table;


Комманда для вывода данных  с таблицы:
SELECT * FROM name_of_table; Выводит все поля с данными с таблицы  - читает 

SELECT id, name FROM name_of_table; - выведит только поля id


Комманды для удобства нужно писать с большой буквы - SELECT FROM  - и.т.д



Комманда для заполнения таблиц:
INSERT INTO users_table(
     first_name, last_name, phone_number, user_name
) VALUES(
    'nikita', 'grebnev', '+996709522367', 'emka'
);


Команда INSERT INTO используется для добавления новых строк (записей) в таблицу базы данных. Формат команды зависит от того, добавляешь ли ты значения во все столбцы таблицы или только в некоторые из них.


Добавление данных во все столбцы:

sql


id serial означает, что PostgreSQL автоматически создаст уникальные значения для id при каждой вставке новой строки.
PRIMARY KEY указывает, что столбец id является первичным ключом. Это означает, что значения в этом столбце должны быть уникальными и не NULL. Первичный ключ обеспечивает уникальность и идентифицирует каждую строку в таблице.



INSERT INTO table_name (column1, column2, column3, ...)
VALUES (value1, value2, value3, ...);


# Вот так выглядит таблица с знчениями

serial   1 | emka       | umetov    | +996709522367 | EMIRLAN
serial  2 | chika      | arzybekov | +996709522367 | CHYNGYZ

Вот на что служит serial в таблице serial - тип данных.

_______________________________________________________


СОЗДАНИЕ ИНСТУКТОРОВ:

CREATE TABLE users_table (
id SERIAL PRIMARY KEY,
first_name VARCHAR(50), 
last_name VARCHAR(50),
phone_number VARCHAR(30), 
user_name VARCHAR(50));





3 - БАЗА ДАННЫХ
_______________________________________________________
КОММАНДА ДЛЯ ОЧИСТКИ ЗАПИСЯ ИЗ ТАБЛИЦЫ:

DELETE FROM name_of_table; - Удаляет все записи из Таблицы

id - заполняеться само по себе

Обновление записи в таблице:
UPDATE name_of_table SET column  = new_val;
Обновляет все записи в таблице 

UPDATE name_of_table SET column = new_val WHERE id <10; Обновления несколько записей id которых меньше 10.





УСЛОВИЯ:
DELETE FROM name_of_table WHERE id=4;
DELETE FROM name_of_table WHERE name='nikita';

Если Условия похожое то он удалит все записи которые похожие 


Выбирает все записи у которых в поле last_name есть название содержащее 'grebnev':
SELECT * FROM name_of_table WHERE last_name like '%grebnev%';

--like - Чувствительный к регистру (Grebnev - код не пройдет)


SELECT * FROM name_of_table WHERE last_name ilike  '%grebnev%'; -- ilike - не чувствительный к регистру


SELECT * FROM name_of_table ORDER BY column; -- Cортировка по определенному полю (по возрастнию ASC)

SELECT * FROM name_of_table ORDER BY column1 DESC; -- сортировка по убыванию (DESC)

ASC - ascending - возрастание
DESC - descending - убывание


SELECT * FROM name_of_table LIMIT 10;
После - LIMIT - нельзя ввести комманды









SELECT * FROM name_of_table OFFSET 5; -- Пропускает превые 5 записей в таблице и выводит все остальные


SELECT * FROM name_if_table LIMIT 5 OFFSET 5; -- пропускает 5 записей, выводит следуюшие 5.



_______________________________________________________
                            СВЯЗИ:
1) RRIMARY KEY (pk) - первичный ключ, ограничение которое наклдываеться на поле, которое будет использовано в связях

2) FOREIGN KEY (fk) - Внешний ключ которое накладываеться на поле, которое ссылаетсья на pk
в другой таблице

CREATE TABLE author(
id SERIAL PRIMARY KEY,
name VARCHAR(50),
last_name VARCHAR(50));

CREATE TABLE book(
id SERIAL PRIMARY KEY,
title VARCHAR(100),
published DATE,
author_id INT,
CONSTRAINT fk_book_author FOREIGN KEY (author_id) REFERENCES author (id));
CREATE TABLE


____________________________________________________________________________________________________________________________
Связи в базах данных помогают моделировать и управлять отношениями между различными объектами (или записями). Вот три основных типа связей, которые используются для построения и организации данных:

    Один к одному (1:1):
        Описание: Каждая запись в одной таблице связана с одной записью в другой таблице.
        Пример: В таблице Сотрудники и таблице Паспорт каждый сотрудник имеет только один паспорт, и каждый паспорт принадлежит только одному сотруднику.
        Применение: Используется для ситуаций, когда два объекта имеют уникальные, однозначные отношения.

    Один ко многим (1
    ):
        Описание: Одна запись в первой таблице может быть связана с несколькими записями во второй таблице, но каждая запись во второй таблице связана только с одной записью в первой таблице.
        Пример: В таблице Авторы и таблице Книги один автор может написать несколько книг, но каждая книга написана только одним автором.
        Применение: Подходит для случаев, когда один объект имеет несколько связанных объектов.

    Многие ко многим (N
    ):
        Описание: Записи в одной таблице могут быть связаны с несколькими записями в другой таблице, и наоборот. Эта связь обычно реализуется через промежуточную таблицу (связующую таблицу), которая содержит ссылки на обе таблицы.
        Пример: В таблице Студенты и таблице Курсы студенты могут записываться на несколько курсов, и каждый курс может иметь несколько студентов. Промежуточная таблица Записи связывает студентов и курсы.
        Применение: Используется для управления множественными связями между объектами.

Эти связи помогают организовать и структурировать данные, обеспечивая целостность информации и упрощая запросы для извлечения и анализа данных.


____________________________________________________________________________________________________________________________




ONE - TO - ONE - Один к Одному
1) Один человек - один ID
2) Один автор   - одна автобиография

UNIQUE - уникальность 


ПРИМЕР КОДА:

CREATE TABLE author(
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    age INT,
);

CREATE TABLE authobiography(
    id SERIAL PRIMARY KEY,
    body TEXT,
    created_at DATE,
    author_id INT UNIQUE ,
    CONSTRAINT fk_author_bio
    FOREIGN KEY (author_id) REFERENCES author (id)
);




ONE - TO - MANY -- один ко многим

CREATE TABLE curator (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50)
);

CREATE TABLE student (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    email VARCHAR(50),
    language VARCHAR(2),
    curator_id INT,
    CONSTRAINT fk_student_curator
    FOREIGN KEY (curator_id) REFERENCES curator (id)
);


MANY - TO - MANY -- Многие ко многим



CREATE TABLE developer (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    experience INT
);

CREATE TABLE project (
    id SERIAL PRIMARY KEY,
    title VARCHAR(100),
    tz TEXT,
    start DATE,
    finish DATE
);

CREATE TABLE dev_proj (
    dev_id INT,
    proj_id INT,

    CONSTRAINT fk_dev FOREIGN KEY (dev_id) REFERENCES developer (id),
    CONSTRAINT fk_proj FOREIGN KEY(proj_id) REFERENCES project (id)
);


_______________________________________________________


CREATE TABLE curator (  # Это создание таблицы `curator`, которая хранит информацию о кураторах
    id SERIAL PRIMARY KEY,  # `id` — это уникальный идентификатор для каждого куратора, автоматически увеличивается (SERIAL)
    name VARCHAR(50)        # `name` — это столбец для хранения имени куратора, ограниченный 50 символами
);

CREATE TABLE student (  # Это создание таблицы `student`, которая хранит информацию о студентах
    id SERIAL PRIMARY KEY,  # `id` — это уникальный идентификатор для каждого студента, автоматически увеличивается (SERIAL)
    name VARCHAR(50),       # `name` — это столбец для хранения имени студента, ограниченный 50 символами
    email VARCHAR(50),      # `email` — это столбец для хранения электронной почты студента, ограниченный 50 символами
    language VARCHAR(2),    # `language` — это столбец для хранения языка, которым говорит студент, ограниченный 2 символами
    curator_id INT,         # `curator_id` — это столбец для хранения идентификатора куратора, который назначен студенту, тип данных INT
    CONSTRAINT fk_student_curator  # Определение ограничения внешнего ключа для связи между таблицами
    FOREIGN KEY (curator_id)  # Указывает, что столбец `curator_id` является внешним ключом
    REFERENCES curator(id)  # Указывает, что внешний ключ ссылается на столбец `id` в таблице `curator`
);






___________________________________________
--JOINS--

JOIN - инструкция, которая позволяет в запросах SELECT брать данные из нескольких таблиц

INNER JOIN (JOIN) - достаются только те записи, у которых есть связь

FULL JOIN - достаются все записи с обеих таблиц

LEFT JOIN - достает все записи с левой таблицы, и с правой таблицы у которых есть связь с левой таблицей

RIGHT JOIN - достает все записи с правой таблицы, и с левой таблицы у которых есть связь с правой таблицей

'левая' таблица - та, которая написана до join'a a 'правая' таблица - та, которая написана после join'a 

_______________________________________________________





































                        ПРАКТИКА

-BLOG

Создание таблицы один ко многим:

СОЗДАНИЕ ТАБЛИЦЫ 


CREATE TABLE blogger(
    id serial primary key,
    name VARCHAR(50)
);


CREATE TABLE post(
    id SERIAL PRIMARY KEY,
    blogger_id  INT,
    body TEXT,
    created_at DATE,
    CONSTRAINT fk_post_blogger FOREIGN KEY (blogger_id) REFERENCES blogger (id)
)


ЗАПОЛНЕНИЕ ТАБЛИЦЫ:

INSERT INTO blogger(name) values ('nikita'), ('isa'),('emir'), ('torokul');

INSERT INTO post (blogger_id, body, created_at) VALUES
(1, 'some body', '2020-08-12'),
(1, 'some body', '2021-06-13'),
(1, 'some body', '2022-07-21');



INSERT INTO post (blogger_id, body, created_at) values 
(2, 'some body', '2005-1-21'),
(2, 'some body', '2003-4-21'),
(2, 'some body', '2004-4-12');


INSERT INTO post (blogger_id, body, created_at) values 
(3, 'some body', '2000-2-12'),
(3, 'some body', '2001-4-4'),
(3, 'some body', '2002-5-6');

INSERT INTO post (blogger_id, body, created_at) values 
(4, 'some body', '2013-2-21'),
(4, 'some body', '2014-4-5'),
(4, 'some body', '2015-6-12');






primary key: Обозначает, что столбец id является первичным ключом таблицы. Это значит, что значения в этом столбце будут уникальными и не могут быть NULL.


_______________________________________________________
                            SHOP

Вход чере терминал в postgres и создание бд:
1) комманда psql - Зайдет в оболочку postgres
2) Create Database shop; --  Создание база данных shop
3) \c shop -- подключение к база данных shop


_______________________________________________________


Работа с таблицами:

CREATE TABLE customer(
    id serial primary key,
    name varchar(50)
);

CREATE TABLE product (
    id serial primary key,
    title varchar(50),
    price DECIMAL
);


CREATE TABLE cart(
    id serial primary key,
    customer_id INT,
    product_id INT,
    CONSTRAINT cart_customer FOREIGN KEY (customer_id)
    REFERENCES customer (id),
    CONSTRAINT cart_product FOREIGN KEY (product_id)
    REFERENCES product (id)

);

---Заполнение таблицы:

INSERT INTO customer (name) values 
('customer_1'),
('customer_2'),
('customer_3');

INSERT INTO product (title, price) VALUES
('milk', 2.24),
('bread', 3),
('egges', 3.33),
('sugar', 5),
('salt', 1);


INSERT INTO cart(customer_id, product_id) values
(1, 3), (2, 1), (3, 5),
(1, 3), (2, 1), (3, 5);

1) Вы создали три таблицы (customer, product, cart), которые связаны между собой.

2) Таблица cart использует внешние ключи для обеспечения ссылочной целостности данных между customer и product.

3) Вы заполнили таблицы начальными данными, чтобы начать работать с ними.



_______________________________________________________

--------АГРЕГАТНЫЕ ФУНКЦИИ--------
SUM - функция которая считает сумму всех записей в сгрупированном поле

SELECT customer.name, SUM(product.price) AS total_price
 FROM product JOIN cart ON product.id = cart.product_id
JOIN customer ON customer.id = cart.customer_id
GROUP BY (customer.name);
ОТВЕТ:

    name    | total_price 
------------+-------------
 customer_3 |           2
 customer_1 |        6.66
 customer_2 |        4.48



ARRAY_AGG - ОБЬЕДИНЯЕТ записи с групированного поля в массив


-------- Пример из blog

select blogger.name, ARRAY_AGG(post.body) AS posts
FROM blogger JOIN post ON blogger.id = post.blogger_id
GROUP BY (blogger.name);

ОТВЕТ:

  name   |                 posts                 
---------+---------------------------------------
 nikita  | {"some body","some body","some body"}
 torokul | {"some body","some body","some body"}
 emir    | {"some body","some body","some body"}
 isa     | {"some body","some body","some body"}




-----MIN - MAX - Высчитывают минимальное и максимальное значение среди згрупированное поле.

select blogger.name, MIN(post.created_at) AS first, MAX(post.created_at) AS last FROM blogger JOIN post ON
blogger.id = post.blogger_id
Group BY (blogger.name);

ОТВЕТ:
 name   |   first    |    last    
---------+------------+------------
 nikita  | 2020-08-12 | 2022-07-21
 torokul | 2013-02-21 | 2015-06-12
 emir    | 2000-02-12 | 2002-05-06
 isa     | 2003-04-21 | 2005-01-21


_______________________________________________________

COUNT - считает количество записей в сгрупированном поле:

SELECT blogger.name, count(post.id) AS posts_count
FROM blogger JOIN post ON blogger.id = post.blogger_id
GROUP BY (blogger.name); 



ОВТЕТ:
  name   | posts_count 
---------+-------------
 nikita  |           3
 torokul |           3
 emir    |           3
 isa     |           3




-- Изменение таблиц----

ALTER TABLE  name_of_table ADD COLUMN col_name type constraint; -- Добавляет новую колонну в таблицу 

---------- ПРИМЕР ---------
ALTER TABLE blogger ADD column age INT;

УДАЛЕНИЯ поля:
ALTER TABLE name_of_table drop column col_name;
-- Удаляет колонну из таблицы

ПРИМЕР:
ALTER TABLE blogger drop column age;


Изменения существующий column:
ALTER TABLE name_of_table ADD CONSTRAINT constr_name constraint; - Добавлния ограничения на поле.









COLUMN - это 


























