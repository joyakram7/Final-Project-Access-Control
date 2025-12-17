from datetime import datetime
def log_attempt(user, stage, result):
    try:
        with open("door_logs.txt", "a") as f:
            f.write(f"[{datetime.now()}] User: {user} Stage: {stage} Result: {result}\n")
    except Exception as e:
        print(f"Logging error: {e}")