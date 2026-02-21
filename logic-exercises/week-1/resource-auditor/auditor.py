import json
from pathlib import Path

base_path = Path(__file__).resolve().parent

metrics = base_path.parent / "data" / "metrics.json"


def auditor():
  try:
    with open(metrics, "r") as file:
      server = json.load(file)

      print("------ High Load Servers ------\n")

      for data in server:
        if data["status"] == "active" and data["cpu_usage"] > 80:
          print(f"{data['server_name']}")
          print(f"{data['status']}")
          print(f"{data['cpu_usage']}")
          print("-" * 20)

  except FileNotFoundError:
    print("⚠️ Error: Access log not found. Please check the source.\n")
  except json.JSONDecodeError:
    print("⚠️ Error: The log file exists but it's corrupted or empty.\n")

auditor()