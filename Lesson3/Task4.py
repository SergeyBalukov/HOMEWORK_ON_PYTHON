# Задача №25: Напишите программу, которая будет преобразовывать десятичное число в двоичное. Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10


# s = ""
# n = int(input("Введите число для преобразовывания десятичного числа в двоичное:\n"))
# while n != 0:
#     s = str(n%2) + s
#     n //=2
# print(s)

n = int(input())
print('{0:b}'.format(n))