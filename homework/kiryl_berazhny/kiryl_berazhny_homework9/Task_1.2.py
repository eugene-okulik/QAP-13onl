# Библиотека (работа с классами).
# Есть пару вопросов - 1. функция book_number (строка 34), пришлось ее сильно расписать, так как не разобрался как ее
# вызвать внутри самой себя (это помогло бы в два раза сократить код самой функции).
# По поиску тоже есть нюансы, а именно - я поставил порог символов 4 штуки. А если название книги из одной буквы,
# то получается нужно добавить поиск еще по автору книги, но уже было лень расписывать. И еще плюс поиск не умеет искать
# книги, название которых состоят только из цифр.
# В целом задание класс, спасибо

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

    def read_file(self):  # чтение файла (получится список)

        with open(self.library) as book_file:
            library_book = [json.loads(book) for book in book_file]
            return library_book

    def book_number(self):  # отвечает за выбор индекса книги, которую выбираем из прочтенного файла

        print('Список книг:')
        for number in range(len(self.book)):
            if "Класс" in self.book[number]:
                print(
                    f'{number + 1}. {self.book[number]["Название книги"]}, '
                    f'{self.book[number]["Автор"]}, {self.book[number]["Класс"]} класс'
                )
            else:
                print(f'{number + 1}. {self.book[number]["Название книги"]}, {self.book[number]["Автор"]}')
        print('\nВоспользуйтесь поиском или выберите необходимую книгу')
        while True:
            num_book = input('Введите номер интересующей книги или введите название книги (не менее 4 символов): ')
            if num_book.isdigit() is True:
                num_book = int(num_book)
                if 0 < num_book <= len(self.book):
                    return num_book - 1
                else:
                    print(f'В библиотеке {len(self.book)} книг.')
            else:
                while True:
                    while len(num_book) < 4:
                        num_book = input('Введите не менее 4 символов для поиска книги: ')
                    search_list = list()
                    for name in self.book:
                        if num_book.lower() in name["Название книги"].lower():
                            search_list.append(name)
                    if search_list == list():
                        num_book = input(
                            'К сожалению такой книги нету, попробуйте заново (введите не менее 4 символов):'
                        )
                    elif len(search_list) == 1:
                        return self.book.index(search_list[0])
                    else:
                        print('\nПо вашему запросу доступны следующие книги:')
                        for index_book in range(len(search_list)):
                            if "Класс" in search_list[index_book]:
                                print(
                                    f'{index_book + 1}. {search_list[index_book]["Название книги"]}, '
                                    f'{search_list[index_book]["Автор"]}, {search_list[index_book]["Класс"]} '
                                    f'класс'
                                )
                            else:
                                print(
                                    f'{index_book + 1}. {search_list[index_book]["Название книги"]}, '
                                    f'{search_list[index_book]["Автор"]}'
                                )
                        while True:
                            num_list = int(input('Введите номер интересующей книги : '))
                            if 0 < num_list <= len(search_list):
                                return self.book.index(search_list[num_list - 1])
                            else:
                                print(f'Поиск дал книг: {len(search_list)}.')

    def status_book(self):  # это необходимо для вывода результата с артикулом "Зарезервирована"

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
    )
    selection = int(input('Выберите раздел (введите номер раздела): '))
    if selection == 1:
        main_library = Books('library.txt')
        print(
            f'\nНазвание: {main_library.name_book}, Автор: {main_library.author_book},'
            f' страниц: {main_library.num_pages}, материал: {main_library.material} {main_library.status}'
        )
    elif selection == 2:
        School_books = SchoolTextbooks('school_library.txt')
        print(
            f'\nНазвание: {School_books.name_book}, Автор: {School_books.author_book}, '
            f'страниц: {School_books.num_pages}, предмет: {School_books.disc}, '
            f'класс: {School_books.class_number} {School_books.status}'
        )
    else:
        break
    qa = input('\nХотите выбрать другую книгу?  Введите "да": ')
    if qa.lower() != 'да' and qa.lower() != 'lf':
        print("\nСпасибо, что обратились к нам!")
        break
