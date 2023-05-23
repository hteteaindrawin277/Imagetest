from django.shortcuts import render
import pytesseract
from PIL import Image

def extract_text(request):
    if request.method == 'POST' and request.FILES['image']:
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        image = request.FILES['image']
        img = Image.open(image)
        text = pytesseract.image_to_string(img)
        return render(request, 'extracted_text.html', {'text': text})
    return render(request, 'extract_text.html')
