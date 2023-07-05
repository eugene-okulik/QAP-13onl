import mysql.connector as mysql

db = mysql.connect(
    user='qap',
    passwd='AVNS_kkO9k0GPxfmPRPop6cY',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='qap13'
)
cursor = db.cursor()

group_name = 'GPN-737-800MAX'
start_date = '2023-01-01'
end_date = '2023-12-12'
cursor.execute("INSERT INTO `groups` (title, start_date, end_date) VALUES (%s, %s, %s)",
               (group_name, start_date, end_date,))
group_id = cursor.lastrowid

first_name = 'Leo'
last_name = 'Messi'
cursor.execute("INSERT INTO students (name, second_name, group_id) VALUES (%s, %s, %s)",
               (first_name, last_name, group_id))
student_id = cursor.lastrowid


book_title = ['From Zero To Hero', 'How I became a millionaire.']
for title in book_title:
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
    first_name = student_info[0]
    last_name = student_info[1]
    group_title = student_info[2]
    book_titles = [book_info[3] for book_info in result]

    print(f"Student {first_name} {last_name} studies in {group_title} group "
          f"and has taken next books in library: {', '.join(book_titles)}")

db.close()
