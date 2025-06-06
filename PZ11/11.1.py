#1. Средствами языка Python сформировать два текстовых файла (.txt), 
# содержащих по Одной последовательности из целых положительных и отрицательных чисел. 
# Сформировать новый текстовый файл (.txt) слелующего вида, прелварительно выполнив 
# требуемую обработку Элементов:
# Элементы первого и второго файлов: Средисе арифметическое элементов первого и второго файлов: 
# Количество нечетных элементов первого и второго файлов: Элементы общие для двух файлов: 
# Количество элементов, общцих для двух файлов:
import random

def generate_random_numbers(count=10, min_num=-100, max_num=100):
    """Генерация случайных чисел (положительных и отрицательных)"""
    return [random.randint(min_num, max_num) for _ in range(count)]

def write_numbers_to_file(filename, numbers):
    """Запись чисел в файл"""
    with open(filename, 'w') as f:
        f.write(' '.join(map(str, numbers)))

def read_numbers_from_file(filename):
    """Чтение чисел из файла"""
    with open(filename) as f:
        return list(map(int, f.read().split()))

# 1. Создаем два файла с числами
numbers1 = generate_random_numbers()
numbers2 = generate_random_numbers()
write_numbers_to_file('file1.txt', numbers1)
write_numbers_to_file('file2.txt', numbers2)

# 2. Читаем числа из файлов
nums1 = read_numbers_from_file('file1.txt')
nums2 = read_numbers_from_file('file2.txt')

# 3. Выполняем обработку
avg1 = sum(nums1) / len(nums1) if nums1 else 0
avg2 = sum(nums2) / len(nums2) if nums2 else 0
odd_count1 = sum(1 for num in nums1 if num % 2 != 0)
odd_count2 = sum(1 for num in nums2 if num % 2 != 0)
common_elements = list(set(nums1) & set(nums2))
common_count = len(common_elements)

# 4. Записываем результат в новый файл
with open('result.txt', 'w', encoding='utf-8') as f:
    f.write(f"Элементы первого и второго файлов:\n{nums1}\n{nums2}\n\n")
    f.write(f"Среднее арифметическое элементов:\nПервый файл: {avg1:.2f}\nВторой файл: {avg2:.2f}\n\n")
    f.write(f"Количество нечетных элементов:\nПервый файл: {odd_count1}\nВторой файл: {odd_count2}\n\n")
    f.write(f"Элементы общие для двух файлов:\n{common_elements}\n\n")
    f.write(f"Количество элементов, общих для двух файлов: {common_count}\n")

print("Результат записан в файл result.txt")