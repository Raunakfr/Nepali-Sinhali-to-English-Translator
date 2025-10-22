# ocr_module.py
import pytesseract
from pdf2image import convert_from_path
from PIL import Image

# Set tesseract path if needed
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text_from_image(image_path, lang_code="eng"):
    return pytesseract.image_to_string(Image.open(image_path), lang=lang_code)

def extract_text_from_pdf(pdf_path, lang_code="eng"):
    pages = convert_from_path(pdf_path)
    text = ""
    for page in pages:
        text += pytesseract.image_to_string(page, lang=lang_code) + "\n"
    return text
