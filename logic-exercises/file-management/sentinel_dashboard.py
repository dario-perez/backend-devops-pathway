import json

LOG_FILE = "health_log.json"

# Error messages
file_not_found = "File not found"
json_decode_error = "JSON file is corrupted"
no_permission = "Not enough permission"
type_error = "Not supported"
key_error = "Key not found in JSON file"
value_error = "Wrong data type"


# Dispay log history in JSON file
def display_logs():
    try:
        with open(LOG_FILE, "r") as file:
            logs = json.load(file)
        if logs == []:
            print("No log history found\n")
        else:
            for i, log in enumerate(logs, 1):
                print(f"--- Server {i} ---")
                print(f"Status: {log['status']}")
                print(f"CPU: {log['cpu']}")
                print(f"Memory: {log['mem']}\n")

    except PermissionError:
        print(no_permission)

    except (FileNotFoundError, json.JSONDecodeError):
        logs = []
        print(f"⚠️ {file_not_found} or {json_decode_error}")


# Allow manual server health check
def record_health(status, cpu, mem):
    try:
        try:
            with open(LOG_FILE, "r") as file:
                logs = json.load(file)

        except FileNotFoundError:
            logs = []
            print(file_not_found)

            logs.append({"status": status, "cpu": cpu, "mem": mem})
            with open(LOG_FILE, "w") as file:
                json.dump(logs, file, indent=4)

        except (TypeError, KeyError):
            logs = []
            print(f"{type_error} or {key_error}")

        check_logs = input("Would you like to check the logs? (Y/N)\n").lower()
        if check_logs == "y":
            display_logs()

    except Exception as e:
        print(f"✖ Error: Cannot continue. {e}\n")


# Clear all logs
def clear_logs():
    user_option = input(
        "⚠️ Warning: You are about to delete all logs. "
        "Are you sure that you want to proceed? "
        "Data cannot be recovered. (Y/N)\n"
    ).lower()
    if user_option == "y":
        with open(LOG_FILE, "w") as file:
            json.dump([], file)
        print("All logs were deleted.\n")


# User Interface
while True:
    print("====== SENTINEL DASHBOARD ======")
    print("-" * 32)
    user_option = input(
        "[1] View Server History.\n"
        "[2] Run Manual Health Check.\n"
        "[3] Clear All Logs.\n"
        "[4] Exit\n"
    )

    if user_option == 1:
        display_logs()
    elif user_option == 2:
        try:
            sv_status = input("Enter Server Status: \n").capitalize()
            sv_cpu = int(input("Enter Server CPU %: \n"))
            sv_mem = int(input("Enter Server Memory %: \n"))
            record_health(sv_status, sv_cpu, sv_mem)

        except ValueError:
            print(f"✖ {value_error}")

    elif user_option == 3:
        clear_logs()
    elif user_option == 4:
        print("Thank you for using Sentinel. Have a nice day.\n")
        break
    else:
        print("✖ You enter an invalid option.\n")
