#run this command in command prompt first -> pip install mysql-connector-python

import mysql.connector
conn = mysql.connector.connect(host="localhost",user="root",password="admin",charset="utf8")
print(conn)
myCursor = conn.cursor()
'''myCursor.execute("SHOW DATABASES")
for x in myCursor:
    print(x)'''
#Create a new Database
'''myCursor.execute("CREATE DATABASE hatim")
print("Done!")'''
'''print("-----------------Tables List---------------")
myCursor.execute("SHOW TABLES")
for x in myCursor:
    print(x)'''
#create a new table in selected database
'''myCursor.execute("CREATE TABLE students(id int PRIMARY KEY AUTO_INCREMENT,
s_name varchar(100),s_contact varchar(10),s_email varchar(150),s_dob DATE,s_age int)")
print("Done!")'''
#Insert a particular value in MySQL
'''try:
    sql ="insert into students(s_name,s_email,s_contact,s_dob,s_age) VALUES(%s,%s,%s,%s,%s)"
    val = ("Hatim K","hatimkanorwala0@gmail.com","0987654321","1990-03-03",48)
    myCursor.execute(sql, val)
    conn.commit()
    print("Value Inserted ",myCursor.rowcount)
    print("Last Value Inserted ", myCursor.lastrowid)
except mysql.connector.Error as error:
    print("Failed to insert row due to: {}".format(error))'''
#select data from MYSql
'''myCursor.execute("select * from students")
result = myCursor.fetchall()
for x in result:
    print(x) #Prints all the data in array
    print("ID: ", x[0], "\tName: ",x[1]) #Print specific column data'''
#Using where clause
'''myCursor.execute("select * from students where id=2")
result = myCursor.fetchall()
for x in result:
    print(x) #Prints all the data in array
    print("ID: ", x[0], "\tName: ",x[1]) #Print specific column data '''
#Select using specific columns
'''myCursor.execute("select id,s_name,s_contact from students")
result = myCursor.fetchall()
for x in result:
    print(x) #Prints all the data in array
    print("ID: ", x[0], "\tName: ",x[1], "\tContact: ",x[2]) #Print specific column data  '''
#Delete record
'''myCursor.execute("delete from students where id=2")
conn.commit()
print("Row Deleted: ",myCursor.rowcount)'''






