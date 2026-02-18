import json


def save_log(message, file_name="system.json"):
    try:
        try:
            with open(file_name, "r") as file:
                logs = json.load(file)
        except FileNotFoundError:
            logs = []

            logs.append({"message": message, "status": "info"})

        with open(file_name, "w") as file:
            json.dump(logs, file, indent=4)
        print("✅ Log saved professionally.")

    except Exception as e:
        print(f"❌ Failed to save log: {e}")


save_log("Server started")
save_log("User logged in")
