import sqlite3

# Connect to sqlite
connection = sqlite3.connect("student.db")

# Create a cursor object to insert a record, create table
cursor = connection.cursor()

# Create the table
table_info="""
CREATE TABLE STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25), SECTION VARCHAR(25),MARKS INT)
"""

cursor.execute(table_info)

# Insert some records
cursor.execute('''INSERT INTO STUDENT VALUES('KRISH','DATA SCIENCE', 'A',90)''')
cursor.execute('''INSERT INTO STUDENT VALUES('PARTH','COMPUTER SCIENCE', 'A',99)''')
cursor.execute('''INSERT INTO STUDENT VALUES('ARNAV','AERONAUTICAL', 'B',70)''')
cursor.execute('''INSERT INTO STUDENT VALUES('VINAY','ELECTRICAL', 'A',84)''')
cursor.execute('''INSERT INTO STUDENT VALUES('PRANAY','COMPUTER SCIENCE', 'C',34)''')
cursor.execute('''INSERT INTO STUDENT VALUES('ARYA','DATA SCIENCE', 'B',75)''')

# Display all the records

print("The inserted records are")
data=cursor.execute('''SELECT * FROM STUDENT''')
for row in data:
    print(row)

# Commit
connection.commit()
connection.close()