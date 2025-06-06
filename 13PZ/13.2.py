# 2. В двумерном списке элементы столбца № 
# (№ залать с клавиатуры) увеличить в два раза.
import random

# Генерация нового случайного списка
random_list = [random.randint(1, 50) for _ in range(8)]
print("\nНовый случайный список:", random_list)

# Выбор случайной позиции N
n = random.randint(0, len(random_list) - 1)
print(f"Выбрана случайная позиция N = {n} (элемент = {random_list[n]})")

# Увеличение элемента в позиции N в два раза
random_list[n] *= 2
print(f"Элемент на позиции {n} увеличен в два раза: {random_list[n]}")
print("Список после изменения:", random_list)