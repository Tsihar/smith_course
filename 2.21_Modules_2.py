# def sum(a, b):
#     result = a + b
#     print('Результат сложения: ' + str(result))
#
#
# def sub(a, b):
#     result = a - b
#     print('Результат вычитания: ' + str(result))

# grades = {'math': 9, 'russian': 8, 'belarusian': 8, 'chemistry': 9}

import statistics # эта либа содержит ф-цию mean, которая вычисляет среднее арифметическое из объектов списка

mat = int(input('Введите оценку ученика по математике:\n'))
rus = int(input('Введите оценку ученика по русскому языку:\n'))
bel = int(input('Введите оценку ученика по белорусскому языку:\n'))
chem = int(input('Введите оценку ученика по химии:\n'))

grades = {'math': mat, 'russian': rus, 'belarusian': bel, 'chemistry': chem}
gradeslist = list(grades.values())  # из значений словаря сделали список при помощи конструктора list() и метода values()
# grades_avg_1 = sum(gradeslist)/len(gradeslist) # 1й способ посчитать сред арифм списка
# print(grades_avg) # 1й способ посчитать сред арифм списка
grades_avg_2 = statistics.mean(gradeslist)# 2й способ посчитать сред арифм списка
# ф-ция mean, вычисляет среднее арифметическое из объектов списка
print(grades_avg_2) # 2й способ посчитать сред арифм списка



