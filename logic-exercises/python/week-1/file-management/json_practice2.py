import json

employee = {
    "name": "Dario",
    "role": "Backend Developer Trainee",
    "skills": ["Python", "Git", "Error Handling"],
}

try:
    with open("employee.json", "w") as file:
        json.dump(employee, file, indent=4)
        print("✅ JSON file saved!")
except Exception as e:
    print(f"❌ Error: {e}")
