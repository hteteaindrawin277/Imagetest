import cv2
import pytesseract

img = cv2.imread('kpay.jpg')

config = ('-l eng --oem 1 --psm 3')

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
text = pytesseract.image_to_string(img,config=config)

text = text.split('\n')
print(text)