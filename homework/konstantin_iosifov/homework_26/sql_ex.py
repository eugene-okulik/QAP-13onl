import mysql.connector as mysql

db = mysql.connect(
    user='qap',
    passwd='AVNS_kkO9k0GPxfmPRPop6cY',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='qap13'
)
cursor = db.cursor()

group_name = 'GPN-053'
sd = '2023-05-05'
ed = '2023-08-19'
cursor.execute("INSERT INTO `groups` (title, start_date, end_date) VALUES (%s, %s, %s)", (group_name, sd, ed,))
group_id = cursor.lastrowid


student_first_name = 'James'
student_last_name = 'Bond'
cursor.execute("INSERT INTO students (name, second_name, group_id) VALUES (%s, %s, %s)",
               (student_first_name, student_last_name, group_id))
student_id = cursor.lastrowid


book_titles = ['Python SDET', 'Python for real-true idiots']
for title in book_titles:
    cursor.execute("INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)",
                   (title, student_id))


cursor.execute('''SELECT students.name, students.second_name, groups.title, books.title
                  FROM students
                  JOIN `groups` ON students.group_id = groups.id
                  JOIN books ON books.taken_by_student_id = students.id
                  WHERE students.id = %s''', (student_id,))
result = cursor.fetchall()
db.commit()

if len(result) > 0:
    student_info = result[0]
    student_first_name = student_info[0]
    student_last_name = student_info[1]
    group_title = student_info[2]
    book_titles = [book_info[3] for book_info in result]

    print(f"Student {student_first_name} {student_last_name} studies in {group_title} group "
          f"and has taken next books in library: {', '.join(book_titles)}")


db.close()
