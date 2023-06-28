n = int(input("Введите количество элементов в массиве: "))
array = []
for _ in range(n):
    num = int(input("Введите число: "))
    array.append(num)
x = int(input("Введите число X: "))

# Вычисление количества вхождений числа X в массиве
count = 0
for num in array:
    if num == x:
        count += 1

# Вывод результата
print(f"Число {x} встречается в массиве: {count} раз.")
#######################################################################################

n = int(input("Введите количество элементов в массиве: "))
array = []
for _ in range(n):
    num = int(input("Введите число: "))
    array.append(num)
x = int(input("Введите число X: "))

# Нахождение самого близкого элемента
closest = None
min_diff = float('inf')
for num in array:
    diff = abs(num - x)
    if diff < min_diff:
        min_diff = diff
        closest = num

# Вывод результата
print(f"Самый близкий элемент к числу {x} в массиве: {closest}")
