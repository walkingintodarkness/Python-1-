import doctest

# TODO Написать 3 класса с документацией и аннотацией типов

class Book:

    def __init__(self, title: str, author: str, pages: int):

        if not isinstance(title, str):
            raise TypeError("Название книги должно быть типа str")
        if not title:
            raise ValueError("Название книги не может быть пустым")
        self.title = title

        if not isinstance(author, str):
            raise TypeError("Автор книги должен быть типа str")
        if not author:
            raise ValueError("Автор книги не может быть пустым")
        self.author = author

        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self.pages = pages

    def is_thick_book(self) -> bool:

        return self.pages > 500

    def get_book_info(self) -> str:

        return f'Книга "{self.title}", автор: {self.author}, страниц: {self.pages}'

    def read_pages(self, pages_to_read: int) -> None:

        if not isinstance(pages_to_read, int):
            raise TypeError("Количество страниц для чтения должно быть типа int")
        if pages_to_read < 0:
            raise ValueError("Количество страниц для чтения не может быть отрицательным")
        # В реальной реализации здесь была бы логика отслеживания прочитанных страниц


class Car:


    def __init__(self, brand: str, model: str, fuel_level: float = 0.0):

        if not isinstance(brand, str):
            raise TypeError("Марка автомобиля должна быть типа str")
        if not brand:
            raise ValueError("Марка автомобиля не может быть пустой")
        self.brand = brand

        if not isinstance(model, str):
            raise TypeError("Модель автомобиля должна быть типа str")
        if not model:
            raise ValueError("Модель автомобиля не может быть пустой")
        self.model = model

        if not isinstance(fuel_level, (int, float)):
            raise TypeError("Уровень топлива должен быть типа int или float")
        if fuel_level < 0:
            raise ValueError("Уровень топлива не может быть отрицательным")
        self.fuel_level = float(fuel_level)

    def is_tank_empty(self) -> bool:

        return self.fuel_level < 5.0

    def refuel(self, fuel_amount: float) -> None:

        if not isinstance(fuel_amount, (int, float)):
            raise TypeError("Количество топлива должно быть типа int или float")
        if fuel_amount < 0:
            raise ValueError("Количество топлива не может быть отрицательным")
        self.fuel_level += fuel_amount

    def get_car_info(self) -> str:

        return f'Автомобиль {self.brand} {self.model}, топлива: {self.fuel_level} л'


class BankAccount:


    def __init__(self, account_number: str, owner: str, balance: float = 0.0):

        if not isinstance(account_number, str):
            raise TypeError("Номер счета должен быть типа str")
        if not account_number:
            raise ValueError("Номер счета не может быть пустым")
        self.account_number = account_number

        if not isinstance(owner, str):
            raise TypeError("Владелец счета должен быть типа str")
        if not owner:
            raise ValueError("Владелец счета не может быть пустым")
        self.owner = owner

        if not isinstance(balance, (int, float)):
            raise TypeError("Баланс счета должен быть типа int или float")
        if balance < 0:
            raise ValueError("Баланс счета не может быть отрицательным")
        self.balance = float(balance)

    def is_account_empty(self) -> bool:

        return self.balance == 0.0

    def deposit(self, amount: float) -> None:

        if not isinstance(amount, (int, float)):
            raise TypeError("Сумма должна быть типа int или float")
        if amount < 0:
            raise ValueError("Сумма не может быть отрицательной")
        self.balance += amount

    def withdraw(self, amount: float) -> bool:

        if not isinstance(amount, (int, float)):
            raise TypeError("Сумма должна быть типа int или float")
        if amount < 0:
            raise ValueError("Сумма не может быть отрицательной")
        if amount > self.balance:
            return False
        self.balance -= amount
        return True

    def get_account_info(self) -> str:

        return f'Счет: {self.account_number}, владелец: {self.owner}, баланс: {self.balance}'

if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod(verbose=True)