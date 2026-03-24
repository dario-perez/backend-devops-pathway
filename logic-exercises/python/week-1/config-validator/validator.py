import json
from pathlib import Path

base_path = Path(__file__).resolve().parent
access_file = base_path.parent / "data" / "validation_config.json"

required_keys = ["port", "database_url", "environment"]

def validation():
    try:
        with open(access_file, "r") as file:
            data = json.load(file)

        missing_keys = []
        for key in required_keys:
            if key not in data:
                missing_keys.append(key)
        
        if missing_keys:
            print(f"❌ Validation failed. Missing keys: {', '.join(missing_keys)}")
            return

        if not isinstance(data["port"], int):
            print(f"❌ Type Error: 'port' must be an integer, but got {type(data['port']).__name__}")
            return

        print(f"✅ System ready to launch on port: {data['port']}")

    except FileNotFoundError:
        print(f"⚠️ Error: File not found at {access_file}")
    except json.JSONDecodeError:
        print("⚠️ Error: JSON file is corrupted.")

validation()