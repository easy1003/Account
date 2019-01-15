import mysql.connector

## raw mysql connection
conn = mysql.connector.connect(user='root', password='123098', database='account', use_unicode=True)
cursor = conn.cursor()
cursor.execute('select * from ACC_USER')
values = cursor.fetchall()
print(values)
cursor.close()
conn.close()