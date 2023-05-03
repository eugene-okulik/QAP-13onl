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