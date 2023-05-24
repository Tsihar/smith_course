# num_1 = float(input("Введите первое число:\n"))
# action = input("Введите одно из 4х математических действий: '/', '*', '+', '-'\n")
# num_2 = float(input("Введите второе число:\n"))
#
# if action == "+":
#     result_1 = num_1 + num_2
#     print(f'Результат: {float(result_1)}')
# elif action == "-":
#     result_2 = num_1 - num_2
#     print(f'Результат: {float(result_2)}')
# elif action == "*":
#     result_3 = num_1 * num_2
#     print(f'Результат: {float(result_3)}')
# elif action == "/":
#     try:
#         result_4 = num_1 / num_2
#         print(f'Результат: {float(result_4)}')
#     except ZeroDivisionError:
#         print('Результат: На 0 делить нельзя')
# else:
#     print("Неверно указано математическое действие.")

num_1 = float(input("Введите первое число:\n"))
action = input("Введите одно из 4х математических действий: '/', '*', '+', '-'\n")
num_2 = float(input("Введите второе число:\n"))

if action == "+":
    result_sum = num_1 + num_2
    print(f'Результат: {result_sum}')
elif action == "-":
    result_sub = num_1 - num_2
    print(f'Результат: {result_sub}')
elif action == "*":
    result_mult = num_1 * num_2
    print(f'Результат: {result_mult}')
elif action == "/":
    try:
        result_div = num_1 / num_2
        print(f'Результат: {result_div}')
    except ZeroDivisionError:
        print('Результат: На 0 делить нельзя')
else:
    print("Неверно указано математическое действие.")