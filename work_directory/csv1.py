"============================ <CSV КУРС> ================================"

# {'emka': 'umetov',
# 'akbar': 'toichubaev',}

#_________________________________________________________________________________________________________
# Что такое CSV файлы?

# CSV (Comma-Separated Values) - это формат хранения данных, где значения разделяются запятыми 
# (или другими разделителями, такими как точка с запятой).
# CSV файлы удобны для хранения и обмена данными в виде таблиц.
#_________________________________________________________________________________________________________

# Чтение данных из CSV файла:

# Для работы с CSV файлами в Python используется модуль csv.

# import csv

# # Чтение данных из CSV файла
# with open('file.csv', mode='r') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)

# В этом примере:

#     open('file.csv', mode='r') открывает файл file.csv для чтения.
#     csv.reader(file) создает объект reader, который позволяет итерироваться по строкам CSV файла.
#     for row in reader итерирует по каждой строке файла, где row представляет собой
#      список значений на этой строке.

#_____________________________________________________________________________________________________

#Запись данных  в CSV

# import csv

# # Данные для записи
# data = [
#     ['Имя', 'Возраст', 'Город'],
#     ['Алексей', 25, 'Москва'],
#     ['Елена', 30, 'Санкт-Петербург']
# ]

# # Запись данных в CSV файл
# with open('output.csv', mode='w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerows(data)

# В этом примере:

#     open('output.csv', mode='w', newline='') открывает файл output.csv для записи.
#     csv.writer(file) создает объект writer, позволяющий записывать данные в файл.
#     writer.writerows(data) записывает все строки данных из списка data в CSV файл.

# import csv 

# data = [
#     {'emka':'umetov', 
#      'age': 16,
#      }
# ]

# with open("name_fio.csv", mode='w') as file:
#     writer = csv.writer(file)
#     writer.writerow(data)
    


# with open("name_fio.csv", mode='r') as file:
#     read = csv.reader(file)
#     print(file.read())




















# Товар Самокат из 3 разных стран
import csv

data = {

        'Из': 'Самокат из Китая',
        'страна': 'Китай',
        'цена': 3000,
        'количество': 50
    
}

data_2 = {
 
        'название': 'Самокат из России',
        'страна': 'Россия',
        'цена': 2500,
        'количество': 40
    

}

data_3 = {
 
        
        'страна': 'США',
        'цена': 3500,
        'количество': 30
    

}


with open("samocat.csv", mode='w') as file:
    writer = csv.writer(file)

    writer.writerow(data.keys())
    writer.writerow(data.keys())
    writer.writerow(data.values())
    writer.writerow(data_2.values())
    writer.writerow(data_3.values())

with open("samocat.csv", mode='r') as file:
    read = csv.reader(file)
    print(file.read())