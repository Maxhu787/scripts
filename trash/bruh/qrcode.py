import pygrcode
import png
link = "google.com"
qr_code = pyqrcode.create(link)
qr_code.png("google.png", scale=5)