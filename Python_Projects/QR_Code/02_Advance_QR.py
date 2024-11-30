import qrcode

# from PIL import Image
import qrcode.constants

qr=qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=10,border=4)

qr.add_data("Hello Content Data of the QR")

qr.make(fit=True)"""  """

img = qr.make_image(fill_color="#5c1111f5", back_color="white")
img.save("Advance_QR.png")

print("QR code generated and saved as 'Advance_QR.png'")
