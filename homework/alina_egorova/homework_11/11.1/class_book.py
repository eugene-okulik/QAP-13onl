# Импорт класса
# Создайте папку с программой. В одном файле создайте класс, а команды, использующие этот класс поместите в другом
# файле. Класс должен содержать информацию о книге - класс Book. Атрибуты: количество страниц, год издания, автор, цена.
# В файле с командами создайте несколько экземпляров объекта Book. Для каждого из экземпляров выведите на экран
# какую-либо информацию о нем. Во время работы с импортом попробуйте разные способы (импорт конкретно класса,
# импорт файла, содержащего класс, и т.д.)
class Book:
    def __init__(self, book_title, author, number_of_pages, year_of_publishing, price):
        self.book_title = book_title
        self.author = author
        self.number_of_pages = number_of_pages
        self.year_of_publishing = year_of_publishing
        self.price = price
