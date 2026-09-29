import mysql.connector


class vechileListCreateRetrieveUpdateDelete:

    def __init__(self):

        # Connect to MySQL server first
        self.connection = mysql.connector.connect(
            user="root",
            password="horsepower12@",
            host="localhost"
        )

        self.cursor = self.connection.cursor()

        # Create database
        self.cursor.execute(
            "CREATE DATABASE IF NOT EXISTS vechile_db"
        )

        self.cursor.close()
        self.connection.close()

        # Connect to vechile_db
        self.connection = mysql.connector.connect(
            user="root",
            password="horsepower12@",
            host="localhost",
            database="vechile_db"
        )

        self.cursor = self.connection.cursor()

        # Create vehicle table
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS vechile_list (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), model VARCHAR(255), year INT, price DECIMAL(10, 2))"
        )       

        self.connection.commit()

        print("Connection established successfully")


#list

    def list(self):
        self.cursor.execute("SELECT * FROM vechile_list")
        records = self.cursor.fetchall()
        for row in records:
            print(row)

        else:
            print("No records found.")



    def create(self,name,model,year,price):
        self.cursor.execute("INSERT INTO vechile_list (name, model, year, price) VALUES (%s, %s, %s, %s)", (name, model, year, price))
        self.connection.commit()
        print("Record created successfully")


    def retrieve(self, id):
        self.cursor.execute("SELECT * FROM vechile_list WHERE id = %s", (id,))
        record = self.cursor.fetchone()
        if record:
            print(record)
        else:
            print("Record not found.")


    def update(self, id,name,model,year,price):
        query= "update from vechile_list set name %s, model = %s, year = %s, price = %s where id = %s"
        data = (name, model, year, price, id)
        self.cursor.execute(query, data)
        self.connection.commit()
        if self.cursor.rowcount > 0:
            print("Record updated successfully")
        else:
            print("No record updated.") 

v=vechileListCreateRetrieveUpdateDelete()
v.list()
# v.create("Toyota", "Camry", 2020, 25000.00)
# v.create("Honda", "Civic", 2021, 22000.00)
v.retrieve(1)
v.update(1, "Toyota", "Camry", 2020, 26000.00)