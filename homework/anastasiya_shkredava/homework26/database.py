import mysql.connector as mysql


db = mysql.connect(
    user='qap',
    passwd='AVNS_kkO9k0GPxfmPRPop6cY',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='qap13'
)

cursor = db.cursor(dictionary=True)


def create_group(title, start_date, end_date):
    create_group_query = '''INSERT
                         INTO `groups` (title, start_date, end_date)
                         VALUES (%s, %s, %s)'''
    values = (title, start_date, end_date)
    cursor.execute(create_group_query, values)
    db.commit()
    gr_id = cursor.lastrowid
    return gr_id


def create_student(name, second_name, gr_id):
    create_student_query = '''INSERT
                           INTO students (name, second_name, group_id)
                           VALUES (%s, %s, %s)'''
    values = (name, second_name, gr_id)
    cursor.execute(create_student_query, values)
    db.commit()
    st_id = cursor.lastrowid
    return st_id


def create_book(books, st_id):
    create_book_query = '''INSERT
                        INTO books (title, taken_by_student_id)
                        VALUES (%s, %s)'''
    for book in books:
        values = (book, st_id)
        cursor.execute(create_book_query, values)
    db.commit()


def student_data(st_id):
    data_query = '''SELECT students.name, students.second_name, `groups`.title as group_title, books.title as book_title
                FROM `groups`
                JOIN students ON `groups`.id = students.group_id
                JOIN books ON students.id = books.taken_by_student_id
                WHERE students.id = %s'''
    values = (st_id,)
    cursor.execute(data_query, values)
    result = cursor.fetchall()
    name = result[0]['name']
    second_name = result[0]['second_name']
    group_title = result[0]['group_title']
    books = [result[i]['book_title']for i in range(len(result))]
    print(f"Student {name} {second_name} studies in '{group_title}' group "
          f"and has borrowed from a library the following books: {', '.join(books)}")


books_list = ['Organic Chemistry', 'Analytical Chemistry']

group_id = create_group('Chem', '01-Jan-2023', '12-Aug-2023')
student_id = create_student('Dima', 'Mendeleev', group_id)
create_book(books_list, student_id)
student_data(student_id)

db.close()
