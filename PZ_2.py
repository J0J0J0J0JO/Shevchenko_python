#С начала суток прошло N секунд (N-целое). Найти количество полных минут, прошедших с начала последнего часа.
N = input("Введите кол-во секунд: ")

while type(N) != int:
    try:
        N = int(N)
    except ValueError:
        print('Неправильно ввели!')
        N = input("Введите кол-во секунд: ")

if N > 0:
    seconds_since_last_hour = N % 3600
    full_minutes_since_last_hour = seconds_since_last_hour // 60
print(f"Прошло {full_minutes_since_last_hour} минуты с начала последнего часа.")