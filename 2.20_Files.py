#1 из определенного файла мы можем брать список и делать с нима что угодно
# fw = open('doc/file.txt', 'a')
# ф-я open открывает файл, но если его нет, то создает
# в ковычках указываем:
# > имя директории (doc)
# > через '/' дальнейшие директории и в конце сам файл
# в конце ф-ции open через ',' мы будем указывать параметр(мод), что именно мы делаем с файлом
# мод а - запись новых данных в файл и дозаписывать к-л информацию в конец файла
# fw.write("Hello world") # к переменной fw мы применяем ф-ю write и зн-ние которое мы хоти поместить в файл
# fw.close() # закрываем файл

#2 если несколько раз выполнить этот код, то значение из функции write будет записываться в конец файла

#3
# fw = open('doc/file.txt', 'a')
# fw.write("Hello world\n") # \n опция означает перенос на след строку зн-ния при выполнении кода
# fw.close()

#4 через input записывает введенное значение в конец файла
# var = input('Напиши что нить: ')
# fw = open('doc/file.txt', 'a')
# fw.write(var)
# fw.close()

#5 мод 'w' - запись новых данных, но с удалением старых данных
# fw = open('doc/file2.txt', 'w')
# fw.write("privet")
# fw.close()

#6 как читать данные с файлов - мод 'r'
fr = open('doc/file.txt', 'r')
text = fr.read() # эта переменная будет хранить содержимое файла
fr.close()
print(text)

# Поигрался
# razrabotka = {'102510':23, '102520':24, '102530':27, '102540':32}
#
# # for g, q in razrabotka.items():
# print(sum(razrabotka.values())) - сумма значений всего словаря
#
# for g, q in razrabotka.items():
#     if g == '102510':
#         print()
