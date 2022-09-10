import mysql.connector
from datetime import datetime

def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData


def insertBLOB(id, comment, image):
    print("Sedang menyimpan foto ke dalam database")
    try:
        connection = mysql.connector.connect(host='localhost',
                                         database='project_sic',
                                         user='root',
                                         password='root')

        cursor = connection.cursor()
        sql_insert_blob_query = """ INSERT INTO log_data
                          (id, comment, image) VALUES (%s,%s,%s)"""

        empPicture = convertToBinaryData(image)
        # file = convertToBinaryData(biodataFile)



        # Convert data into tuple format
        insert_blob_tuple = (id, comment, empPicture)
        result = cursor.execute(sql_insert_blob_query, insert_blob_tuple)
        connection.commit()
        print("Foto berhasil disimpan", result)

    except mysql.connector.Error as error:
        print("Gagal menyimpan foto {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Koneksi database ditutup")

insertBLOB(1, "Eric", "C:\\Users\\smkbp\\Desktop\\project_sic\\py_mysql\\foto1.jpg")
insertBLOB(2, "Scott", "C:\\Users\\smkbp\\Desktop\\project_sic\\py_mysql\\foto2.png")
