# Импорт класса

# from homework.kiryl_berazhny.kiryl_berazhny_homework11 import create_class as CB
#
# book1 = CB.Books('Polska', 50, 2022, 'Duda', 50)
# book2 = CB.Books('Belarus', 40, 2023, 'Kiryl', 40)
# book3 = CB.Books('Germany', 45, 2019, 'Adolf', 30)
# book1.read_author()
# book2.read_date()
# book3.read_book()


from homework.kiryl_berazhny.kiryl_berazhny_homework11.create_class import Books as CB  # импорт класса из файла

book1 = CB('Polska', 50, 2022, 'Duda', 50)
book2 = CB('Belarus', 40, 2023, 'Kiryl', 40)
book3 = CB('Germany', 45, 2019, 'Adolf', 30)
book1.read_author()
book2.read_date()
book3.read_book()
