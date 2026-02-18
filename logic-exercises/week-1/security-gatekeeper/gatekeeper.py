import json
import os

script_dir = os.path.dirname(__file__)

access_file = os.path.join(script_dir, "access_log.json")

try:
    with open(access_file, "r") as file:
        access = json.load(file)

    successes = 0
    failures = 0
    suspect_users = []

    for entry in access:
        if entry["success"]:
            successes += 1
        else:
            failures += 1
            if entry["user"] not in suspect_users:
                suspect_users.append(entry["user"])

    print("📊 --- SECURITY REPORT ---")
    print(f"✅ Success cases: {successes}")
    print(f"❌ Failure cases: {failures}")
    print(f"👤 Suspect users: {', '.join(suspect_users) if suspect_users else 'None'}")
    print("--------------------------")

except FileNotFoundError:
    print("⚠️ Error: Access log not found. Please check the source.")
except json.JSONDecodeError:
    print("⚠️ Error: The log file exists but it's corrupted or empty.")
