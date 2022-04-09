'''import mysql.connector'''




'''import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE Bank")'''





'''import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database='Bank'
)
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE BankAtm (Name VARCHAR(255), CardNumber int, PIN int, BankBalance int,AccountNumber int)")'''




'''import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database='Bank'
)
mycursor = mydb.cursor()
sql = 'INSERT INTO BankAtm(Name, CardNumber, PIN, BankBalance, AccountNumber) VALUES (%s, %s, %s, %s, %s)'
val = [
 ('Akshay Gulve', 1111, 1111, 10000, 11111111),
 ('Pramod Thorat', 2222, 2222, 12000, 22222222),
 ('Varun Jadhav', 3333, 3333, 15000, 33333333),
 ('Akash Kawade', 4444, 4444, 25000, 44444444),
 ('Pravin Karpe', 5555, 5555, 60000, 55555555),
 ('Sagar Shinde', 6666, 6666, 75000, 66666666)
]
mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "record was inserted.")'''