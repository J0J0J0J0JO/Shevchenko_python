#С начала суток прошло N секунд (N-целое). Найти количество полных минут, прошедших с начала последнего часа.
N = input("Введите кол-во секунд: ")

while type(N) != int:
    try:
        N = int(N)
    except ValueError:
        print('Неправильно ввели!')
        N = input("Введите кол-во секунд: ")

if N > 0:
    seconds_since = N % 3600
    minutes = seconds_since // 60
print(f"Прошло {minutes} минута с начала последнего часа.")