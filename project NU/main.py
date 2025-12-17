from ocr import verify_user
from voice import voice_passphrase
from logger import log_attempt



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
        result = verify_user (image_path, student['first_name'], student['student_id']) #هياخد ال ----> student['first_name'],student['student_id'] هو ال -----> first_name , student_id 
        if result:
            print("Proceed to Voice Stage ✅")

            voice_passphrase(student['first_name'],student["student_id"]) # take these parameters to save logs with log_attempt()
        
        else:
            print("OCR failed. Cannot proceed to Voice Stage ❌")

    else:
        print("First name not found in the system. ❌")
    

if __name__ == "__main__":
    main()