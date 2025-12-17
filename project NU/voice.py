import os
import speech_recognition as sr 
from logger import log_attempt



def voice_passphrase(first_name,student_id):
    attempts = 0
    max_attempts = 3
    passphrase = "open now"
    print("===== Stage 2 : Passphrase =====")
    reco = sr.Recognizer() 
    try:
        with sr.Microphone() as source:
            print(" adjusting noise level... ")
            reco.adjust_for_ambient_noise(source)
            print(" Say The Passphrase... ")
            audio = reco.listen(source)
            text = reco.recognize_google(audio).lower()
        
        while attempts < max_attempts:
            if text == passphrase:
                print("passphrase matched! ✅")
                print("Access granted! ✅")

                log_attempt(first_name, "voice", f" Success ID: {student_id}") # تسجيل log 

                break

            else: 
                print("Passphrase is incorrect!")
                print("Access Denied!")
                attempts += 1 
                print(f"failed .. remaining attempts = {max_attempts - attempts}")  

                log_attempt(first_name, "voice", f" Fail ID: {student_id}") # تسجيل log 

        else: 
            print("System is locked" \
        "No more attempts left")
            log_attempt(first_name, "voice", f" Fail ID: {student_id} - System locked")
           

    except sr.UnknownValueError:
        print("[ERROR] Could not understand audio.")

        log_attempt(first_name, "voice", f" Fail ID: {student_id} - Unintelligible speech") 
        return False

    except sr.RequestError:
        print("[ERROR] Speech Recognition service unavailable.")

        log_attempt(first_name, "voice", f" Fail ID: {student_id} - Recognition service error")
        return False

    except Exception as e:
        print(f"[ERROR] Microphone/Audio error: {e}")
        #لبمفروض هسجل هنا log -----> f"FAILED - {e}")
        return False
    

