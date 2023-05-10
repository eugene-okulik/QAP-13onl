# Case A
# Importing multiple classes from another file in the same folder

import Book_class


book1 = Book_class.Book('Atomic Habits', 290, 2018, 'James Clear', 60)
book2 = Book_class.Book('Island', 300, 2020, 'Aldous Huxley', 15)
book3 = Book_class.Book('Alice in Wonderland', 100, 2022, 'Lewis Carroll', 13)
print(book1.name, book2.pages, book3.cost)


# # Case B
# # Importing all classes from another file in the same folder using import * command
#
# from Book_class import *
#
#
# book1 = Book('Atomic Habits', 290, 2018, 'James Clear', 60)
# book2 = Book('Island', 300, 2020, 'Aldous Huxley', 15)
# book3 = Book('Alice in Wonderland', 100, 2022, 'Lewis Carroll', 13)
# print(book1.name, book2.pages, book3.cost)


# # Case C
# # Importing a specific class from another file in the same folder
#
# from Book_class import Book as Bk
#
#
# book1 = Bk('Atomic Habits', 290, 2018, 'James Clear', 60)
# book2 = Bk('Island', 300, 2020, 'Aldous Huxley', 15)
# book3 = Bk('Alice in Wonderland', 100, 2022, 'Lewis Carroll', 13)
# print(book1.name, book2.pages, book3.cost)
