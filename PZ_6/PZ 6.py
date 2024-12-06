# Дан список A размера N. Найти минимальный элемент из его элементов с четными
# номерами: A2, A4, A6, ... .
import random

n = input('Введите длину списка: ')
while type(n) != int:
    try:
        n = int(n)
    except ValueError:
        print('Вы ввели неккоректное число!')
        n = input('Введите длину списка: ')
a = [random.randint(1, 99) for _ in range(n)]

print("Сгенерированный список A:", a)

even_indexed_elements = a[1::2]
if even_indexed_elements:
    min_element = min(even_indexed_elements)
    print("Минимальный элемент с четными индексами:", min_element)
else:
    print("Нет элементов с четными индексами.")
