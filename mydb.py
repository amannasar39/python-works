import mysql.connector
# establish connection between mysql server and python code
con=mysql.connector.connect(user="root",password="horsepower12@",host="localhost")
#it returns a connection object which is used to connect to the database
c=con.cursor()
#query to create a database
querry="create database school_db1"
c.execute(querry)
print("database created successfully")

c.close()
con.close()