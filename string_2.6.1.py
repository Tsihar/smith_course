# для хранения строчных данных

# 1 вывод зн-ния переменной
var_1 = "hello"
print(var_1)

# 2 вывод просто слова
print("hello")

# 3 2ух слов через переменные в две строки
var_1 = "hello"
var_2 = "world"
print(var_1)
print(var_2)

# 4 пример вывода строчных данных и чтения сверху вниз
var_1 = "hello"
var_2 = "world"
print(var_1)
var_2 = "people"
print(var_2)

# 5 пример исп-я одинарных ковычек, системе пофиг
# главное, чтобы одинарные с двойными не пересекались, иначе бут ошибка
var_1 = 'hello'
var_2 = "world"
print(var_1)
print(var_2)

# ошибка пересечения ковычек
# str_1 = 'world" #тут
# str_2 = "world"
# print(str_1)
# print(str_2)

# 6 сложение стринговых данных слитно и стринга ТОЛЬКО СКЛАДЫВАЕТСЯ
# так как мы не можем из слова вычесть слово, или разделить или перемножить слова
# НО есть нюнасы о которых ниже
var_1 = "hello"
var_2 = "world"
result = var_1 + var_2
print(result)

# ...раздельно (в необходимое место в значении переменной вставлять пробел)
var_1 = "hello"
var_2 = " world"
result = var_1 + var_2
print(result)

print('hello world')

# пример работы системы сверху вниз ()
# выдает helloworld так как система не видит, что мы поменяли значение переменно ниже
# система не может поднятся наверх и поменять str_2 на новое значение, поэтому его не видно
# а в пункте 4 все ок читается сверху вниз корректно также
var_1 = "hello"
var_2 = " world"
result = var_1 + var_2
var_2 = "people"
print(result)

# 7 умножение стринговых данных, 3 раза просто подряд выводит
var_1 = "hello "
var_2 = "world "
result = var_1 + var_2
print(result*3)

var_1 = "hello "
var_2 = "world "
result = var_1 * 2 + var_2 #умножение в переменной
print(result)

var_1 = "hello"
var_2 = "world " * 2 #умножение в переменной
result = var_1 + var_2
print(result)

# НО правильнее умножать в переменной result:
# если нам надо изменить переменную во всем коде(мы не правильно ее указали вначале, а в конце правильно), то мы рефакторим ее в переменной через меню

# 8 разные типы данных
var_1 = "три"
var_2 = "5" #ковычки дают для значения тип str
result = var_1 + var_2
print(result)

# расскомментить ниже чтоб увидеть ошибку
# var_1 = "три"
# var_2 = 5 #ковычек нет и соотв тип int, кот система не сложит
# result = var_1 + var_2
# print(result)

# 9 еще про ковычки, система норм воспринимает одинар ковычку внутри двойных
var_3 = "I don't love you"
print(var_3)

#10 конкатинация. делается только для строчныго типа данных
var_1 = "hello"
var_2 = "world"
result = var_1 + var_2
print(result)

var_1 = "hello"
var_2 = "world"
print(var_1 + " !!! " + var_2) # пробелы тож играют роль

var_1 = "5"  # строчный тип
var_2 = "10" # строчный тип
print(var_1 + " " + var_2)

# раскомментить чтоб увидеть ошибку
# var_1 = 5  # целочисленный тип
# var_2 = "10" # строчный тип
# print(var_1 + " " + var_2) # на выходе бут ошибка

# раскомментить чтоб увидеть ошибку
# var_1 = 5
# var_2 = 10
# result = var_1 + var_2
# print("Результат: " + result) # ошибка так как строку складываем с числом

var_1 = 5
var_2 = 10
result = var_1 + var_2
print("Результат: " + str(result)) # ошибки нет так как result преобразован в строку
# подсветка кода зеленым - код работает, ное сть грамматич ошибка

var_1 = 5
var_2 = 10
result = var_1 + var_2
print("Результат: " + str(15)) # ошибки нет так как число 15 преобразовано в строку


























