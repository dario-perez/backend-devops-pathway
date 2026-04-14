import json

server_config = {"ip": "192.168.1.1", "port": 8000, "status": "online"}

try:
    with open("config.json", "w") as file:
        json.dump(server_config, file, indent=4)
    print("✅ JSON config saved!")
except Exception as e:
    print(f"❌ Error: {e}")
