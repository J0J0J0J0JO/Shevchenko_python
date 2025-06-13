#Приложение ПАРИКМАХЕРСКАЯ для некоторой организации. 
#БД должна содержать таблицу Услуги со следующей структурой записи: 
#ФИО мастера, ФИО клиента, пол, пазвание стрижки, стоимость.
import sqlite3
from typing import List, Dict, Optional

class BarberShopDB:
    def __init__(self, db_name: str = 'barbershop.db'):
        self.db_name = db_name
        self._initialize_db()

    def _initialize_db(self):
        """Инициализация базы данных и создание таблицы, если её нет"""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS services (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    master_name TEXT NOT NULL,
                    client_name TEXT NOT NULL,
                    client_gender TEXT NOT NULL,
                    haircut_name TEXT NOT NULL,
                    price REAL NOT NULL,
                    service_date TEXT DEFAULT CURRENT_DATE
                )
            ''')
            conn.commit()

    def add_service(self, master_name: str, client_name: str, client_gender: str, 
                    haircut_name: str, price: float) -> int:
        """Добавление новой услуги"""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO services (master_name, client_name, client_gender, haircut_name, price)
                VALUES (?, ?, ?, ?, ?)
            ''', (master_name, client_name, client_gender, haircut_name, price))
            conn.commit()
            return cursor.lastrowid

    def get_all_services(self) -> List[Dict]:
        """Получить список всех услуг"""
        with sqlite3.connect(self.db_name) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM services ORDER BY service_date DESC')
            return [dict(row) for row in cursor.fetchall()]

    def get_services_by_master(self, master_name: str) -> List[Dict]:
        """Получить услуги по конкретному мастеру"""
        with sqlite3.connect(self.db_name) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute('''
                SELECT * FROM services 
                WHERE master_name = ? 
                ORDER BY service_date DESC
            ''', (master_name,))
            return [dict(row) for row in cursor.fetchall()]

    def get_services_by_client(self, client_name: str) -> List[Dict]:
        """Получить услуги по конкретному клиенту"""
        with sqlite3.connect(self.db_name) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute('''
                SELECT * FROM services 
                WHERE client_name = ? 
                ORDER BY service_date DESC
            ''', (client_name,))
            return [dict(row) for row in cursor.fetchall()]

    def get_services_by_gender(self, gender: str) -> List[Dict]:
        """Получить услуги по полу клиента"""
        with sqlite3.connect(self.db_name) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute('''
                SELECT * FROM services 
                WHERE client_gender = ? 
                ORDER BY service_date DESC
            ''', (gender,))
            return [dict(row) for row in cursor.fetchall()]

    def get_total_revenue(self) -> float:
        """Получить общую выручку"""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT SUM(price) FROM services')
            return cursor.fetchone()[0] or 0.0

    def get_master_revenue(self, master_name: str) -> float:
        """Получить выручку по конкретному мастеру"""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT SUM(price) FROM services WHERE master_name = ?', (master_name,))
            return cursor.fetchone()[0] or 0.0
def delete_service(self, service_id: int) -> bool:
        """Удалить услугу"""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM services WHERE id = ?', (service_id,))
            conn.commit()
            return cursor.rowcount > 0


def display_menu():
    """Отображение меню приложения"""
    print("\nПарикмахерская - система учета услуг")
    print("1. Добавить новую услугу")
    print("2. Просмотреть все услуги")
    print("3. Просмотреть услуги по мастеру")
    print("4. Просмотреть услуги по клиенту")
    print("5. Просмотреть услуги по полу клиента")
    print("6. Показать общую выручку")
    print("7. Показать выручку по мастеру")
    print("8. Удалить услугу")
    print("9. Выход")


def display_services(services: List[Dict]):
    """Отображение списка услуг"""
    if not services:
        print("Нет услуг для отображения.")
        return
    
    print("\nСписок услуг:")
    print("-" * 120)
    print(f"{'ID':<5} | {'Мастер':<20} | {'Клиент':<20} | {'Пол':<6} | {'Стрижка':<30} | {'Цена':<10} | {'Дата':<10}")
    print("-" * 120)
    
    for service in services:
        print(f"{service['id']:<5} | {service['master_name']:<20} | {service['client_name']:<20} | "
              f"{service['client_gender']:<6} | {service['haircut_name'][:28]:<30} | "
              f"{service['price']:<10.2f} | {service['service_date']:<10}")
    print("-" * 120)


def main():
    db = BarberShopDB()
    
    while True:
        display_menu()
        choice = input("Выберите действие: ")
        
        if choice == '1':
            # Добавление новой услуги
            master_name = input("ФИО мастера: ")
            client_name = input("ФИО клиента: ")
            client_gender = input("Пол клиента (м/ж): ").lower()
            haircut_name = input("Название стрижки/услуги: ")
            price = float(input("Стоимость услуги: "))
            
            try:
                service_id = db.add_service(master_name, client_name, client_gender, haircut_name, price)
                print(f"Услуга успешно добавлена с ID {service_id}")
            except Exception as e:
                print(f"Ошибка при добавлении услуги: {e}")
        
        elif choice == '2':
            # Просмотр всех услуг
            services = db.get_all_services()
            display_services(services)
        
        elif choice == '3':
            # Просмотр услуг по мастеру
            master_name = input("Введите ФИО мастера: ")
            services = db.get_services_by_master(master_name)
            display_services(services)
        
        elif choice == '4':
            # Просмотр услуг по клиенту
            client_name = input("Введите ФИО клиента: ")
            services = db.get_services_by_client(client_name)
            display_services(services)
        
        elif choice == '5':
            # Просмотр услуг по полу клиента
            gender = input("Введите пол клиента (м/ж): ").lower()
            services = db.get_services_by_gender(gender)
            display_services(services)
        
        elif choice == '6':
            # Общая выручка
            total = db.get_total_revenue()
            print(f"\nОбщая выручка: {total:.2f} руб.")
        
        elif choice == '7':
            # Выручка по мастеру
            master_name = input("Введите ФИО мастера: ")
            revenue = db.get_master_revenue(master_name)
            print(f"\nВыручка мастера {master_name}: {revenue:.2f} руб.")
        
        elif choice == '8':
            # Удаление услуги
            service_id = input("Введите ID услуги для удаления: ")
            try:
                if db.delete_service(int(service_id)):
                    print("Услуга успешно удалена")
                else:
                    print("Услуга с таким ID не найдена")
            except ValueError:
                print("Неверный формат ID")
        
        elif choice == '9':
            # Выход
            print("Выход из программы")
            break
        
        else:
             print("Неверный выбор. Пожалуйста, выберите действие от 1 до 9.")


if __name__ == "__main__":
    main()
