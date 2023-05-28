str_1 = "hello"
print(dir(str_1)) # выводит все возможные действия с переменной
print(str_1.upper()) # верхний регистр значения переменной

str_1 = "Hello" # верхний регистр все равно, даж если есть больгие буквы уже
print(str_1.upper())

str_1 = "hello"
print(str_1.title()) # верхний регистр только первой буквы

str_2 = "WORLD"
print(str_2)
print(str_2.lower()) # делает нижний регистр из значения

name = "Ivan"
a = "Hello {}" # {} - значит что можно в них передать какое-либо str зн-ние
result = a.format(name)
print(result)

name = "Ivan"
name = "Denis" # система будет сверху вниз читать Дениса
a = "Hello {}"
result = a.format(name) # позволяет форматировать строку, т е строка hello форматнулась(добавилась) переменная name.
print(result)

first_name = "Ivan"
last_name = "Ivanov"
a = '{} {}'
result = a.format(first_name, last_name)
print("Меня зовут: " + result)  # с конкатинацией

# f-string нотация, которая заменяет строчки 28 и 29, тот де резалт даёт
first_name = "Ivan"
last_name = "Ivanov"
result = f'{first_name} {last_name}'
print(result)

# 2.8
name1 = "Ihar"
Age = 30
result = f'My name is {name1}. I am {Age} years old.' # не надо переводить тип данных для 30ти в str в нотации
print(result)

# еще вариант написания более короткий
name1 = "Vasya"
Age = 29
print(f"My name is {name1}. I am {Age} years old.")

# сложение чисел в нотации
num_1 = 10
num_2 = 20
print(f"Сумма чисел равна {num_1 + num_2}")

var5 = "you"
var2 = " love me"
result = var5 + var2
print(result.upper())

var5 = "test"
print(var5.lower())

print(f"{var5} {var2} probably")























