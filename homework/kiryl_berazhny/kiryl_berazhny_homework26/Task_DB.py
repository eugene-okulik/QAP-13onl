import mysql.connector as mysql


db = mysql.connect(
    user='qap',
    passwd='AVNS_kkO9k0GPxfmPRPop6cY',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='qap13'
)
cursor = db.cursor(dictionary=True)


def new_group(title_group, start_date, end_date):
    query = 'INSERT INTO `groups` (title, start_date, end_date) VALUES (%s, %s, %s)'
    values = (title_group, start_date, end_date)
    cursor.execute(query, values)
    db.commit()


def group_id(title_group):
    cursor.execute('SELECT id FROM `groups` WHERE title = %s', (title_group,))
    return cursor.fetchone()['id']


def new_student_in_group(name, second_name, id_group):
    query = 'INSERT INTO students (name, second_name, group_id) VALUES (%s, %s, %s)'
    values = (name, second_name, id_group)
    cursor.execute(query, values)
    db.commit()


def student_id(name, second_name, title_group):
    id_group = group_id(title_group)
    query = 'SELECT id FROM students WHERE name = %s AND second_name = %s AND group_id = %s'
    values = (name, second_name, id_group)
    cursor.execute(query, values)
    return cursor.fetchone()['id']


def new_books_a_student(student, book):
    query = 'INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)'
    for i in book:
        values = (i, student)
        cursor.execute(query, values)
    db.commit()


def info_student(student):
    cursor.execute(
        '''SELECT students.name, students.second_name, `groups`.title as group_title, books.title as book_title
        FROM students 
        JOIN books ON students.id = books.taken_by_student_id 
        JOIN `groups` ON students.group_id = `groups`.id  
        WHERE students.id = %s''',
        (student,)
    )
    result = cursor.fetchall()
    student = f"{result[0]['name']} {result[0]['second_name']}"
    group = result[0]['group_title']
    books_student = [book['book_title'] for book in result]
    print(
        f'{student} is a student in the {group} group'
        f' and borrowed the following books from the library: {" and ".join(books_student)}'
    )


new_group('10-ES-1', '01-09-2010', '30-06-2015')
id_group_student = group_id('10-ES-1')
new_student_in_group('Kiryl', 'Berazhny', id_group_student)
id_student = student_id('Kiryl', 'Berazhny', '10-ES-1')
books = ['Factotum', 'Women']
new_books_a_student(id_student, books)
info_student(id_student)


db.close()
