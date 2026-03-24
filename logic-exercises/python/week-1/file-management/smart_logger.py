user_action = input("What action do you want to take? (Read/Write): ")
action = user_action.lower()

try:
    if action == "read":
        with open("system.log", "r") as file:
            print(f"System.log: \n{file.read()}")
    elif action == "write":
        with open("system.log", "a") as file:
            user_message = input("Input message: ")
            file.write(user_message + "\n")
    else:
        print("Incorrect action")
except FileNotFoundError:
    print("⚠️ Error: The log file does not exist yet.")
except (IOError, PermissionError):
    print(("⚠️ Alert: Disk is full or you do not have permissions"))
except Exception as e:
    print(f"❌ Unexpected error: {e}")
