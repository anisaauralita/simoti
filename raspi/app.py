import cv2
from time import sleep
import time
import sys
import RPi.GPIO as GPIO
from datetime import datetime

import mysql.connector
from datetime import datetime
import time
# import gridfs
# import pymongo
# from pymongo import MongoClient

# Koneksi ke database
# cluster = MongoClient("mongodb://localhost:27017")
# db = cluster["project_sic"]

#################################################################
dt = datetime.now()
ts = dt.strftime("_%d%m%Y_%H%M%S")
img_name = "FOTO{}.png".format(ts)

def take():
    # Konfigurasi kamera
    cam = cv2.VideoCapture(0)
    ret, frame = cam.read()
    

    # Mengambil gambar
    time.sleep(5)
    cv2.imwrite(img_name, frame)

    # Menampilkan pesan
    print("Foto disimpan dengan nama {}".format(img_name))

    # Mengimport GridFS
    # fs = gridfs.GridFS(db)
    # file = img_name

    # with open(file, 'rb') as f:
        # contents = f.read()

    # Mengupload gambar ke database
    # fs.put(contents, filename=file)

    # Menampilkan pesan
    # print("Foto telah diupload ke database!")



#################################################################

# Convert digital data to binary format
def convertToBinaryData(filename):
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData

#################################################################

# Fungsi kirim gambar ke database
def insertBLOB(comment, image):
    print("Sedang menyimpan foto ke dalam database")
    try:
        connection = mysql.connector.connect(host='ch01-id.tunnel.web.id',
                                         database='tnch25_projectsic',
                                         user='tnch25_projectsic',
                                         password='Bismillahi99')

        cursor = connection.cursor()
        sql_insert_blob_query = """ INSERT INTO log_data
                          (comment, image) VALUES (%s, %s)"""

        empPicture = convertToBinaryData(image)
        # file = convertToBinaryData(biodataFile)



        # Convert data into tuple format
        insert_blob_tuple = (comment, empPicture)
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
            print("Sedang menginisialisasi ulang sistem")

now = datetime.now()
sekarang = now.strftime("%H:%M:%S")

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def action(pin):
    print(sekarang, 'Asap Terdeteksi!')
    print('Menginisialisasi kamera')
    take()
    insertBLOB("Foto Baru", img_name)
    time.sleep(60)
    
GPIO.add_event_detect(23, GPIO.RISING)
GPIO.add_event_callback(23, action)

try:
    print('mendeteksi asap')
    while True:
        time.sleep(0.5)
except KeyboardInterrupt:
     GPIO.cleanup()
     sys.exit()

