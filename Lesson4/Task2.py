# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# n = int(input('Введите число -> '))
# my_lst = [n]

# def prosto(my_lst):
#     fl = 0
#     for i in range(my_lst[-1] // 2, 1, -1):
#         if my_lst[len(my_lst)-1] % i == 0:
#             my_lst.append(i)
#             my_lst[-2] = my_lst[-2] // i              
#             fl += 1

#     if fl != 0:
#         prosto(my_lst)

# prosto(my_lst)
    
# print(my_lst)


num = int(input("Введите число: "))
i = 2 # первое простое число
lst = []
old = num
while i <= num:
    if num % i == 0:
        lst.append(i)
        num //= i
        i = 2
    else:
        i += 1
print(f"Простые множители числа {old} приведены в списке: {lst}")