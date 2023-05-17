class Book:
    material = 'бумага'
    text = True

    def __init__(self, title, author, pages, isbn, reserved):
        self.title = title
        self.author = author
        self.pages = pages
        self.isbn = isbn
        self.reserved = reserved

    def details(self):
        res = (f'Название: {self.title}, Автор: {self.author}, Страниц: {self.pages}, Материал: {self.material}, '
               f'Наличие текста: {self.text}, ISBN: {self.isbn}')
        return f'{res}, RESERVED' if self.reserved else res


class StudentBook(Book):
    def __init__(self, title, author, pages, isbn, reserved, subject, num_class, tasks):
        super().__init__(title, author, pages, isbn, reserved)
        self.subject = subject
        self.num_class = num_class
        self.tasks = tasks

    def details(self):
        res = (f'Название: {self.subject}, Автор: {self.author}, Страниц: {self.pages}, Предмет: {self.subject}, '
               f'Класс: {self.num_class}, Наличие заданий: {self.tasks}')
        return f'{res}, RESERVED' if self.reserved else res


book1 = Book('Гордость и предубеждение', 'Джейн Остен', 100, 123456789, True)
book2 = Book('Гарри Поттер', 'Джоан Роулинг', 200, 345678901, True)
book3 = Book('Алиса в Стране чудес', 'Льюис Кэрролл', 300, 567890123, False)
book4 = Book('Маленький принц', 'Антуан де Сент-Экзюпери', 400, 789012345, False)
book5 = Book('Идиот', 'Достоевский', 500, 12345670, True)

student_book1 = StudentBook('Алгебра', 'Иванов', 100, 123456789, True, 'Математика', '10-A', True)
student_book2 = StudentBook('География', 'Петров', 200, 345678901, True, 'География', '7-Г', True)
student_book3 = StudentBook('Геометрия', 'Иванов', 300, 567890123, False, 'Математика', '9-Б', True)
student_book4 = StudentBook('Физика', 'Крутой', 400, 789012345, False, 'Физика', '5-В', True)
student_book5 = StudentBook('Труды', 'Петрович', 500, 12345670, True, 'Труды для девочек', '7-В', False)

print(f'\n{book1.details()}, '
      f'\n{book2.details()}, '
      f'\n{book3.details()}, '
      f'\n{book4.details()}, '
      f'\n{book5.details()}')
print(f'\n{student_book1.details()}, '
      f'\n{student_book2.details()}, '
      f'\n{student_book3.details()}, '
      f'\n{student_book4.details()}, '
      f'\n{student_book5.details()}')
