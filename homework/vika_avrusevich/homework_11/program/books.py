from main import Book
# from main import *
# import main

books = [Book('Гордость и предубеждение', 100, 2000, 'Джейн Остен', 123),
         Book('Гарри Поттер', 200, 2001, 'Джоан Роулинг', 345),
         Book('Алиса в Стране чудес', 300, 2002, 'Льюис Кэрролл', 567)]

# print(books)
for book in books:
    print(f'Name: {book.name}\n'
          f'Pages: {book.pages}\n'
          f'Year: {book.year}\n'
          f'Author: {book.author}\n'
          f'Price: {book.price}\n')

print(f'1 - year: {books[0].year}\n2 - pages: {books[1].pages}\n3 - author: {books[2].author}')
