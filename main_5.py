# input_string = input('Введите строку: ')
# compress_string = ""
# count = 1
#
# for i in range(len(input_string)):
#     # Проверяем, если текущий символ равен следующему символу
#     if i < len(input_string) - 1 and input_string[i] == input_string[i+1]:
#         count += 1
#     else:
#         # Если символ не повторяется, добавляем его в сжатую строку
#         if count == 1:
#             compress_string += input_string[i]
#         else:
#             compress_string += str(count) + input_string[i]
#             count = 1
#
# print(compress_string)  # Вывод: a2bc3a

##################################################################################################
# import random
#
# # Создаем список из случайных чисел
# numbers = [random.randint(1, 100) for _ in range(10)]
#
# # Находим номер последнего локального максимума
# last_local_max_index = -1
#
# for i in range(1, len(numbers) - 1):
#     if numbers[i] > numbers[i-1] and numbers[i] > numbers[i+1]:
#         last_local_max_index = i
#
# print("Список чисел:", numbers)
# print("Номер последнего локального максимума:", last_local_max_index)

######################################################################################################

# import random
#
# # Создаем список из случайных чисел
# numbers = [random.randint(1, 10) for _ in range(20)]
#
# # Создаем словарь для подсчета количества каждого элемента
# count_dict = {}
#
# # Подсчитываем количество каждого элемента
# for num in numbers:
#     if num in count_dict:
#         count_dict[num] += 1
#     else:
#         count_dict[num] = 1
#
# # Находим максимальное количество одинаковых элементов
# max_count = max(count_dict.values())
#
# print("Список чисел:", numbers)
# print("Максимальное количество одинаковых элементов:", max_count)
# ###############################################################################################################

# import random
#
# # Создаем список из случайных чисел
# numbers = [random.randint(1, 100) for _ in range(10)]
#
# # Находим максимальное и второе максимальное значение в списке
# max_value = max(numbers)
# second_max_value = max([num for num in numbers if num != max_value])
#
# print("Список чисел:", numbers)
# print("Первый максимум:", max_value)
# print("Второй максимум:", second_max_value)

###########################################################################################################

