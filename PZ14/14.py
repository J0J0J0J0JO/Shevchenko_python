#В исходиом текстовом файлс(datcs.tx) найти все даты в форматах ДД.ММ.ГГГГ и ДДММ/ГГГ. 
#Посчитать количество дат в каждом формате. Поместить в новый текстовый файл 
#все даты февраля в формате ДДММЛГГГ
import re
from datetime import datetime

def extract_and_process_dates(input_file, output_file):
    # Чтение исходного файла
    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()

    # Регулярные выражения для поиска дат
    pattern_dot = re.compile(r'\b\d{2}\.\d{2}\.\d{4}\b')  # ДД.ММ.ГГГГ
    pattern_slash = re.compile(r'\b\d{2}/\d{2}/\d{4}\b')  # ДД/ММ/ГГГГ

    # Поиск всех дат
    dates_dot = pattern_dot.findall(content)
    dates_slash = pattern_slash.findall(content)

    # Подсчет количества дат каждого формата
    count_dot = len(dates_dot)
    count_slash = len(dates_slash)

    # Сбор всех дат февраля
    feb_dates = []

    # Проверка дат формата ДД.ММ.ГГГГ
    for date_str in dates_dot:
        try:
            date = datetime.strptime(date_str, '%d.%m.%Y')
            if date.month == 2:
                feb_dates.append(date.strftime('%d%m%Y'))
        except ValueError:
            continue

    # Проверка дат формата ДД/ММ/ГГГГ
    for date_str in dates_slash:
        try:
            date = datetime.strptime(date_str, '%d/%m/%Y')
            if date.month == 2:
                feb_dates.append(date.strftime('%d%m%Y'))
        except ValueError:
            continue

    # Запись результатов в новый файл
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(f"Количество дат в формате ДД.ММ.ГГГГ: {count_dot}\n")
        file.write(f"Количество дат в формате ДД/ММ/ГГГГ: {count_slash}\n\n")
        file.write("Даты февраля в формате ДДММГГГГ:\n")
        for date in feb_dates:
            file.write(date + '\n')

    print(f"Обработка завершена. Результаты сохранены в {output_file}")

# Использование функции
extract_and_process_dates('data.txt', 'february_dates.txt')