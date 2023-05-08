class Book:
    def __init__(self, material, has_text, title, author, num_pages, isbn, reserved=False):
        self.material = material
        self.has_text = has_text
        self.title = title
        self.author = author
        self.num_pages = num_pages
        self.isbn = isbn
        self.reserved = reserved

    def reserve(self):
        self.reserved = True


book1 = Book("paper", True, "To Kill a Mockingbird", "Harper Lee", 324, "978-0061120084")
book2 = Book("paper", True, "1984", "George Orwell", 328, "978-0451524935")
book3 = Book("e-book", True, "The Alchemist", "Paulo Coelho", 208, "978-0061122415", True)
book4 = Book("paper", True, "Pride and Prejudice", "Jane Austen", 432, "978-0141439518")
book5 = Book("e-book", True, "The Great Gatsby", "F. Scott Fitzgerald", 180, "978-0743273565")


for book in [book1, book2, book3, book4, book5]:
    print(f"Book title: {book.title}")
    print(f"Author: {book.author}")
    print(f"Number of pages: {book.num_pages}")
    print(f"ISBN: {book.isbn}")
    print(f"Material: {book.material}")
    print(f"Has text: {book.has_text}")
    print(f"Reserved: {book.reserved}")
    print('----------------|')


class SchoolBooks(Book):
    def __init__(self, material, has_text, title, author, num_pages, isbn, subject, grade, homework, reserved=False):
        super().__init__(material, has_text, author, title, num_pages, isbn, reserved)
        self.subject = subject
        self.grade = grade
        self.homework = homework


sb1 = SchoolBooks("paper", True, "Algebra I", "John Doe", 320, "978-0133500400", "Mathematics", 9, True)
sb2 = SchoolBooks("paper", True, "World History", "Jane Smith", 400, "978-0133185499", "History", 10, True)
sb3 = SchoolBooks("paper", True, "English Grammar", "Lisa Williams", 240, "978-0131849372", "English", 8, True, True)

for sb in [sb1, sb2, sb3]:
    print(f"Subject: {sb.subject}")
    print(f"Author: {sb.author}")
    print(f"Grade: {sb.grade}")
    print(f"Homework: {sb.homework}")
    print(f"Reserved: {sb.reserved}")
    print('----------------|')
