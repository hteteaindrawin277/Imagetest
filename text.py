import cv2

import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
img = cv2.imread('kpay.jpg')
img = cv2.resize(img,None,fx=0.5,fy=0.5)

text=pytesseract.image_to_string(img)
print(text)
cv2.imshow("img",img)
cv2.waitKey(0)