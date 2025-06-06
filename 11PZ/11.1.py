import random

# Генерация последовательности из 20 целых чисел
sequence = [random.randint(1, 10) for _ in range(20)]
print("Исходная последовательность:", sequence)

# Выбор неповторяющихся элементов
unique_elements = list(set(sequence))
print("Неповторяющиеся элементы:", unique_elements)

# Подсчет количества уникальных элементов
count_unique = len(unique_elements)
print("Количество уникальных элементов:", count_unique)

# Увеличение элементов больше 5 в два раза
processed_elements = [x * 2 if x > 5 else x for x in unique_elements]
print("Обработанные элементы (больше 5 увеличено в 2 раза):", processed_elements)