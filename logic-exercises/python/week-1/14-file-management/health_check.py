import json


def record_health(status, cpu_usage, memory_usage, file_name="health_log.json"):
    try:
        try:
            with open(file_name, "r") as file:
                logs = json.load(file)

        except (FileNotFoundError, json.JSONDecodeError):
            logs = []

        logs.append({"status": status, "cpu": cpu_usage, "mem": memory_usage})
        with open(file_name, "w") as file:
            json.dump(logs, file, indent=4)
        print("✅ Data added correctly.")

    except Exception as e:
        print(f"❌ Error: Failed to save log {e}")


record_health("Healthy", 20, 45)
record_health("Warning", 85, 60)
record_health("Critical", 98, 95)

show_logs = input("Do you want to print health_log file in console? (Y/N)\n").lower()

if show_logs == "y":
    with open("health_log.json", "r") as file:
        logs = json.load(file)
    for i, log in enumerate(logs, 1):
        print(f"--- Server {i} ---")
        print(f"Status: {log['status']}")
        print(f"CPU: {log['cpu']}")
        print(f"Memory: {log['mem']}\n")
