class Book:
    page_mat = 'бумага'
    presence_of_text = True

    def __init__(self, name_book, author, pages, isbn, flag):
        self.name_book = name_book
        self.author = author
        self.pages = pages
        self.isbn = isbn
        self.flag = flag

    def reserves(self):
        if self.flag:
            return (
                f'Название: {self.name_book}, Автор: {self.author}, Страниц: {self.pages}, '
                f'Материал: {self.page_mat}, Зарезервирована.'
            )
        else:
            return (
                f'Название: {self.name_book}, Автор: {self.author}, Страниц: {self.pages}, '
                f'Материал: {self.page_mat}.'
            )


book_1 = Book('Коллекционер', 'Джон Фаулз', 345, '978-5-386-01614-2', True)
book_2 = Book('Цветы для Элджернона', 'Джон Фаулз', 239, '128-5-326-45724-3', False)
book_3 = Book('1984', 'Джордж Оруэлл', 564, '999-9-286-32344-4', False)
book_4 = Book('Джейн Эйр', 'Шарлотта Бронте', 322, '888-1-106-23514-0', False)
book_5 = Book('Великий Гэтсби', 'Ф. С. Фицджеральд', 911, '777-4-626-76894-7', False)

print(book_1.reserves())
print(book_2.reserves())
print(book_3.reserves())
print(book_4.reserves())
print(book_5.reserves())


class SchBooks(Book):

    def __init__(self, name_book, author, pages, isbn, availability_task: bool, item, school_group, flag):
        super().__init__(name_book, author, pages, isbn, flag)
        self.availability_task = availability_task
        self.item = item
        self.school_group = school_group

    def reserves(self):
        if self.flag:
            return (
                f'Название: {self.name_book}, Автор: {self.author}, Страниц: {self.pages}, '
                f'Предмет: {self.item}, Класс: {self.school_group}, Зарезервирована.'
            )
        else:
            return (
                f'Название: {self.name_book}, Автор: {self.author}, Страниц: {self.pages}, '
                f'Предмет: {self.item}, Класс: {self.school_group}.'
            )


school_book_1 = SchBooks('Алгебра', 'Петров', 345, '999-9-286-32344-4', True, 'Математика', '8 класс', True)
school_book_2 = SchBooks('География', 'Сидоров', 249, '128-5-326-45724-3', True, 'География', '9 класс', False)
school_book_3 = SchBooks('Физика', 'Иванова', 234, '777-4-626-76894-7', True, 'Физика', '10 класс', False)

print(school_book_1.reserves())
print(school_book_2.reserves())
print(school_book_3.reserves())
