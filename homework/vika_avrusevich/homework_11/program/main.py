# Класс должен содержать информацию о книге - класс Book. Атрибуты: количество страниц, год издания, автор, цена.
# В файле с командами создайте несколько экземпляров объекта Book. Для каждого из экземпляров
# выведите на экран какую-либо информацию о нем. Во время работы с импортом попробуйте разные способы
# (импорт конкретно класса, импорт файла, содержащего класс, и т.д.)

class Book:
    def __init__(self, name, pages, year, author, price):
        self.name = name
        self.pages = pages
        self.year = year
        self.author = author
        self.price = price