'''while using this mysql database makesure that in your computer system mysql is to be pre installed
or if already installed then make sure that you need to make some changes
in the program as below where 

  host="localhost", 
  user="root", 
  password="root"

in this data make sure you have to update as per your database info

i created database on sample base you can edit and make changes in this database'''


import mysql.connector


import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE AlterBank")


import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database='AlterBank'
)
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE BankAtm (Name VARCHAR(255), CardNumber int, PIN int, BankBalance float,AccountNumber int)")


import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database='AlterBank'
)
mycursor = mydb.cursor()
sql = 'INSERT INTO BankAtm(Name, CardNumber, PIN, BankBalance, AccountNumber) VALUES (%s, %s, %s, %s, %s)'
val = [
 ('Akshay Gulve', 1111, 1111, 10000.00, 11111111),
 ('Pramod Thorat', 2222, 2222, 12000.00, 22222222),
 ('Varun Jadhav', 3333, 3333, 15000.00, 33333333),
 ('Akash Kawade', 4444, 4444, 25000.00, 44444444),
 ('Pravin Karpe', 5555, 5555, 60000.00, 55555555),
 ('Sagar Shinde', 6666, 6666, 75000.00, 66666666)
]
mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "record was inserted.")