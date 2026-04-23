# Ticket ID: INFRA-500

import json
import psutil
import logging
from abc import ABC
from pathlib import Path

script_path = Path(__file__).resolve().parent
json_file = script_path / "data" / "config.json"
log_path = script_path / "monitor.log"



def load_config(filename):
    try:
        with open(filename, "r") as file:
            content = json.load(file)
        return content
    
    except FileNotFoundError:
        print("Error: File not found")
        return []



logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename=str(log_path),
    filemode='a'
)



class Storage(ABC):
    def __init__(self, name: str):
        self.name = name



class LocalDisk(Storage):
    def __init__(self, name: str, path: str):
        super().__init__(name)
        self.path = Path(path)

        try:
            self.capacity_gb = psutil.disk_usage(str(self.path)).total / (1024 ** 3)

        except (FileNotFoundError, OSError) as e:
            logging.error(f"Could not access path {path}: {e}")
            self.capacity_gb = 0

    def to_gb(self, number):
        return number / (1024 ** 3)

    def get_usage(self):
        current_usage = psutil.disk_usage(str(self.path))
        return current_usage.percent

    def get_disk_info(self):
        if self.capacity_gb == 0:
            return

        try:
            current_usage = psutil.disk_usage(str(self.path))
            print(f"\n--- Monitoring: {self.name} ---")
            print(f"Total space: {self.to_gb(current_usage.total):.2F} GB")
            print(f"Used space: {self.to_gb(current_usage.used):.2F} GB")
            print(f"Free space: {self.to_gb(current_usage.free):.2F} GB")
            print(f"Percent used: {current_usage.percent}%")

            logging.info(f"STORAGE_REPORT | Name: {self.name} | Usage: {current_usage.percent}%")

        except FileNotFoundError:
            print("Error: File not found")
        except Exception as e:
            print(f"An error has ocurred: {e}")



if __name__ == "__main__":
    config_data = load_config(json_file)

    fleet = []
    for disk_info in config_data:
        new_disk = LocalDisk(disk_info["name"], disk_info["path"])
        fleet.append(new_disk)

    for disk in fleet:
        disk.get_disk_info()
