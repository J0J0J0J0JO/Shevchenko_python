 # 2. Из предложенного текстового файла (text18-28.1x0) вывссти на экран его содержимое, 
 # количество символов в тексте. Сформировать новый файл, в который поместить текст в 
 # стихотворной форме предварительно вставив после строки № (N — залается пользователем) 
 # ироизвольную фразу.
def task2():
    # Чтение исходного файла
    try:
        with open('text18-28.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("Файл text18-28.txt не найден.")
        return
    
    # Вывод содержимого файла
    print("Содержимое файла:")
    print(''.join(lines))
    
    # Подсчет количества символов
    char_count = sum(len(line) for line in lines)
    print(f"\nКоличество символов в тексте: {char_count}")
    
    # Запрос номера строки и фразы у пользователя
    try:
        N = int(input("\nВведите номер строки N для вставки фразы: ")) - 1
        if N < 0 or N >= len(lines):
            print("Некорректный номер строки.")
            return
    except ValueError:
        print("Некорректный ввод номера строки.")
        return
    
    phrase = input("Введите фразу для вставки: ") + '\n'
    
    # Вставка фразы
    lines.insert(N + 1, phrase)
    
    # Сохранение в новый файл
    new_filename = 'modified_text18-28.txt'
    with open(new_filename, 'w', encoding='utf-8') as file:
        file.writelines(lines)
    
    print(f"\nТекст с вставленной фразой сохранен в файл {new_filename}")

# Вызов функции
task2()