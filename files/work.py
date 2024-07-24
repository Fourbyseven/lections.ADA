file = open('emka.txt', 'r')
# print(file.writable())
# print(file.readable())

# print(file.read())
# file.seek(0)
# print(file.read())

# print(file.readlines())_





file.close()



with open('emka.py', 'a') as file:
    # print(file.writable())
    # print(file.readable())
    file.write("""# Next, install the Python 3 interpreter on your computer. This is the program that reads Python programs and carries out their instructions;
# you need it before you can do any Python programming. Mac and Linux distributions may include an outdated version of Python (Python 2),
# but you should install an updated one (Python 3). See BeginnersGuide/Download for instructions to download the correct version of Python.
# """)
    
print(file.closed)

#closed, который является логическим значением (True или False), указывающим на то, закрыт ли файл.
    





# 1) Создайте файл, внесите туда небольшой текст. В программе откройте 
# этот файл и выведите содержимое на экран. 
# with open('file.txt', 'r') as file1:
#     print(file1.read())


# file.close()
# 2) Создайте файл users.txt. Напишите программу которая спрашивает у пользователя 
# его Логин и Пароль и записывает в файл users.txt


with open("users.txt", 'w') as file:
    user = input("ВВедите ваш Логин:        ")
    password = input("Введите ваш пароль:       ")
    file.write(f"Логин:      {user},  Пароль:       {password}")

file.close()
    







