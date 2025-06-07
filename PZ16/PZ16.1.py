#Создайте класс «Счетчик», который имеет атрибут текущего значения и методы для
#инкремента и декремента значения. код python
class Counter:
    def __init__(self, initial_value=0):
        self.value = initial_value

    def increment(self, step=1):
        """Увеличивает значение счетчика на заданный шаг (по умолчанию на 1)."""
        self.value += step

    def decrement(self, step=1):
        """Уменьшает значение счетчика на заданный шаг (по умолчанию на 1)."""
        self.value -= step

    def get_value(self):
        """Возвращает текущее значение счетчика."""
        return self.value

    def reset(self, new_value=0):
        """Сбрасывает счетчик к заданному значению (по умолчанию к 0)."""
        self.value = new_value


# Пример использования
if __name__ == "__main__":
    counter = Counter()  # Создаем счетчик с начальным значением 0
    print("Начальное значение:", counter.get_value())

    counter.increment()  # Увеличиваем на 1
    print("После инкремента:", counter.get_value())

    counter.increment(3)  # Увеличиваем на 3
    print("После инкремента на 3:", counter.get_value())

    counter.decrement(2)  # Уменьшаем на 2
    print("После декремента на 2:", counter.get_value())

    counter.reset(10)  # Сбрасываем на 10
    print("После сброса на 10:", counter.get_value())