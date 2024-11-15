#Дан номер месяца целое число в диапазоне 1-12 (1 - январь, 2 - февраль и т. д.). 
# Вывести название соответствующего времени года («зима», «весна», «лето». «осень»).
# Ввод номера месяца
month = int(input("Введите номер месяца (1-12): "))

# Определение времени года и вывод соответствующего сообщения на экран
if month in [12, 1, 2]:
    print("Время года: зима")
elif month in [3, 4, 5]:
    print("Время года: весна")
elif month in [6, 7, 8]:
    print("Время года: лето")
elif month in [9, 10, 11]:
    print("Время года: осень")
else:
    print("Ошибка ввода номера месяца")