# Составить программу, в которой функция генерирует четырехзначное 
# число и определяет, есть ли в числе одинаковые цифры.
import random

def check_duplicate_digits():
   
    number = random.randint(1000, 9999)
    print(f"Сгенерированное число: {number}")

    digits_set = set(range(10))
    temp_number = number

    while temp_number > 0:
        digit = temp_number % 10
        if digit in digits_set:
            print(f"Число {number} содержит одинаковые цифры.")
            return True
        else:
            digits_set.add(digit) 
        temp_number //= 10

    print(f"Число {number} не содержит одинаковых цифр.")
    return False

check_duplicate_digits()
