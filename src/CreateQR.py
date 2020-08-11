import qrcode
import json

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

with open('info.json') as file:
    data = json.load(file)
    for box in data['arrayBoxes']:
        print('numeroBox:', box['numeroBox'])
        print('ruta:', box['ruta'])
        print('nombre paciente:', box['nombrePaciente'])
        qr.add_data(box['numeroBox'])
        qr.add_data(',')
        qr.add_data(box['ruta'])
        qr.add_data(',')
        qr.add_data(box['nombrePaciente'])

qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save('QR-Images/qrcode1.png')