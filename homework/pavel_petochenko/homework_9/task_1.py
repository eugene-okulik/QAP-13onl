# Первый класс
# Создайте класс book с атрибутами:
#     материал страниц
#     наличие текста
#     название книги
#     автор
#     кол-во страниц
#     ISBN
#     флаг зарезервирована ли книга или нет (True/False).
# Какие-то из атрибутов будут общими для всех книг (материал, наличие текста), какие-то индивидуальными.
# Создайте несколько (штук 5) экземпляров разных книг.
# После создания пометьте одну книгу как зарезервированную.
# Распечатайте детали о каждой книге в таком виде:
# Если книга зарезервирована:
#     Название: Идиот, Автор: Достоевский, страниц: 500, материал: бумага, зарезервирована
# если не зарезервирована:
#     Название: Идиот, Автор: Достоевский, страниц: 500, материал: бумага
#
# Второй класс
# Создайте дочерний класс для первого. Это будет класс для школьных учебников. В нем будут дополнительные атрибуты:
#     предмет (типа математика, история, география),
#     класс (школьный класс, для которого этот учебник)(осторожно с названием переменной. class - зарезервиров. слово),
#     наличие заданий (bool)
# Создайте несколько экземпляров учебников.
# После создания пометьте один учебник как зарезервированный.
# Распечатайте детали о каждом учебнике в таком виде: Если учебник зарезервирован:
#     Название: Алгебра, Автор: Иванов, страниц: 200, предмет: Математика, класс: 9, зарезервирована
# если не зарезервирован:
#     Название: Алгебра, Автор: Иванов, страниц: 200, предмет: Математика, класс: 9


class Book:
    page_material = 'бумага'
    presence_of_text = True

    def __init__(self, title, author, num_of_pages, isbn, reserved=False):
        self.title = title
        self.author = author
        self.num_of_pages = num_of_pages
        self.isbn = isbn
        self.reserved = reserved

    def details(self):
        if self.reserved:
            reservation = ', эта книга зарезервирована'
        else:
            reservation = ''
        print(f'Название: {self.title}, Автор: {self.author}, страниц: {self.num_of_pages},'
              f' материал страниц: {self.page_material}, ISBN: {self.isbn}{reservation}.')


book1 = Book('11/22/63', 'Stephen King', 925, '978-5-17-134703-1')
book2 = Book('The Lord Of the Rings. Pt.1: The Fellowship Of the Ring', 'John R. R. Tolkien', 510, '978-5-17-107241-8')
book3 = Book('1984', 'George Orwell', 371, '978-5-9925-0563-4')
book4 = Book('The Catcher in The Rye', 'Jerome David Salinger', 246, '978-5-9925-0147-6')
book5 = Book('The Chronicles Of Narnia', 'C. S. Lewis', 834, '978-5-699-44894-4')

book3.reserved = True

book1.details()
book2.details()
book3.details()
book4.details()
book5.details()


class SchoolBook (Book):
    def __init__(self, title, author, num_of_pages, isbn, subject, grade, exercise, reserved=False):
        super().__init__(title, author, num_of_pages, isbn, reserved)
        self.subject = subject
        self.grade = grade
        self. exercise = exercise


textbook1 = SchoolBook('Алгебра', 'Дмитриева Д. Д.', 100500, '123456789', 'Математика', 10, True)
textbook2 = SchoolBook('Анатомия', 'Иванов И. И.', 3, '987654321', 'Биология', 7, False)

textbook1.reserved = True

for textbook in [textbook1, textbook2]:
    if textbook.reserved:
        print(f"Название: {textbook.title}, Автор: {textbook.author}, страниц: {textbook.num_of_pages}, "
              f"предмет: {textbook.subject}, класс: {textbook.grade}, зарезервирована")
    else:
        print(f"Название: {textbook.title}, Автор: {textbook.author}, страниц: {textbook.num_of_pages}, "
              f"предмет: {textbook.subject}, класс: {textbook.grade}")
