import datetime
from datetime import time

# написать функцию, возвращающую время с полуночи в миллисекундах.
# from datetime import timedelta
#
#
# # def past(h, m, s):
# #     return (3600 * h + 60 * m + s) * 1000
#
#
# def past1(h, m, s):
#     b = timedelta(hours=h, minutes=m, seconds=s) // timedelta(milliseconds=2)
#     return b
#
#
# b = past1(0, 0, 1)
# print(b)


# def pillars(num_pill, dist, width):
#     return dist * 100 * (num_pill - 1) + width * (num_pill - 2) * (num_pill > 1)
#
#
# t1 = pillars(1, 3, 5)
# print(t1)

# def double_char(s):
#     for char in s:
#         b = char * 2
#         # print(b)
#     return b
#
#
# dc = double_char("master")
# print(dc)


# def double_char(s):
#     return ''.join(c * 2 for c in s)
#
# dc = double_char("master")
# print(dc)

# def rev(n):
#     k = ""
# for i in range(5, 1, -1):
#     print(i)

# def hotpo(n):
#     b =
#     while
#         b = n % 2
#         if b == 1:
#             c = 3*n + 1
#             print(c)
#         else:
#             c = n / 2
#             print(c)

# i = 1
# j = 1
# while i < 10:
#     while j < 10:
#         print(i * j, end="\t")
#         j += 1
#     print("\n")
#     j = 1
#     i += 1


# def combined_strs(str1, str2):
#     result = ''
#
#     for ch1, ch2 in zip(str1, str2):
#         if ch1 == '+' and ch2 == '+':
#             result += '+'
#         elif ch1 == '-' and ch2 == '-':
#             result += '-'
#         else:
#             result += '0'
#
#     return result
#
#
# strs = combined_strs('-+-', '+--')
# print(strs)

def count_chars(st1, st2):
    return ''.join('1' if i == j else '0' for i, j in zip(st1, st2))

# def count_chars(st1, st2):
#     result = ''
#     for i in st1:
#         for
#
# strs = count_chars('anton', 'baton')
# print(strs)

# def square_or_square_root(arr):
#     result = []
#     for x in arr:
#         root = x**0.5
#         if root.is_integer():
#             result.append(root)
#         else:
#             result.append(x*x)
#     return result
#
# def process_array(arr):
#     return [int(x**0.5) if (x**0.5).is_integer() else x**2 for x in arr]

# def remove_duplicates(arr):
#     return [x for i, x in enumerate(arr) if x not in arr[:i]]
#
#
# t = remove_duplicates([1, 2, 3, 4, 1, 2, 5, 6])
# print(t)

# def get_average(marks):
#     return []

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
shift = int(input("Type the shift number:\n"))
alphabet1 = []
for i in range(len(alphabet)):
    alphabet1[i] = alphabet[i - shift]
print(alphabet1)