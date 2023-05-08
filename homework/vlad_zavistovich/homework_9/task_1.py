class Book:
    material = 'бумага'
    text = True

    def __init__(self, book_name: str, author: str, num_pages: int, isbn: str, reservation_flag: bool):
        self.book_name = book_name
        self.author = author
        self.num_pages = num_pages
        self.isbn = isbn
        self.reservation_flag = reservation_flag

    def __str__(self):
        if not self.reservation_flag:
            return f'Название: {self.book_name}, Автор: {self.author}, страниц: {self.num_pages}, ' \
                + f'материал: {self.material}'
        else:
            return f'Название: {self.book_name}, Автор: {self.author}, страниц: {self.num_pages}, ' \
                + f'материал: {self.material}, зарезервирована'


book_1 = Book('Идиот', 'Достоевский', 816, '978-5-907028-28-9', True)
book_2 = Book('Мертвые души', 'Гоголь', 400, '978-5-9268-2498-5', False)
book_3 = Book('Мастер и Маргарита', 'Булгаков', 400, '978-5-00195-960-1', False)
book_4 = Book('Война и Мир', 'Толстой', 1000, '978-5-9268-2585-2', False)
book_5 = Book('Чиполлино', 'Джанни', 264, '978-5-699-76231-6', False)
print(book_1)
print(book_2)
print(book_3)
print(book_4)
print(book_5)


class SchoolBook(Book):

    def __init__(self, subject: str, grade: int, tasks: bool, book_name: str, book_author: str, pages_qty: int,
                 isbn: str, reservation_flag: bool):
        self.book_author = book_author
        self.pages_qty = pages_qty
        self.subject = subject
        self.grade = grade
        self.tasks = tasks
        super().__init__(book_name, book_author, pages_qty, isbn, reservation_flag)

    def __str__(self):
        if not self.reservation_flag:
            return f'Название: {self.book_name}, Автор: {self.book_author}, Страниц: {self.pages_qty}, ' \
                + f'Предмет: {self.subject}, Класс: {self.grade}'
        else:
            return f'Название: {self.book_name}, Автор: {self.book_author}, Страниц: {self.pages_qty}, ' \
                + f'Предмет: {self.subject}, Класс: {self.grade}, Зарезервирована'


student_book1 = SchoolBook('Математика', 1, True, 'Алгебра', 'Лозицкий', 125, '78-5-907028-28-9', True)
student_book2 = SchoolBook('Труды', 6, True, 'Труды', 'Васильевич', 999, '978-5-907028-28-9', False)
student_book3 = SchoolBook('История', 7, True, 'История', 'Крушевский', 99, '978-5-907028-28-9', False)
student_book4 = SchoolBook('Астрономия', 8, True, 'Астрономия', 'Чапская', 333, '978-5-907028-28-9', False)
student_book5 = SchoolBook('Литература', 11, True, 'Литература', 'Макаренко', 400, '978-5-907028-28-9', False)
print(student_book1)
print(student_book2)
print(student_book3)
print(student_book4)
print(student_book5)
