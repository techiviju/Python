import pyqrcode
from random import randrange

link = input("Enter a link to generate QR code :-")

qr=pyqrcode.create(link)

qr.png('Wqr.png',scale=15)