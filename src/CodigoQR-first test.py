import qrcode 
from PIL import Image


cadena = input("introduzca info para qr: ")
imagen = qrcode.make(cadena)

### Generacion de Imagen QR
nombre_imagen = input("introduzca nombre para qr :")+'.png'
archivo_imagen = open('QR-images/'+nombre_imagen,'wb')
imagen.save(archivo_imagen)
archivo_imagen.close()

ruta_imagen = "QR-Images/" + nombre_imagen
Image.open(ruta_imagen).show()

