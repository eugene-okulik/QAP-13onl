# Библиотека (работа с классами)

import json


class Books:
    material = 'Бумага'
    text_presence = True

    def __init__(self, library):

        self.library = library
        self.book = self.read_file()
        self.book_num = self.book_number()
        self.name_book = self.book[self.book_num]['Название книги']
        self.author_book = self.book[self.book_num]['Автор']
        self.num_pages = self.book[self.book_num]['Количество страниц']
        self.isbn = self.book[self.book_num]['ISBN']
        self.status = self.status_book()

    def read_file(self):

        with open(self.library) as book_file:
            library_book = list()
            for book in book_file:
                library_book.append(json.loads(book))
            return library_book

    def book_number(self):

        print('Список книг:')
        for number in range(len(self.book)):
            if "Класс" in self.book[number]:
                print(f'{number + 1}. {self.book[number]["Название книги"]}, '
                      f'{self.book[number]["Автор"]}, {self.book[number]["Класс"]} класс')
            else:
                print(f'{number + 1}. {self.book[number]["Название книги"]}, '
                      f'{self.book[number]["Автор"]}')
        print('\nДля более детальной информации о книге необходимо ввести ее номер.')
        while True:
            num_book = int(input('Введите номер интересующей книги: '))
            if 0 < num_book <= len(self.book):
                return num_book - 1
            else:
                print(f'В библиотеке {len(self.book)} книг.')

    def status_book(self):

        if self.book[self.book_num]['Статус'] == 'Зарезервирована':
            return self.book[self.book_num]['Статус']
        else:
            return ''


class SchoolTextbooks(Books):

    def __init__(self, library):

        super().__init__(library)
        self.disc = self.book[self.book_num]['Предмет']
        self.class_number = self.book[self.book_num]['Класс']
        self.job = self.job_availability()

    def job_availability(self):

        if self.book[self.book_num]['Наличие заданий'] == 'Есть':
            return self.book[self.book_num]['Наличие заданий']
        else:
            return ''


while True:
    print(
        'В библиотеке имеются:'
        '\n1. Художественная литература.'
        '\n2. Школьные учебники.'
        '\nВыберите раздел (введите номер раздела): '
    )
    selection = int(input())
    if selection == 1:
        main_library = Books('library.txt')
        print(
            f'\nНазвание: {main_library.name_book}, Автор: {main_library.author_book},'
            f' страниц: {main_library.num_pages}, материал: {main_library.material} {main_library.status}'
        )
    elif selection == 2:
        School_books = SchoolTextbooks('school_library.txt')
        print(
            f'Название: {School_books.name_book}, Автор: {School_books.author_book}, '
            f'страниц: {School_books.num_pages}, предмет: {School_books.disc}, '
            f'класс: {School_books.class_number} {School_books.status}'
        )
    else:
        break
    qa = input('\nХотите выбрать другую книгу?  Введите "да": ')
    if qa.lower() != 'да' and qa.lower() != 'lf':
        print("\nСпасибо, что обратились к нам!")
        break
