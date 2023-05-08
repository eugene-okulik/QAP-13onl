class Book:
    page_material = 'Бумага'
    text_presence = True

    def __init__(self, book_name: str, book_author: str, pages_qty: int, isbn: str, reservation_flag: bool):
        self.book_name = book_name
        self.book_author = book_author
        self.pages_qty = pages_qty
        self.isbn = isbn
        self.reservation_flag = reservation_flag

    def __str__(self):
        if not self.reservation_flag:
            return f'Название: {self.book_name}, Автор: {self.book_author}, Страниц: {self.pages_qty}, ' \
                   + f'Материал: {self.page_material})'
        else:
            return f'Название: {self.book_name}, Автор: {self.book_author}, Страниц: {self.pages_qty}, ' \
                   + f'Материал: {self.page_material}, Зарезервирована)'


book1 = Book('Вишнёвый сад', 'А.П.Чехов', 800, '978-3-16-148410-0', False)
book2 = Book('Шинель', 'Н.В.Гоголь', 560, '978-3-16-118410-0', True)
book3 = Book('Война и Мир', 'Л.Н.Толстой', 99999, '978-3-16-143410-0', False)
book4 = Book('Мцыри', 'М.Ю.Лермонтов', 700, '978-3-16-148410-0', False)
book5 = Book('Джанга с тенями', 'А.Пехов', 633, '928-3-16-148410-0', False)
print(book1)
print(book2)
print(book3)
print(book4)
print(book5)


class SchoolBook(Book):

    def __init__(self, subject: str, grade: int, tasks: bool, book_name: str, book_author: str, pages_qty: int,
                 isbn: str, reservation_flag: bool):
        self.subject = subject
        self.grade = grade
        self.tasks = tasks
        super().__init__(book_name, book_author, pages_qty, isbn, reservation_flag)

    # Название: Алгебра, Автор: Иванов, страниц: 200, предмет: Математика, класс: 9, зарезервирована
    def __str__(self):
        if not self.reservation_flag:
            return f'Название: {self.book_name}, Автор: {self.book_author}, Страниц: {self.pages_qty}, ' \
                   + f'Предмет: {self.subject}, Класс: {self.grade})'
        else:
            return f'Название: {self.book_name}, Автор: {self.book_author}, Страниц: {self.pages_qty}, ' \
                   + f'Предмет: {self.subject}, Класс: {self.grade}, Зарезервирована)'


student_book1 = SchoolBook('Математика', 9, True, 'Алгебра', 'Мордкович', 100, '928-3-16-148410-0', False)
student_book2 = SchoolBook('Обществознание', 5, True, 'Обществознание', 'Петрович', 300, '928-3-16-148410-0', False)
student_book3 = SchoolBook('История Средневековья', 6, True, 'История', 'Иванов', 300, '928-3-16-148410-0', False)
student_book4 = SchoolBook('Химия', 8, True, 'Химия', 'Семёнова', 200, '928-3-16-148410-0', True)
student_book5 = SchoolBook('Литература', 11, True, 'Литература', 'Кучеренко', 400, '928-3-16-148410-0', False)
print(student_book1)
print(student_book2)
print(student_book3)
print(student_book4)
print(student_book5)
