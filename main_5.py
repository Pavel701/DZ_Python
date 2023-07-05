input_string = input('Введите строку: ')
compress_string = ""
count = 1

for i in range(len(input_string)):
    if i < len(input_string) - 1 and input_string[i] == input_string[i+1]:
        count += 1
    else:
        if count == 1:
            compress_string += input_string[i]
        else:
            compress_string += str(count) + input_string[i]
            count = 1

print(compress_string)

##################################################################################################
import random

# Создаем список из случайных чисел
numbers = random.sample(range(1, 101), 10)

# Находим номер последнего локального максимума
last_local_max_index = -1
for i in range(1, len(numbers)-1):
    if numbers[i] > numbers[i-1] and numbers[i] > numbers[i+1]:
        last_local_max_index = i

# Выводим список и номер последнего локального максимума
print("Список чисел:", numbers)
if last_local_max_index != -1:
    print("Номер последнего локального максимума:", last_local_max_index)
else:
    print("Локальный максимум не найден")

######################################################################################################

import random

# Создаем список из случайных чисел
numbers = [random.randint(1, 10) for _ in range(20)]

# Создаем словарь для подсчета количества каждого элемента
count_dict = {}

# Подсчитываем количество каждого элемента
for num in numbers:
    if num in count_dict:
        count_dict[num] += 1
    else:
        count_dict[num] = 1

# Находим максимальное количество одинаковых элементов
max_count = max(count_dict.values())

print("Список чисел:", numbers)
print("Максимальное количество одинаковых элементов:", max_count)
###############################################################################################################

import random

# Создаем список из случайных чисел
numbers = [random.randint(1, 100) for _ in range(10)]

# Находим максимальное и второе максимальное значение в списке
max_value = max(numbers)
second_max_value = max([num for num in numbers if num != max_value])

print("Список чисел:", numbers)
print("Первый максимум:", max_value)
print("Второй максимум:", second_max_value)

###########################################################################################################

