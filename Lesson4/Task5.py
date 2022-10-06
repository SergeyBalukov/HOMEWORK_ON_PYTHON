# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

with open('D:\Python\HOMEWORK_ON_PYTHON\Lesson4\Task5.1.txt', 'r') as file:
   mnog1 = file.read()
   mnog1 = mnog1[0:-4]

with open('D:\Python\HOMEWORK_ON_PYTHON\Lesson4\Task5.2.txt', 'r') as file:
   mnog2 = file.read()

with open('D:\Python\HOMEWORK_ON_PYTHON\Lesson4\Task5.3.txt', 'w', encoding='utf-8') as file:
   file.write(f'{mnog1} + {mnog2}')