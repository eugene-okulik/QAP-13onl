# Библиотека (работа с классами)

import json


class Books:
    material = 'Бумага'
    text_presence = True

    def __init__(self, library):

        self.library = library
        self.book = json.loads(self.read_file())
        self.name_book = self.book['Название книги']
        self.author_book = self.book['Автор']
        self.num_pages = self.book['Количество страниц']
        self.isbn = self.book['ISBN']
        self.status = self.status_book()

    def read_file(self):

        with open(self.library) as book_file:
            return book_file.read()

    def status_book(self):

        if self.book['Статус'] == 'Зарезервирована':
            return self.book['Статус']
        else:
            return ''


list_book = list()
book1 = Books('Book_1.txt')
list_book.append(book1)
book2 = Books('Book_2.txt')
list_book.append(book2)
book3 = Books('Book_3.txt')
list_book.append(book3)
book4 = Books('Book_4.txt')
list_book.append(book4)
book5 = Books('Book_5.txt')
list_book.append(book5)
book6 = Books('Book_6.txt')
list_book.append(book6)
for book in list_book:
    print(
        f'Название: {book.name_book}, Автор: {book.author_book}, страниц: {book.num_pages}, '
        f'материал: {book.material} {book.status}'
    )
print()


class SchoolTextbooks(Books):

    def __init__(self, library):

        super().__init__(library)
        self.disc = self.book['Предмет']
        self.class_number = self.book['Класс']
        self.job = self.job_availability()

    def job_availability(self):

        if self.book['Наличие заданий'] == 'Есть':
            return self.book['Наличие заданий']
        else:
            return ''


list_school_book = list()
School_book1 = SchoolTextbooks('School_book1.txt')
list_school_book.append(School_book1)
School_book2 = SchoolTextbooks('School_book2.txt')
list_school_book.append(School_book2)
School_book3 = SchoolTextbooks('School_book3.txt')
list_school_book.append(School_book3)
School_book4 = SchoolTextbooks('School_book4.txt')
list_school_book.append(School_book4)
for book in list_school_book:
    print(
        f'Название: {book.name_book}, Автор: {book.author_book}, страниц: {book.num_pages}, '
        f'предмет: {book.disc}, класс: {book.class_number} {book.status}'
    )
