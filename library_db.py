import mysql.connector


class BookListCreateRetrieveUpdateDelete:

    def __init__(self):

        # Connect to MySQL server
        server_connection = mysql.connector.connect(
            user="root",
            password="horsepower12@",
            host="localhost"
        )

        server_cursor = server_connection.cursor()

        # Create database
        server_cursor.execute(
            "CREATE DATABASE IF NOT EXISTS library_db"
        )

        server_cursor.close()
        server_connection.close()

        # Connect to library_db
        self.connection = mysql.connector.connect(
            user="root",
            password="horsepower12@",
            host="localhost",
            database="library_db"
        )

        self.cursor = self.connection.cursor()

        # Create book table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS book (
                id INT AUTO_INCREMENT PRIMARY KEY,
                title VARCHAR(100) NOT NULL,
                author VARCHAR(100) NOT NULL,
                price DECIMAL(10, 2) NOT NULL,
                language VARCHAR(50) NOT NULL
            )
        """)

        self.connection.commit()

        print("Connection established successfully")


    # CREATE
    def create(self, title, author, price, language):

        query = """
            INSERT INTO book (title, author, price, language)
            VALUES (%s, %s, %s, %s)
        """

        values = (title, author, price, language)

        self.cursor.execute(query, values)
        self.connection.commit()

        print("Inserted data successfully")


    # LIST / READ ALL
    def list(self):

        query = "SELECT * FROM book"

        self.cursor.execute(query)

        records = self.cursor.fetchall()

        if records:
            for row in records:
                print(row)
        else:
            print("No records found")


    # RETRIEVE / READ ONE
    def retrieve(self, book_id):

        query = "SELECT * FROM book WHERE id = %s"

        self.cursor.execute(query, (book_id,))

        record = self.cursor.fetchone()

        if record:
            print(record)
        else:
            print("No record found")



    # DELETE
    def delete(self, book_id):

        query = "DELETE FROM book WHERE id = %s"

        self.cursor.execute(query, (book_id,))

        self.connection.commit()

        if self.cursor.rowcount > 0:
            print("Deleted data successfully")
        else:
            print("No record found")


#update

    def update(self, book_id, title, author, price, language):
        query = "update book set title = %s, author = %s, price = %s, language = %s where id =%s"
        data = (title, author, price, language, book_id)
        self.cursor.execute(query, data)
        self.connection.commit()
        if self.cursor.rowcount > 0:
            print("Updated data successfully")
        else:
            print("No record found")

b=BookListCreateRetrieveUpdateDelete()
# b.create("Python Programming", "John Doe", 29.99, "English")
b.list()
b.retrieve(1)
b.delete(5)
b.update(2, "Python Programming", "John Doe", 29.99, "Spanish")

 