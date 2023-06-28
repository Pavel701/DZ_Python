# Ввод количества элементов для двух множеств
n = int(input("Введите количество элементов первого множества: "))
m = int(input("Введите количество элементов второго множества: "))

set1 = set()
set2 = set()

# Ввод элементов первого множества
print("Введите элементы первого множества:")
for i in range(n):
    element = int(input())
    set1.add(element)

# Ввод элементов второго множества
print("Введите элементы второго множества:")
for i in range(m):
    element = int(input())
    set2.add(element)

# Находим общие элементы
common = sorted(list(set1.intersection(set2)))

# Выводим результат
print("Общие элементы, встречающиеся в обоих множествах, в порядке возрастания:")
for element in common:
    print(element)
