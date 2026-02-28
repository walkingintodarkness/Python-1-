class Book:
    """Базовый класс для всех книг."""

    def __init__(self, name, author):
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f'Книга "{self.name}". Автор {self.author}'

    def __repr__(self):
        return f"Book('{self.name}', '{self.author}')"


class PaperBook(Book):
    """Бумажная книга, добавляется количество страниц."""

    def __init__(self, name, author, pages):
        Book.__init__(self, name, author)
        self.pages = pages

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value):
        if type(value) != int:
            raise TypeError("Количество страниц должно быть целым числом")
        if value <= 0:
            raise ValueError("Количество страниц должно быть больше 0")
        self._pages = value

    def __str__(self):
        return f'Книга "{self.name}". Автор {self.author}. {self.pages} стр.'

    def __repr__(self):
        return f"PaperBook('{self.name}', '{self.author}', {self.pages})"


class AudioBook(Book):
    """Аудиокнига, добавляется длительность в часах."""

    def __init__(self, name, author, duration):
        Book.__init__(self, name, author)
        self.duration = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        if type(value) not in (float, int):
            raise TypeError("Длительность должна быть числом")
        if value <= 0:
            raise ValueError("Длительность должна быть больше 0")
        self._duration = float(value)

    def __str__(self):
        return f'Книга "{self.name}". Автор {self.author}. Длительность {self.duration} ч.'

    def __repr__(self):
        return f"AudioBook('{self.name}', '{self.author}', {self.duration})"