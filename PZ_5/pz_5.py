# Составить программу, в которой функция генерирует четырехзначное число и 
# определяет, есть ли в числе одинаковые цифры.
def has_duplicate_digits(number):
    num_str = str(number)
    seen_digits = set()
    
    for digit in num_str:
        if digit in seen_digits:
            return True
        seen_digits.add(digit)
    
    return False

def main(number):   
    if has_duplicate_digits(number):
        print("В числе есть одинаковые цифры.")
    else:
        print("В числе нет одинаковых цифр.")
user_input = input('Введите число: ')
while type(user_input) != int:
    try:
        user_input = int(user_input)
    except ValueError:
        print('Вы ввели не число!')
        user_input = input('Введите число: ')
main(user_input)
