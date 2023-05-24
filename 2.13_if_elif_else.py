#1. с пом условных операторов мы сможем создавать конструкцию,
# в которой будет заложена логика программы

age = 25 # присвоили зн-ние переменной
if age == 25: # 1ое условие, если возраст = 25
    print("Мне 25 лет") # то выводить эту надпись
else: # в любом другом случае вывести
    print("Мне не 25 лет") # эту надпись

age = 26
if age == 25:
    print("Мне 25 лет")
else:
    print("Мне не 25 лет") # вывод этой надписи

#2. можно задавать несколько условий
age = 24
if age == 25:
    print("Мне 25 лет")
elif age < 25: # elif помогает задать доп условие
    print("Мне меньше 25 лет")
else:
    print("Мне не 25 лет")

#3. Можно создавать несколько условий в оператор if
age = 25
name = "Ihar"
if age == 25 and name == "Ihar": # второе условие в if
    print("Мне 25 лет и меня зовут Ihar")
elif age > 25:
    print("Мне больше 25 лет")
else:
    print("Мне меньше 25 лет")

#4. условие or
age = 25
name = "Ihar"
if age == 25 or name == "Ihar":
    print("Мне 25 лет и меня зовут Ihar") # сработал этот участок кода т к полностью совпал
else:
    print("Мне меньше 25 лет")

#4.1
age = 20
name = "Ihar"
if age == 25 or name == "Ihar":
    print("Мне 25 лет и меня зовут Ihar") # сработал этот участок снова т к первое условие тож выполнилось, хоть и частично
else:
    print("Мне меньше 25 лет")

#4.2
age = 20
name = "Iha"
if age == 25 or name == "Ihar":
    print("Мне 25 лет и меня зовут Ihar")
else:
    print("Мне меньше 25 лет") # сработал этот участок, т к не было совпадений с первым условием, даже частично

#4.2
name = "Ihar" # присвоили строчное зн-ние переменной
if 'I' in name == "Ihar": # создали условие, регистрозависимое
    print("Меня зовут Ihar") # выводить это условие
else:
    print("Меня не зовут Ihar") # в остальных случаях - вот это, даже если I будет нижнего регистра

name = input()
if 'I' in name:
    print("Уася, ты красавчик, атвечаю!")
else:
    print("Эээээ, ты што твариш, Уася?!")

# name = "koleha"
# if "m" in name or "g" in name:
#     print("His name is Ihar")
# elif "k" in name:
#         print("His name is karen")
# else:
#     print("He has another name")
#
# программа для банкомата, кот будет принимать пин код от пользователя
pin = 1234 # корректный пин юзера
print("Введите пожаллуйста ваш пин-код") # приветствие банкомата
user_pin = int(input()) # просим ввести пин юзера

if pin == user_pin: # если пин правильный равен введенному
    print("Какую сумму вы хотите снять?") # вывести это сообщение
else:
    print("Пин-код не верный. Осталось 2 попытки") # если не равен, то вот это сообщение
    user_pin = int(input()) # ввод пин-кода второй попыткой
    if pin == user_pin:
        print("Какую сумму вы хотите снять?") # если пин правильный равен введенному со второй попытки
    else:
        print("Пин-код не верный. Осталось 1 попытка") # если не равен снова, то вот это сообщение
        user_pin = int(input()) # ввод пин-кода третьей попыткой
        if pin == user_pin: # если пин правильный равен введенному
            print("Какую сумму вы хотите снять?") # вывести это сообщение
        else:
            print("Карта заблокирована") # если не верно с 3 попытки

# код идет сверху вниз поэтому надо было посторить цикл три раза

# прога для ввода логина и пароля
login = "Ihar"
password = "123"
print("Введите креды")
user_login = input()
user_password = input()

if user_login != login and user_password != password:
    print('логин и пароль введены не верно. повторите попытку')
    user_login = input()
    user_password = input()
elif user_login != login and user_password == password:
    print('логин введен не верно. повторите попытку')
    user_login = input()
    user_password = input()
# elif user_login = login and user_password != password:
#     print('пароль введен не верно. повторите попытку')
#     user_login = input()
#     user_password = input()
else:
    print("welcome to the system")
    # user_login = input()
    # user_password = input()
    # if user_login != login and user_password == password:
    #     print('логин введен не верно. повторите попытку')
    # else:
    #     print("")
#
# elif user_login != login and user_password == password:
#     print('welcome to the system')