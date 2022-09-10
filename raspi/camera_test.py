import cv2
#import mysql.connector
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
    time.sleep(3)
    cv2.imwrite(img_name, frame)

    # Menampilkan pesan
    print("Foto disimpan dengan nama {}".format(img_name))

take()