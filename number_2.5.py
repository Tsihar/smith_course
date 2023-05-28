# почему при выполнении написанного здесь кода так много ответов?
# потому что система выполняет команды сверху вниз
# прочитала переменные > отдала результат(т к в этом коде везде функции вывода), прочитала переменные > отдала результат и т.д до самой последней строчки

#1
num1 = 1
num2 = 2
result = num1 + num2
print(result)

#2 пример чтения кода сверху вниз
num1 = 1
num2 = 2
result = num1 + num2
num1 = 2
print(result)

#3 чтение кода сверху вниз
num1 = 1
num2 = 2
num1 = 2
result = num1 + num2
print(result)

#4 вычитание
num1 = 1
num2 = 2
result = num1 - num2
print(result)

#5 отрицательность
num1 = 1
num2 = 2
result = -(num1 - num2)
print(result)

#6 умножение
num1 = 1
num2 = 2
result = num1 * num2
print(result)

#7 умножение в переменной можно делать
num1 = 1
num2 = 2
result = (num1 * num2)*2
print(result)

#8 умножение в принте можно делать
num1 = 1
num2 = 2
result = num1 * num2
num3 = 2
print(num3*2)

#9 ** - возведение в степень в принте
num1 = 1
num2 = 2
result = num1 * num2
num3 = 2
print(num3**4)

#10 ** - возведение в степень в переменной
num1 = 1
num2 = 2
result = num1 * num2
num3 = 2**4
print(num3)

#11 деление
num1 = 6
num2 = 4
result = num1 / num2
print(result)

#12 если хотим получить резалт целым числом >
# > надо задать тип данных int для переменной
num1 = 6
num2 = 4
result = num1 / num2
print(int(result))

#13 если хотим получить резалт целым числом >
# > надо производить деление(или другое действие) >
# > двойным делением //
num1 = 6
num2 = 4
result = num1 // num2
print(result)

#14 остаток от деления (6/4 это 4 целых,6-4 - в остатке 2)
num1 = 6
num2 = 4
result = num1 % num2
print(result)

#15 математич сравнение: >,<,>=,<=,==;
# в ответе, True или False
num1 = 6
num2 = 4
result = num1 == num2
print(result)
# когда ставим просто '=', то это значит присваивание значения
# а когда '==', то это уже приравнивание/равенство

num1 = 6
num2 = 4
result = num1 >= num2
print(result)

num1 = 6
num2 = 4
result = num1 < num2
print(result)

num1 = 6
num2 = 6
result = num1 <= num2
print(result)

#16 округление
# 1й варик чисто принтом
print(round(10/3))
# 2й варик через переменные
num1 = 6
num2 = 5
result = num1 / num2
print(round(result))

#17 округление до нужного знака после запятой
num1 = 10
num2 = 3
result = num1 / num2
print(round(result, 3))

print(round(10/3, 4))

#17 определение типа данных, как мы зададим, так потом
# и выведется
num1 = float(10.4)
# определили тип сразу в переменной, хотя хз зачем, если мы задаем сразу десятичную и система уже видит, что это float
# это делается для того, чтобы к прим если надо посчитать кол-во детей в семье
# а есть и данные int и float, то в итоге мы получили int так как детей не может быть 1.2, в резалте мы будем указывать int
num2 = 3
result = num1 + num2
print(result)

num1 = 10.4
num2 = 3
result = int(num1 + num2) # определили тип в переменной result
print(result)

num1 = 10.4
num2 = 3
result = num1 + num2
print(float(result)) # определили тип в функции вывода

num1 = float(10.4)
print(num1)
num2 = 3
result = int(num1 + num2)
print(result)




