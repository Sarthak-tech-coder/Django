from pyqrcode import *
import cv2
def generator(message):
    qr = QRCode(message)
    qr.show()

if __name__ == "__main__":
    generator("www.google.com")