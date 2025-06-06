#1. В двумериом списке элемеиты последией строки заменить а О.
import random

# Генерация случайного списка из 10 элементов (числа от 1 до 100)
random_list = [random.randint(1, 100) for _ in range(10)]
print("Случайный список:", random_list)

# Замена последних двух элементов на 0
if len(random_list) >= 2:
    random_list[-2:] = [0, 0]
else:
    random_list[:] = [0] * len(random_list)  # Если список короче 2 элементов

print("Список после замены последних двух элементов на 0:", random_list)