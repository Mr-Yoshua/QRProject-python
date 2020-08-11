import cv2
import numpy as np
from pyzbar.pyzbar import decode

#img = cv2.imread('QR-Images/qrcode1.png')
# Establecer lectura por camara
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)


while True:
    ## mientras se pueda acceder a camara leer codigo QR desde camara, qr data es el contenido pts es para crear un cuadrado que limita el QR que se obtienen las dim desde
    # los datos de lectura, se utiliza para esta accion numpy
    success,img = cap.read()
    for barcode in decode(img):
        qrdata = barcode.data.decode('utf-8')
        print(qrdata)
        pts = np.array([barcode.polygon],np.int32)
        pts = pts.reshape((-1,1,2))
        cv2.polylines(img,[pts],True,(0,0,255),5)

    cv2.imshow('Result',img)
    cv2.waitKey(1)




