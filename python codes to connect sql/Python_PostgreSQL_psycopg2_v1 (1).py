# Python & PostgreSQL
# Connect To PostgreSQL Database Server using Python

pip install psycopg2
import psycopg2

# conn = psycopg2.connect("dbname=dvdrental user=postgres password=postgres")

conn = psycopg2.connect(
    host="localhost",
    user="postgres",
    password="Mohan@1610")

conn.autocommit = True
cur = conn.cursor()

# Preparing query to create a database
sql = "CREATE database mydb3";

cur.execute(sql)

conn = psycopg2.connect(
    host="localhost",
    dbname="mydb3",
    user="postgres",
    password="Mohan@1610")

conn.autocommit = True
cur = conn.cursor()


# Drop table if table exists
# cur.execute("DROP TABLE IF EXISTS emp")

#Creating table as per requirement
sql ='''CREATE TABLE EMPLOYEE(
   NAME CHAR(8) NOT NULL,
   ID INT, AGE INT,
   SEX CHAR(1),
   INCOME FLOAT)'''

cur.execute(sql)
conn.commit()

# Preparing SQL queries to INSERT a record into the database.
cur.execute('''INSERT INTO EMPLOYEE(NAME, ID, AGE, SEX, INCOME) VALUES ('Sharat', 1, 40, 'M', 11000)''')
cur.execute('''INSERT INTO EMPLOYEE(NAME, ID, AGE, SEX, INCOME) VALUES ('Vinay', 5, 20, 'M', 6000)''')
cur.execute('''INSERT INTO EMPLOYEE(NAME, ID, AGE, SEX, INCOME) VALUES ('Sharukh', 2, 25, 'M', 8300)''')
cur.execute('''INSERT INTO EMPLOYEE(NAME, ID, AGE, SEX, INCOME) VALUES ('Sam', 3, 26, 'F', 10000)''')
cur.execute('''INSERT INTO EMPLOYEE(NAME, ID, AGE, SEX, INCOME) VALUES ('Trump', 10, 24, 'F', 8000)''')

# Commit your changes in the database
conn.commit()

# Select qurey
cur.execute('''SELECT * from EMPLOYEE''')

# 1st row from the table
result = cur.fetchone();
print(result)

# All rows from the table
result = cur.fetchall();
print(result)


# Inserting many rows 
insert_stmt = "INSERT INTO EMPLOYEE (NAME, ID, AGE, SEX, INCOME) VALUES (%s, %s, %s, %s, %s)"

data = [('Krish', 6, 19, 'M', 2000), 
   ('Raj', 20, 4, 'M', 7000),
   ('Ram', 8, 25, 'M', 5000),
   ('Mac', 7, 26, 'M', 2000)]

cur.executemany(insert_stmt, data)
conn.commit()

# Where condition
cur.execute("SELECT * from EMPLOYEE WHERE AGE <23")
print(cur.fetchall())

# Update command
sql = "UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = 'M'"
cur.execute(sql)

# Select qurey
cur.execute('''SELECT * from EMPLOYEE''')

# All rows from the table
result = cur.fetchall();
print(result)

# 2nd Table
sql ='''CREATE TABLE EMPADD(
   NAME VARCHAR(10) NOT NULL,
   ID INT NOT NULL, CONTACT INT)'''

cur.execute(sql)
conn.commit()

# Inserting many rows 
insert_stmt = "INSERT INTO EMPADD (NAME, ID, CONTACT) VALUES (%s, %s, %s)"

data1 = [('Krish', 6, 19204212), 
   ('Raj', 20, 47006424),
   ('Ramya', 8, 25556565),
   ('Mac', 7, 26256556)]

cur.executemany(insert_stmt, data1)
conn.commit()


# Join Command
sql = '''SELECT EMPLOYEE.NAME, EMPLOYEE.ID, EMPLOYEE.SEX, EMPLOYEE.INCOME, EMPADD.CONTACT from EMPLOYEE INNER JOIN EMPADD ON EMPLOYEE.ID = EMPADD.ID'''
cur.execute(sql)

result = cur.fetchall();
print(result)



#Deleting records
cur.execute('''DELETE FROM EMPLOYEE WHERE AGE > 25''')

# Droping EMPLOYEE table 
cur.execute("DROP TABLE EMPLOYEE")
conn.commit()


#Closing the connection
conn.close()


