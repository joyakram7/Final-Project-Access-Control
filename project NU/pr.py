from PIL import Image, ImageOps
import pytesseract
import os
from datetime import datetime

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

def log_attempt(user, stage, result):
    try:
        with open("door_logs.txt", "a") as f:
            f.write(f"[{datetime.now()}] User: {user} Stage: {stage} Result: {result}\n")
    except Exception as e:
        print(f"Logging error: {e}")

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

def main():
    students = [
        {"first_name": "Joy", "student_id": "2123026"},
        {"first_name": "Mostafa", "student_id": "FCI/2023/102"},
        {"first_name": "Kerolos", "student_id": "2123251"},
    ]

    first_name_input = input("Enter your first name: ").strip()

    student = next((s for s in students if s["first_name"].lower() == first_name_input.lower()), None)

    if student:
        image_path = input("Enter path to your ID image: ").strip()
        result = verify_user(image_path, student['first_name'], student['student_id'])
        if result:
            print("Proceed to Voice Stage ✅")
        else:
            print("OCR failed. Cannot proceed to Voice Stage ❌")
    else:
        print("First name not found in the system. ❌")

if __name__ == "__main__":
    main()


# mostafa
# hello :)