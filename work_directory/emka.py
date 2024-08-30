import json # Импортирование json






# Создаие переменной json - для записи

data = [{
    'emka': 'umetov',
    'gmail': '.com',
    True:False
}]


# Читание json - через работой с файлами
with open('/home/hello/Desktop/lections.ADA/work_directory/data.json',mode='r') as file:
    res = json.load(file)
print(res)


#Запись в файл json

with open("/home/hello/Desktop/lections.ADA/work_directory/data.json", mode='w') as file:
    json.dump(data, file, indent=4)




