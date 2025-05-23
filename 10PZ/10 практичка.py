book_stores = {
    "Магистр": {"Лермонтов", "Достоевский", "Пушкин", "Тютчев"},
    "ДомКниги": {"Толстой", "Грибоедов", "Чехов", "Пушкин"},
    "БукМаркет": {"Пушкин", "Достоевский", "Маяковский"},
    "Галерея": {"Чехов", "Тютчев", "Пушкин"}
}
target_authors = {"Пушкин", "Тютчев"}
result_stores = []
for store, authors in book_stores.items():
    if target_authors.issubset(authors):
        result_stores.append(store)
if result_stores:
    print("Книги Пушкина и Тютчева можно приобрести в следующих магазинах:")
    for store in result_stores:
        print(f"- {store}")
else:
    print("Нет магазинов, где есть оба автора.")