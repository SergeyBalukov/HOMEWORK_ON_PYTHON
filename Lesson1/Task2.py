# Задание 2. Напишите программу, которая принимает на вход координаты точки (X и Y), 
# и выдаёт номер четверти плоскости, в которой находится эта точка 
# (или на какой оси она находится).
# Пример:
# x=34; y=-30 -> 4
# x=2; y=4-> 1
# x=-34; y=-30 -> 3

x = int(input('Введите число x: '))
y = int(input('Введите число y: '))
if x > 0 and y >0:
    print('I четверть')
if x < 0 and y > 0:
    print('II четверть')
if x < 0 and y < 0:
    print('III четверть')
if x > 0 and y < 0:
    print('IV четверть') 
else:
     x == 0 and y == 0
print('Укажите число < или > 0')

