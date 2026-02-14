import json

try:
    with open("server.json", "r") as file:
        data = json.load(file)

    data["online"] = False

    with open("server.json", "w") as file:
        json.dump(data, file, indent=4)

    print("✅ Server status has changed.")

except FileNotFoundError:
    print("⚠️ Error: The file 'server.json' doesn't exist.")
except Exception as e:
    print(f"❌ Unexpected error: {e}")
