# Любой файл с расширением .py можно называть модулем
# Модули бывают:
# - Самописными
# - с различных библиотек питона
#
# Создадим файл modules_hello.py и 2.22_modules_start.py и подключимся к нему
# modules_hello.py - содержит ф-ю some, кот выводит на печать hello world
# в файл 2.22_modules_start.py необходимо прописать команду import, и указать название файла, кот мы импортируем
# чтобы вызвать ф-ю some необходимо - строки 1 и 2 файла modules_hello.py

# важно!!!
# когда мы импортим модуль система сначала ищет этот модуль в проекте (среди py файлов),
# если не находит, то ищет модуль с этим названием среди библиотек питона
# если опять не находит, то отдает ошибку
#
# 1 Создаём самописный файл
# import modules_hello
# modules_hello.some() # вызываем ф-ю some() из файла modules_hello, обяз надо указывать с обращением к файлу вначала,
# иначе система не поймет откуда мы берем эту ф-цию, т к в текущем файле ее нет.
#
# 2. Используем библиотеку math
# import math
# print(math.pi) # вывод числа пи.
# по клику после math. (до ввода ч-л после math.) можно увидеть весь список действий, кот позволяет делать эта ф-ция
#
# 3. библиотека random - позволяет получить рандомные зн-ния
# import random
# r = random.randrange(0, 10) # т е можно даже модуль впихать в переменную
# randrange() = операции range(), кот проходили, арифм прогрессия
# эта ф-я может понадобится, когда нужно создать нового юзера и присвоить ему рандомное имя
# print(r) #нажимая на выполнение ф-ции каждые раз будет генерить новое число

# 3.1 присвоить рандомное имя юзеру
# import random
# r = random.randrange(0, 10)
# user = 'User'
# print(user + '_' + str(r)) # лучше не оставлять в print-e конкатинацию или другие вычисления, а обращаться к этим вычислениям через переменную
# поэтому вставляем перед действием print переменную, кот будет включать конкатинацию, а в сам print включаем эту переменную

# import random # сымпортили либу random
# r = random.randrange(0, 10) # получаем рандомное число от 0 до 10 через переменную r
# user = 'User' # создаем имя юзеру в переменной user
# user_random = user + '_' + str(r) # присваиваем имени юзер рандомную цифру (через "_"), чтобы при новой генерации имени, оно отличалось от предыдущего
# print(user_random) # выводим имя юзера, кот мы создали в переменной user_random

# 4 если у нас название файла совпадает с назв-ем библиотеки и значение внутри этого файла совпадает
# необх создать файл в проекте с таким же незв-нием, как и у сущ-щей либы, и функцией или действием внутри этого файла с таким же назв-ем, как у функции в либе
# наприм создадим папку mod и в ней файл math
# import math
# print (math.pi) # эта ф-я вызовет число пи

# from mod import math
# print(math.pi) # эта ф-я вызовет переменную pi из модуля/файла math

# 5 вызов ф-ции из другого модуля

from mod import Modules_2

# Modules_2.sum(10, 5) #создали ф-ю SUM в модуле/файле Modules_2 и обратились к ней из отдельного(вот этого) файла с пом import
# Modules_2.sub(10, 5) #создали ф-ю SUB в модуле/файле Modules_2 и обратились к ней из отдельного(вот этого) файла с пом import

from mod import Modules_2
# print(round(Modules_2.grades_avg_2, 1))
r = Modules_2.grades_avg_2
print(f'Средняя оценка Титовца И: {r}')


























