# Создание класса

class Books:

    def __init__(self, name: str, num_page: int, date: int, author: str, price: float):

        self.name = name
        self.num_page = num_page
        self.date = date
        self.author = author
        self.price = price

    def read_book(self):

        print(
            f'Наименование книги: {self.name}, количество страниц: {self.num_page}, год издания: {self.date}, '
            f'автор: {self.author}, цена: {self.price}.'
        )

    def read_num(self):

        print(f'Наименование книги: {self.name}, количество страниц: {self.num_page}.')

    def read_date(self):

        print(f'Наименование книги: {self.name}, год издания: {self.date}.')

    def read_author(self):
        print(f'Наименование книги: {self.name}, автор: {self.author}.')

    def read_price(self):
        print(f'Наименование книги: {self.name}, цена: {self.price}.')
