import psycopg2

class RowDGtw ():
    connection = None
    FIO = None
    PhotoPath = None

    def __init__(self, FIO, PhotoPath):
        self.create_connection("sm_app", "postgres", "root", "127.0.0.1", "5432")
        self.FIO = FIO
        self.PhotoPath = PhotoPath

    def create_connection(self, db_name, db_user, db_password, db_host, db_port):
        try:
            self.connection = psycopg2.connect(
                database=db_name,
                user=db_user,
                password=db_password,
                host=db_host,
                port=db_port,
            )
            print("Connection to PostgreSQL DB successful")
        except psycopg2.OperationalError as e:
            print(f"The error '{e}' occurred")
        return self.connection

    # def create_database(self, connection, db_name):
    #     connection.autocommit = True
    #     cursor = connection.cursor()
    #     query = "CREATE DATABASE " + db_name
    #     try:
    #         cursor.execute(query)
    #         print("Query executed successfully")
    #     except psycopg2.OperationalError as e:
    #         print(f"The error '{e}' occurred")
    #
    # def create_table (self):
    #     create_employees_table = """
    #     CREATE TABLE IF NOT EXISTS Employees (
    #       id SERIAL PRIMARY KEY,
    #       FIO TEXT NOT NULL,
    #       PhotoPath TEXT NOT NULL
    #     )
    #     """
    #     self.execute_query(self.connection, create_employees_table)
    # def create_table (self):
    #     create_employees_table = """
    #     CREATE TABLE IF NOT EXISTS Employees (
    #       id SERIAL PRIMARY KEY,
    #       FIO TEXT NOT NULL,
    #       PhotoPath TEXT NOT NULL
    #     )
    #     """
    #     self.execute_query(self.connection, create_employees_table)

    def execute_query(self, connection, query):
        connection.autocommit = True
        cursor = connection.cursor()
        try:
            cursor.execute(query)
            print("Query executed successfully")
        except psycopg2.OperationalError as e:
            print(f"The error '{e}' occurred")

    def Insert (self):
        insert_text = f"""
        INSERT INTO
          Employees (FIO, PhotoPath)
        VALUES
          ('{self.FIO}', '{self.PhotoPath}');
        """
        self.execute_query(self.connection, insert_text)

    def Delete (self):
        delete_text = f"""
        INSERT INTO
          Employees (FIO, PhotoPath)
        VALUES
          ('{self.FIO}', '{self.PhotoPath}');
        """
        self.execute_query(self.connection, delete_text)



if __name__ == "__main__":
    temp = RowDGtw('Elbow Elbowich', 'tempimage.png')
    temp.Insert()
#     create_database_name = "sm_app"
#     temp.create_database(temp.connection, create_database_name)