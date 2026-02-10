user_message = input("Input message: ")

try:
    with open("system.log", "a") as file:
        file.write(user_message + "\n")
    print("✅ Log saved successfully!")
except IOError, PermissionError:
    print(("⚠️ Alert: Disk is full or you do not have permissions"))
except Exception as e:
    print(f"❌ Unexpected error: {e}")
