# функции - это изолированный блок кода, кот. можно повторно использовать
# Они делают код модульным и более компактным, ниже код где много строк

# num_1 = 10
# num_2 = 20
# result = num_1 + num_2
# print(result)
#
# num_1 = 30
# num_2 = 40
# result = num_1 + num_2
# print(result)


#1 def summ() - Создание функции (summ - ее название)
def summ(): # задача функции вывести слово hello
    print("hello")

summ()

#2 Задача функции вывести резултат сложения двух чисел
def summ(num_1, num_2):  # num_1, num_2 - аргументы функции. Те арги, кот мы тут зада1м являются ОБЯЗАТЕЛЬНЫМИ!!
    result = num_1 + num_2
    print(result)

summ(10, 20) # здесь мы вызываем функцию при этом задавая значения ее аргументов в таком же виде, как мы ее и задавали
summ(30, 40) # можем вызвать функцию повторно

# !!!!!!!!!!!!! как создаем функцию:
# 1. Задали имя
# 2. В имени указали аргументы("переменные" по-старому)
# 3. Прописали действия(функции), которые функция будет делать, к прим print
# 4. Обратились к функции, указав значения аргументов(переменных), столько раз, сколько захочется

#3 Также можно играться функцией и на строчном типе данных
def stroka(str_1, str_2):
    result = str_1 + str_2
    print(result)

stroka("Hello", " World")

# пример того, что как мы подали значения аргументов так они и отобразятся
# мы поменяли местами hello и world - соотв-но они в обратном порядке и отобразились
def stroka(str_1, str_2):
    result = str_1 + str_2
    print(result)

stroka("World", " Hello")

# # но также в вызове переменной мы можем указать какое значение какому аргументу соответствует, т о задавая нужную нам последовательность вывода
def stroka(str_1, str_2):
    result = str_1 + str_2
    print(result)

stroka(str_2=" World", str_1="Hello") # поставив названия аргов со знаком равно перед зн-нием аргумента

# Создадим функцию, кот будет здороваться с пользователем
def hi(name):
    print("hello " + name)

hi("Ihar")

# задать значение аргумента можно и при создании ф-ции
def hi(name="Ihar"):
    print("hello " + name)

hi()

# еще можно вот так добавлять значение переменной в функции
name = "Ihar" # но нешта неудобно
def hi(name):
    print("hello " + name)

hi("Ihar")

def hi(name, age):
    print("Hello! My name is " + name + ". I'm " + age + " years old.")

hi("Ihar", "29")

# всегда следи за кол-вом аргов, иначе система даст ошибку
# раскомментить, чтобы проверить
# def hi(name, vozrast):
#     print("Hello! My name is " + name + ". I'm " + vozrast + " years old.")
#
# hi("Ihar") # пропущено зн-ние арга, система даст ошибку

# применение input для задания зн-ний переменным
# def hi(имя, возраст):
#     print("Hello! My name is " + имя + ". I'm " + возраст + " years old.")
#
# hi(input(), input())
# еще варик
# def hi(имя=input(), возраст=input()):
#     print("Hello! My name is " + имя + ". I'm " + возраст + " years old.")
#
# hi()

# можно делать как мы раньше делали, не чисто через print, а еще и с переменной резалт
def hi(имя, возраст):
    result = "Hello! My name is " + имя + ". I'm " + возраст + " years old."
    print(result)

hi(input(), input())

# return
Name = "Ihar"
Age = "29"
def my_age(Name, Age):
    result = Name + " " + Age
    return result # если мы не хотим выводить значение действия, то нужен return. Она возвращает какое-либо действие

h = my_age(Name, Age) # вызов функции надо помещать в переменную, если мы хотим ее вызвать
print(h)