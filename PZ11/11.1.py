#1 Средствами языка Руthon сформировать два текстовых файла (.txt), содержащих по 
#Одной последовательности из целых положительных и отрицательных чисел. Сформировать новый 
#текстовый файл (.txt) слелующего вида, предварительно выполнив требуемую обработку элемештов:
# Элементы первого и второго файлов: Средисе арифмстическое элемеитов первого и второго файлов: 
#Количество нечегных элементов первого и второго файлов: 
#Элементы общие для двух файлов: Количество элементов, общцих для двух файлов:
import random

# Функция для генерации случайной последовательности чисел
def generate_sequence(length):
    return [random.randint(-100, 100) for _ in range(length)]

# Функция для записи последовательности в файл
def write_to_file(filename, sequence):
    with open(filename, 'w') as f:
        f.write(' '.join(map(str, sequence)))

# Функция для чтения последовательности из файла
def read_from_file(filename):
    with open(filename, 'r') as f:
        content = f.read()
        return list(map(int, content.split()))

# Генерация и запись последовательностей в файлы
seq1 = generate_sequence(10)
seq2 = generate_sequence(10)
write_to_file('file1.txt', seq1)
write_to_file('file2.txt', seq2)

# Чтение последовательностей из файлов
numbers1 = read_from_file('file1.txt')
numbers2 = read_from_file('file2.txt')

# Вычисление среднего арифметического
avg1 = sum(numbers1) / len(numbers1) if numbers1 else 0
avg2 = sum(numbers2) / len(numbers2) if numbers2 else 0

# Подсчет нечетных элементов
odd_count1 = sum(1 for num in numbers1 if num % 2 != 0)
odd_count2 = sum(1 for num in numbers2 if num % 2 != 0)

# Нахождение общих элементов
common_elements = list(set(numbers1) & set(numbers2))
common_count = len(common_elements)

# Формирование содержимого для нового файла
output_content = f"""Элементы первого и второго файлов:
Первый файл: {numbers1}
Второй файл: {numbers2}

Среднее арифметическое элементов первого и второго файлов:
Первый файл: {avg1:.2f}
Второй файл: {avg2:.2f}

Количество нечетных элементов первого и второго файлов:
Первый файл: {odd_count1}
Второй файл: {odd_count2}

Элементы общие для двух файлов: {common_elements}
Количество элементов, общих для двух файлов: {common_count}
"""

# Запись результатов в новый файл
with open('result.txt', 'w', encoding='utf-8') as f:
    f.write(output_content)

print("Файлы успешно созданы и обработаны. Результаты сохранены в result.txt")