import qrcode
text = input("Enter text/URL: ")
qrcode.make(text).save("qr.png")
print("QR Created: qr.png")
