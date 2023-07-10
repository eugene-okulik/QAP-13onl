import mysql.connector as mysql

db = mysql.connect(
    user='qap',
    passwd='AVNS_kkO9k0GPxfmPRPop6cY',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='qap13'
)

cursor = db.cursor(dictionary=True)


# Создает группу (даты в запросе можно указывать как строки, т.е. '2022-04-03')
def create_group(title, start_date, end_date):
    new_group = '''INSERT INTO `groups`(title, start_date, end_date) VALUES(%s, %s, %s)'''
    values = (title, start_date, end_date)
    cursor.execute(new_group, values)
    db.commit()
    group_id = cursor.lastrowid
    return group_id


# Создает студента с именем и фамилией, такими как вы придумаете и group_id той группы, что вы создали
def create_student(name, second_name, group_id):
    new_student = '''INSERT INTO students (name, second_name, group_id) VALUES(%s, %s, %s)'''
    values = (name, second_name, group_id)
    cursor.execute(new_student, values)
    db.commit()
    student_id = cursor.lastrowid
    return student_id


# Создает 2 книги. В колонку taken_by_student_id записывает id вашего студента.
def create_books(books, student_id):
    new_books = '''INSERT INTO books (title, taken_by_student_id) VALUES(%s, %s)'''
    for book in books:
        values = (book, student_id)
        cursor.execute(new_books, values)
    db.commit()


# Получает из базы данных данные для студента, которого вы добавили. Желательно одним запросом получить
# и студента и группы и книги (с помощью Join). Выводит следующий текст на основании полученных данных:
# Студент Ivan Ivanov учится в группе GPN-001 и взял в библиотеке следующие книги: SQL essentials,
# Python for dummies
def student_info(student_id):
    get_info = '''SELECT students.name, students.second_name, `groups`.title as group_title, books.title as book_title
             FROM `groups`
             JOIN students ON `groups`.id = students.group_id
             JOIN books ON students.id = books.taken_by_student_id
             WHERE students.id = %s'''
    values = (student_id,)
    cursor.execute(get_info, values)
    res = cursor.fetchall()
    name = res[0]['name']
    second_name = res[0]['second_name']
    group_title = res[0]['group_title']
    books = [res[i]['book_title'] for i in range(len(res))]
    print(f'Student {name} {second_name} studies in {group_title} '
          f'and has taken in library the following books: {", ".join(books)}')


group = create_group('Math', '01-09-2022', '31-05-2023')
student = create_student('Ivan', 'Ivanov', group)
list_of_books = ['Math', 'Bio', 'Geo']
create_books(list_of_books, student)
student_info(student)

db.close()
