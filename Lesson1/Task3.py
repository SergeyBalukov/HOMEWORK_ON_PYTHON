# Задание 3. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
a = int(input('Введите номер четверти: '))
if a < 1 or a > 4:
    print('Ошибка! Введите номер четверти от 1 до 4')
elif a == 1:
    print('x > 0 и y > 0')
elif a == 2:
    print('x < 0 и y > 0')
elif a == 3:
    print('x < 0 и y < 0')
elif a == 4:
    print('x > 0 и y < 0')
