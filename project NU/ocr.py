from PIL import Image, ImageOps
import pytesseract
import os
from datetime import datetime
from logger import log_attempt

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def preprocess_image(image_path):
    if not os.path.exists(image_path):
        print(f"Error: {image_path} not found.")
        return None
    try:
        img = Image.open(image_path)
        img = img.convert('L')  
        img = ImageOps.autocontrast(img)  
        max_size = (800, 800)
        img.thumbnail(max_size)
        return img
    except Exception as e:
        print(f"Error processing image: {e}")
        return None

def extract_text(img):
    if img is None:
        return None
    try:
        text = pytesseract.image_to_string(img)
        return text.strip()
    except Exception as e:
        print(f"OCR error: {e}")
        return None



def verify_user(image_path, first_name, student_id):
    img = preprocess_image(image_path)
    ocr_result = extract_text(img)

    if ocr_result:
        print(f"OCR Result:\n{ocr_result}")
        if first_name.lower() in ocr_result.lower() and student_id in ocr_result:
            print("OCR Verification: Success ✅")
            log_attempt(first_name, "OCR", f"Success ID: {student_id}")
            return True
        else:
            print("OCR Verification: Failed ❌")
            log_attempt(first_name, "OCR", f"Fail ID: {student_id}")
            return False
    else:
        print("No text extracted from image.")
        log_attempt(first_name, "OCR", f"Fail ID: {student_id}")
        return False




# mostafa
# hello :)
# i created a new branch 
# merge and push 