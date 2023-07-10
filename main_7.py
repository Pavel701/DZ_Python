poem = input("Введите стихотворение Винни-Пуха: ")
lines = poem.split(" ")
num_syllables = None
rhythm = True

for line in lines:
    words = line.split("-")
    for word in words:
        count = sum(1 for char in word if char.lower() in "а, о, э, и, у, ы, е, ё, ю, я")
        if num_syllables is None:
            num_syllables = count
        elif count != num_syllables:
            rhythm_ok = False
            break

if rhythm:
    print("Парам пам-пам")
else:
    print("Пам парам")
######################################################################################################################
def print_operation_table(operation, num_rows=6, num_columns=6):
    for i in range(1, num_rows + 1):
        for j in range(1, num_columns + 1):
            result = operation(i, j)
            print(result, end="\t")
        print()


def multiply(x, y):
    return x * y

print_operation_table(multiply)
