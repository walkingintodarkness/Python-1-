if __name__ == "__main__":
    class Animal:
        """
        Базовый класс для животных.
        Атрибуты:
            name (str): имя животного
            age (int): возраст
            _species (str): вид животного (защищенный, так как используется внутри иерархии)
        """
        def __init__(self, name: str, age: int, species: str) -> None:
            """
            Конструктор класса Animal.
            :param name: имя
            :param age: возраст
            :param species: вид
            """
            self.name = name
            self.age = age
            self._species = species

        def __str__(self) -> str:
            """Возвращает удобочитаемое строковое представление."""
            return f"{self.name} ({self.age} лет) - {self._species}"

        def __repr__(self) -> str:
            """Возвращает формальное строковое представление для отладки."""
            return f"Animal(name='{self.name}', age={self.age}, species='{self._species}')"

        def move(self) -> str:
            """Метод, описывающий движение животного."""
            return f"{self.name} двигается."

        def speak(self) -> str:
            """Метод, издающий звук животного. По умолчанию возвращает общую фразу."""
            return f"{self.name} издает звук."

    class Dog(Animal):
        """
        Класс собаки, наследник Animal.
        Добавляет атрибут породы.
        Переопределяет методы speak, __str__, __repr__.
        Наследует метод move без изменений.
        """
        def __init__(self, name: str, age: int, breed: str) -> None:
            """
            Конструктор класса Dog.
            :param name: имя
            :param age: возраст
            :param breed: порода
            """

            super().__init__(name, age, species="Canis familiaris")
            self._breed = breed

        def __str__(self) -> str:
            """Переопределяем для включения породы."""
            return f"{self.name} (собака, {self.age} лет, порода: {self._breed})"

        def __repr__(self) -> str:
            """Переопределяем для отладки."""
            return f"Dog(name='{self.name}', age={self.age}, breed='{self._breed}')"

        def speak(self) -> str:
            """
            Переопределенный метод издания звука.
            Причина переопределения: собаки лают, а не издают общий звук.
            """
            return f"{self.name} лает: Гав!"


    animal = Animal("Кеша", 3, "Попугай")
    dog = Dog("Бобик", 5, "Такса")

    print(animal)
    print(repr(animal))
    print(animal.move())
    print(animal.speak())
    print()
    print(dog)
    print(repr(dog))
    print(dog.move())
    print(dog.speak())
