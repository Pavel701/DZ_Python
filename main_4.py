Ввод количества элементов для двух множеств
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

######################################################################################################################
n = int(input("Введите число кустов черники: "))

bushes = []
for i in range(n):
    berries = int(input("Введите количество ягод на кусте {}: ".format(i+1)))
    bushes.append(berries)

max_berries = 0

for i in range(n):
    curr_bush = bushes[i]
    left_bush = bushes[(i-1) % n]
    right_bush = bushes[(i+1) % n]

    total_berries = curr_bush + left_bush + right_bush
    max_berries = max(max_berries, total_berries)

print("Максимальное количество ягод:", max_berries)


