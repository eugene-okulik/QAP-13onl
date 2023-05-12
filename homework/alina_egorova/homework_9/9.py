# Первый класс
class Book:
    page_material = 'бумага'
    presence_of_text = True

    def __init__(self, book_title, author, number_of_pages, ISBN, reserved_flag):
        self.book_title = book_title
        self.author = author
        self.number_of_pages = number_of_pages
        self.ISBN = ISBN
        self.reserved_flag = reserved_flag

    def reserv(self):
        if self.reserved_flag:
            return (
                f'Название: {self.book_title}, Автор: {self.author}, Страниц: {self.number_of_pages}, '
                f'Материал: {self.page_material}, Зарезервирована'
            )
        else:
            return (
                f'Название: {self.book_title}, Автор: {self.author}, Страниц: {self.number_of_pages}, '
                f'Материал: {self.page_material}'
            )


book1 = Book('Мастер и Маргарита', 'Булгаков', 464, 9785001120636, True)
book2 = Book('Идиот', 'Достоевский', 624, 9785171123789, False)
book3 = Book('Незнайка', 'Носов', 512, 9785389202108, False)
book4 = Book('Муму', 'Тургенев', 224, 9785041191405, False)
book5 = Book('Метель', 'Пушкин', 24, 9785392305803, False)
print(book1.reserv())
print(book2.reserv())
print(book3.reserv())
print(book4.reserv())
print(book5.reserv())


# Второй класс
class SchoolClassNumber(Book):
    availability_of_tasks_bool = True

    def __init__(self, book_title, author, number_of_pages, ISBN, class_num, item, reserved_flag):
        super().__init__(book_title, author, number_of_pages, ISBN, reserved_flag)
        self.class_num = class_num
        self.item = item

    def reserv(self):
        if self.reserved_flag:
            return (
                f'Название: {self.book_title}, Автор: {self.author}, Страниц: {self.number_of_pages}, '
                f'Предмет: {self.item}, Класс: {self.class_num}, Зарезервирована'
            )
        else:
            return (
                f'Название: {self.book_title}, Автор: {self.author}, Страниц: {self.number_of_pages}, '
                f'Предмет: {self.item}, Класс: {self.class_num}'
            )


book6 = SchoolClassNumber('Русский язык', 'Разумовская', 250, 9785001154268, 11, 'Русский язык', False)
book7 = SchoolClassNumber('Алгебра', 'Мордкович', 233, 9784761123789, 8, 'Математика', False)
book8 = SchoolClassNumber('Геометрия', 'Атанасян', 150, 9785352692108, 8, 'Математика', True)
book9 = SchoolClassNumber('Всеобщая история. Новейшая история.', 'Иванов', 224, 9785090736534, 10, 'История', False)

print(book6.reserv())
print(book7.reserv())
print(book8.reserv())
print(book9.reserv())
