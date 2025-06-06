# 2. Составить генератор (yield), который переведет 
# символы строки из верхнего регистра в нижний.
def lower_case_generator(input_string):
    for char in input_string:
        yield char.lower()

# Пример использования генератора
test_string = "Hello World! ПРИВЕТ МИР!"
print("Исходная строка:", test_string)

print("Результат работы генератора:")
for char in lower_case_generator(test_string):
    print(char, end='')

# Альтернативный вариант с преобразованием всей строки
result_string = ''.join([char for char in lower_case_generator(test_string)])
print("\nРезультат в виде строки:", result_string)