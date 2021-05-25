import qrcode
import json

#recibe datos de json
with open('info.json') as file:
    data = json.load(file)
    index = 0
    #for que itera sobre Json
    for box in data.items():
        #for que itera sobre Arrayboxes
        for elemento in box:
            for paciente in elemento:
                
                # Crea una instancia del QR
                qr = qrcode.QRCode(
                    version=1,
                    error_correction=qrcode.constants.ERROR_CORRECT_L,
                    box_size=10,
                    border=4,
                )
                # Agrega y crea la información a QR por cada objeto
                print('Info QR:', box[1][index])
                qr.add_data(box[1][index])
                qr.make(fit=True)
                img = qr.make_image(fill_color="black", back_color="white")
                img.save('QR-Images/qrcode'+str(index)+'.png')
                if index != len(elemento):
                    index+=1;
            

