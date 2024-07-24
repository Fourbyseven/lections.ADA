# 1) Создайте файл, внесите туда небольшой текст. В программе откройте этот файл и выведите содержимое на экран. 
# file = open('file.txt', 'a+')
# file.write("""
# Александр Пушкин начал писать свои первые произведения уже в семь лет.
# В годы учебы в Лицее он прославился, когда прочитал свое стихотворение Гавриилу Державину. 
#            Пушкин первым из русских писателей начал зарабатывать литературным трудом. 
#            Он создавал не только лирические стихи, но и сказки, историческую прозу и произведения 
#            в поддержку революционеров — за вольнодумство поэта даже отправляли в ссылки.
# """)
# file.seek(0)
# print(file.read())


# file.close()


# 2) Создайте файл users.txt. Напишите программу которая спрашивает
#  у пользователя его Логин и Пароль и записывает в файл users.txt

# File = open('users.txt', 'w+')


# my_user = input("Введите ваш Логин:         ")
# my_password = input("Введите ваш Пароль:        ")
# print(File.write("LOgin\n"))
# print(File.writelines(my_user))
# print(File.writelines("\nPAssword\n"))
# print(File.writelines(my_password))

# print(f"Логин {my_user}, Пароль:     {my_password}")



# File.close()



# 3) Создайте программу, которая считает из файла текст, и если в тексте содержится буква “w”,
# то выведет на экран “Да, в тексте есть w”, иначе - “Нет, в тексте нет w”. Подсказка: используйте ключевое слово in.

# with open('users.txt', 'r') as file:
#     content  = file.read()
# if 'w' in content:
#     print(" да в тексте есть w")
# else:
#     print("НЕт")

# print(file.closed)

# 4) Создайте текстовый файл python.txt и запишите в него текст #1 из github: Затем, считайте его. Найдите слова которые содержат букву  "o" и запишите в список o_words=[] и 
#   выведите на экран все полученные слова.
# текст: """
# Next, install the Python 3 interpreter on your computer. This is the program that reads Python programs and carries out their instructions;
# you need it before you can do any Python programming. Mac and Linux distributions may include an outdated version of Python (Python 2),
# but you should install an updated one (Python 3). See BeginnersGuide/Download for instructions to download the correct version of Python.
# """
text = """
# Next, install the Python 3 interpreter on your computer. This is the program that reads Python programs and carries out their instructions;
# you need it before you can do any Python programming. Mac and Linux distributions may include an outdated version of Python (Python 2),
# but you should install an updated one (Python 3). See BeginnersGuide/Download for instructions to download the correct version of Python.
# # """
# with open('python.txt', 'w') as file:
#     file.write(text)


# with open('python.txt', 'r') as file:
#     content = file.read()

# o_words = [word for word in content.split() if  'o' in word]
# print(o_words)



# file.close()


# 5)  Возьмите текст №2(GitHub), запишите его в файл. Далее считайте этот текст с файла и выведите в обратном порядке.
# """
# .detacilpmoc naht retteb si xelpmoC
# .xelpmoc naht retteb si elpmiS
# .ticilpmi naht retteb si ticilpxE
# .ylgu naht retteb si lufituaeB

# """


text = """
.detacilpmoc naht retteb si xelpmoC
.xelpmoc naht retteb si elpmiS
.ticilpmi naht retteb si ticilpxE
.ylgu naht retteb si lufituaeB

"""



# with open('task5.txt', 'w') as file:
#     file.write(text)
# with open('task5.txt', 'r') as file:
#     content = file.read()
#     reversed_countent  = content[::-1]
#     print(reversed_countent)



#6) Создайте файл и запишите туда текст №3(github). 
#В каждой строчке есть цифры, которые вместе дадут число. Посчитайте сумму всех чисел. 

# """
# 123
# aaa456
# fxdya 5 0 0
# """

text =  """
123
aaa456
fxdya 500
"""
 
with open('task6.txt', 'w') as file:
    file.write(text)
total_sum = 0
with open('task6.txt', 'r') as file:
    for line in file:
        print(line)
        for word in line.split():
            number = ''.join(filter(str.isdigit, word))
            if number:
                total_sum += int(number)

print(f"Сумма чисел:        {total_sum}")

















