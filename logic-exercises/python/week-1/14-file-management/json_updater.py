import json

try:
    with open("employee.json", "r") as file:
        data = json.load(file)

    data["role"] = "Mid-Level Backend Developer (Road to Seoul)"
    data["skills"].append("JSON Mastery")

    with open("employee.json", "w") as file:
        json.dump(data, file, indent=4)

    print("✅ Profile updated successfully! You've leveled up.")

except FileNotFoundError:
    print("⚠️ Error: The file 'employee.json' doesn't exist.")
except Exception as e:
    print(f"❌ Unexpected error: {e}")
