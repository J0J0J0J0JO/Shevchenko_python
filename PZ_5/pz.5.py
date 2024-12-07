# Составить программу, в которой функция генерирует четырехзначное 
# число и определяет, есть ли в числе одинаковые цифры.
import random

def check_duplicate_digits():
    # Генерация случайного 4-значного числа
    number = random.randint(1000, 9999)
    
    # Преобразуем число в строку для удобства работы с цифрами
    str_number = str(number)
    
    # Проверка наличия одинаковых цифр
    digits_set = set()
    for digit in str_number:
        if digit in digits_set:
            print(f"Число {number} содержит одинаковые цифры.")
            return True
        else:
            digits_set.add(digit)
            
    print(f"Число {number} не содержит одинаковых цифр.")
    return False

check_duplicate_digits()