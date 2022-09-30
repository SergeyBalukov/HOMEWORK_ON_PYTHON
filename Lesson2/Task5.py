#Реализуйте алгоритм перемешивания списка.(Без использования библиотеки random)
def listSort(n):
    for i in range(len(n) // 2):
        helpVar = n[i]
        n[i] = n[-i - 1]
        n[-i - 1] = helpVar

n = ['1', '2', '3', '4', '5', '6', '7']
listSort(n)
print(n)           