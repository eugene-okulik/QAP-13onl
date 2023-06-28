import mysql.connector as mysql

db = mysql.connect(
    user='qap',
    passwd='AVNS_kkO9k0GPxfmPRPop6cY',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='qap13'
)

cursor = db.cursor(dictionary=True)
# cursor.execute('SELECT * FROM students')
# cursor.execute('SELECT * FROM students WHERE id = 3')

# cursor.execute('UPDATE students SET group_id = 3 where id = 1')
# db.commit()
# name = input('put a name: ')
# cursor.execute("SELECT * FROM students WHERE name = %s and second_name = 'Stalin'", (name,))

# result = cursor.fetchall()
# print(result)

cursor.execute("INSERT INTO books (title) VALUES ('Python for dummies')")
db.commit()
print(cursor.lastrowid)

db.close()
