import pytesseract
import cv2
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
img_path="kpay.jpg"
img=cv2.imread(img_path)

extracted_text = pytesseract.image_to_string(img)
print(extracted_text.strip())

cv2.imshow("image",img)
cv2.waitKey(0)