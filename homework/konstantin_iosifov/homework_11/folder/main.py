from book import Book
# import book
# from book import *

book1 = Book(300, 2005, "J.K. Rowling", 20.99)
book2 = Book(400, 1997, "J.R.R. Tolkien", 25.99)
book3 = Book(250, 2020, "Stephen Hawking", 15.99)

print("Book 1:")
print("Pages:", book1.pages)
print("Year:", book1.year)
print("Author:", book1.author)
print("Price:", book1.price)

print("Book 2:")
print("Pages:", book2.pages)
print("Year:", book2.year)
print("Author:", book2.author)
print("Price:", book2.price)

print("Book 3:")
print("Pages:", book3.pages)
print("Year:", book3.year)
print("Author:", book3.author)
print("Price:", book3.price)
