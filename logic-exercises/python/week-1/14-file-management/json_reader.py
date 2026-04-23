import json

try:
    with open("employee.json", "r") as file:
        data = json.load(file)

    print("--- 👤 Employee Profile ---")
    print(f"Name: {data['name']}")
    print(f"Role: {data['role']}")
    print(f"Main Skill: {data['skills'][0]}")
    print(f"Other Skills: {', '.join(data['skills'][1:])}")
except FileNotFoundError:
    print("⚠️ Error: The JSON file was not found.")
except Exception as e:
    print(f"❌ Unexpected error: {e}")
