import qrcode as qr
#  qr is a alternate name of the qrcode

img=qr.make("Hello yuvraj")
# make fun is used to enter text in a qr

# save the file name Hello_Qr.png
img.save("Hello_Qr1.png",scale=50)
