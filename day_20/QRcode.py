import qrcode

data = input("Enter Text or Link: ")

img = qrcode.make(data)
img.save("qr.png")
img.show()
print("QR code Generated!!!!")

