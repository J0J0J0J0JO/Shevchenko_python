russian_english_dict = {
    "яблоко": "apple",
    "книга": "book",
    "дом": "house",
    "солнце": "sun",
    "вода": "water",
    "кошка": "cat",
    "собака": "dog",
    "машина": "car",
    "город": "city",
    "школа": "school"
}
def translate(word):
    return russian_english_dict.get(word.lower(), "Слово не найдено в словаре")
user_input = input("Введите слово на русском: ")
translation = translate(user_input)
print(f"Перевод: {translation}")