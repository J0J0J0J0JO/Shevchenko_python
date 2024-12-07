# Дан список A размера N. Найти минимальный элемент из его элементов с четными
# номерами: A2, A4, A6, ... .
import random

try:
    while True:
        n = int(input("Введите длину списка: "))
        if n < 0:
            print("Длина списка не может быть отрицательная!")
            continue
        break

    a = [random.randint(1, 99) for _ in range(n)]

    print("Сгенерированный список A:", a)

    even_indexed_elements = a[1::2]
    if even_indexed_elements:
        min_element = min(even_indexed_elements)
        print("Минимальный элемент с четными индексами:", min_element)
    else:
        print("Нет элементов с четными индексами.")
except ValueError:
    print("Ошибка при вводе данных!")
