import mysql.connector

# Create Connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345678"
)


mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE my_first_db")

# Check if Database Exists
mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(2, x)

# Create Connection to Database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345678",
    database="my_first_db"
)

# Creating a Table
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE students (id INT, name VARCHAR(255))")
# Creating a Table
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE employee (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), salary INT(6))")

# Check if Table Exists

mycursor = mydb.cursor()
mycursor.execute("SHOW TABLES")

for x in mycursor:
    print(3, x)


# Modify primary key on an existing table
mycursor = mydb.cursor()
mycursor.execute("ALTER TABLE students MODIFY id INT AUTO_INCREMENT PRIMARY KEY")

# Insert Into Table
mycursor = mydb.cursor()
sql = "INSERT INTO students (id, name) VALUES (%s, %s)"
val = ("01", "John")
mycursor.execute(sql, val)

mydb.commit()
print(mycursor.rowcount, "record inserted.")

mycursor = mydb.cursor()
sql = "INSERT INTO employee (id, name, salary) VALUES (%s, %s, %s)"
val = ("01", "John", 10000)
mycursor.execute(sql, val)

mydb.commit()
print(mycursor.rowcount, "record inserted.")

# Select From a Table
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM students")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM employee")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
