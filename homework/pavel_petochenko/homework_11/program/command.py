# Для этого файла:
# В файле с командами создайте несколько экземпляров объекта Book.
# Для каждого из экземпляров выведите на экран какую-либо информацию о нем.
# Во время работы с импортом попробовать разные способы (импорт конкретно класса, импорт файла,
# содержащего класс, и т.д.)

# Импорт1:
# from class_book import Book
# book1 = Book(512, 2022, 'John R.R. Tolkien', 34)
# book2 = Book(848, 2014, 'C. S. Lewis', 30)
# book3 = Book(928, 2021, 'Stephen King', 25)
# print(book1.price, book2.year, book3.author)

# Импорт2:
# from class_book import Book as Shelf
# book1 = Shelf(512, 2022, 'John R.R. Tolkien', 34)
# book2 = Shelf(848, 2014, 'C. S. Lewis', 30)
# book3 = Shelf(928, 2021, 'Stephen King', 25)
# print(book1.num_page, book2.author, book3.year)

# Импорт3:
from homework.pavel_petochenko.homework_11.program.class_book import Book
book1 = Book(512, 2022, 'John R.R. Tolkien', 34)
book2 = Book(848, 2014, 'C. S. Lewis', 30)
book3 = Book(928, 2021, 'Stephen King', 25)
print(book1.author, book2.year, book3.num_page)
