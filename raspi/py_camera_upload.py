import cv2
from datetime import datetime
import gridfs
import pymongo
from pymongo import MongoClient

# Koneksi ke database
cluster = MongoClient("mongodb://localhost:27017")
db = cluster["project_sic"]

def take():
    # Konfigurasi kamera
    cam = cv2.VideoCapture(0)
    ret, frame = cam.read()
    dt = datetime.now()
    ts = dt.strftime("_%d%m%Y_%H%M%S")
    img_name = "FOTO{}.png".format(ts)

    # Mengambil gambar
    cv2.imwrite(img_name, frame)

    # Menampilkan pesan
    print("Foto disimpan dengan nama {}".format(img_name))

    # Mengimport GridFS
    fs = gridfs.GridFS(db)
    file = img_name

    with open(file, 'rb') as f:
        contents = f.read()

    # Mengupload gambar ke database
    fs.put(contents, filename=file)

    # Menampilkan pesan
    print("Foto telah diupload ke database!")

take()