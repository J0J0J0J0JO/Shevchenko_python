#Создайте класс "Животное", который содержит информацию о виде и возрасте
#животного. Создайте классы "Собака" и "Кошка", которые наследуются от класса
#"Животное" и содержат информацию о породе.
class Animal:
    def __init__(self, species, age):
        self.species = species
        self.age = age

    def get_info(self):
        return f"{self.species}, {self.age} лет"


class Dog(Animal):
    def __init__(self, age, breed):
        super().__init__("Собака", age)
        self.breed = breed

    def get_info(self):
        return f"{super().get_info()}, порода: {self.breed}"


class Cat(Animal):
    def __init__(self, age, breed):
        super().__init__("Кошка", age)
        self.breed = breed

    def get_info(self):
        return f"{super().get_info()}, порода: {self.breed}"


dog = Dog(5, "Лабрадор")
cat = Cat(7, "Британская")
print(dog.get_info())
print(cat.get_info())
