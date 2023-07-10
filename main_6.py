n = int(input("Введите количество элементов: "))
a1 = int(input("Введите первый элемент: "))
d = int(input("Введите разность: "))

array = []
for i in range(n):
    element = a1 + (i * d)
    array.append(element)

print(array)
###############################################################################################

array = [1, 5, 3, 7, 9, 2, 4, 6, 8]
minimum = 3
maximum = 7

indexes = []
for i in range(len(array)):
    if minimum <= array[i] <= maximum:
        indexes.append(i)

print(indexes)