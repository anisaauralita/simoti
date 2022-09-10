# Membuat Tabel
import mysql.connector

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='project_sic',
                                         user='root',
                                         password='root')

    mySql_Create_Table_Query = """CREATE TABLE `Python_Employee`
                                ( `id` INT NOT NULL ,
                                `name` TEXT NOT NULL ,
                                `photo` BLOB NOT NULL ,
                                `biodata` BLOB NOT NULL ,
                                    PRIMARY KEY (`id`))
                                """

    cursor = connection.cursor()
    result = cursor.execute(mySql_Create_Table_Query)
    print("Laptop Table created successfully ")

except mysql.connector.Error as error:
    print("Failed to create table in MySQL: {}".format(error))
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")