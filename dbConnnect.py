import mysql.connector

mydb = mysql.connector.connect(host = "localhost", user = "root",password = "1234",database = "test");

mycursor = mydb.cursor()
'''
mycursor.execute("CREATE DATABASE dbConnect")

mycursor.execute("SHOW DATABASES")
for i in mycursor:
    print(i)

mycursor.execute("CREATE TABLE students(name VARCHAR(50),email VARCHAR(80),age INTEGER(3),stdnt_id INTEGER AUTO_INCREMENT PRIMARY KEY)")

mycursor.execute("SHOW TABLES")
for _ in mycursor:
    print(_[0])

sql1 = "INSERT INTO students(name,email,age) VALUES (%s, %s, %s) "
record1 = ("somesh","somesh.routray11@gmail.com",25)


mycursor.execute(sql1,record1)
mydb.commit()

SQL2 = "select * from employee"
mycursor.execute(SQL2)

mycursor.execute("SHOW DATABASES")
for i in mycursor:
   print(i)
'''
def InsertEmp(mydb):
   mycursor = mydb.cursor()
   mycursor.execute("insert into employee values(%s,%s,%s)",('Jackman','TestUser',000000))
   mydb.commit()
   print(mycursor.rowcount,'Record inserted')

def DisplayEmp(mydb):
   mycursor = mydb.cursor()
   mydb = mysql.connector.connect(host="localhost", user="root", password="1234", database="test");
   mycursor = mydb.cursor()
   sql2 = 'select * from employee'
   mycursor.execute(sql2)
   print('-------------Displaying values--------------------')
   for i in mycursor:
      print(i)

def UpdateEmp(mydb):
   mycursor = mydb.cursor()

   mycursor.execute("update employee set dept = %s, salary = %s where name = %s", ('Test',9999999,'Jackman'))

   mydb.commit()
   print(mycursor.rowcount, 'record updated')
'''
def DeleteEmp(mydb):
   mycursor = mydb.cursor()

   # "DELETE FROM customer WHERE customer_id = %(id)s", {'id': 1234}
   #"DELETE FROM customer WHERE customer_id = :id", {'id': 1234}

   mycursor.execute("delete from employee where name = %s",('Jackman',))
   mydb.commit()
   print(mycursor.rowcount, 'record deleted')
'''
#mydb = mysql.connector.connect(host="localhost", user="root", password="1234", database="test")

#mycursor = mydb.cursor()

InsertEmp(mydb)
DisplayEmp(mydb)
UpdateEmp(mydb)
#DeleteEmp(mydb)
