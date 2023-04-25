class FictionBooks:
    text_presence = True
    material = 'paper'

    def __init__(self, title, author, pages, isbn, reservation):
        self.title = title
        self.author = author
        self.pages = pages
        self.isbn = isbn
        self.reservation = reservation

    def book_reservation(self):
        output = f'Book Title: {self.title}, Author: {self.author}, pages: {self.pages}, material: {self.material}'
        return f'{output}, RESERVED' if self.reservation else output


class SchoolBooks(FictionBooks):
    def __init__(self, title, author, pages, isbn, reservation, school_subject, grade, tasks):
        super().__init__(title, author, pages, isbn, reservation)
        self.school_subject = school_subject
        self.grade = grade
        self.tasks = tasks

    def book_reservation(self):
        output = f'Book Title: {self.title}, Author: {self.author}, ' \
                 f'pages: {self.pages}, subject: {self.school_subject}, grade: {self.grade}'
        return f'{output}, RESERVED' if self.reservation else output


fiction_books = [
    FictionBooks('Island', 'Aldous Huxley', 300, 1234567898, False),
    FictionBooks('Alice in Wonderland', 'Lewis Carroll', 100, 3216549879, True),
    FictionBooks('Winnie-the-Pooh', 'Alan Alexander Milne', 140, 4567891231, False),
    FictionBooks('Harry Potter', 'J. K. Rowling', 300, 1379842655, False),
    FictionBooks('The Lord of the Rings', 'Tolkien', 800, 7913468258, False)
]
fiction_books_list = [book.book_reservation() for book in fiction_books]
for book in fiction_books_list:
    print(book)

school_books = [
    SchoolBooks('Chemistry 10 class', 'Mendeleev', 150, 4567891235, True, 'Chemistry', 10, True),
    SchoolBooks('Geography 7 class', 'Columbus', 120, 4561235789, False, 'Geography', 7, False),
    SchoolBooks('Physics 9 class', 'Newton', 170, 4562861739, False, 'Physics', 9, True)
]
school_books_list = [book.book_reservation() for book in school_books]
for book in school_books_list:
    print(book)
