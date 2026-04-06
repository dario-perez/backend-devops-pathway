import json
import datetime
from pathlib import Path



script_dir = Path(__file__).resolve().parent
logs_dir = script_dir / "logs"
file_path = logs_dir / "logs.txt"



class InfrastructureManager():
    def __init__(self):
        self.tagged_servers = {}

    def add_server(self, server_obj, tag):
        if tag not in self.tagged_servers:
            self.tagged_servers[tag] = []

        self.tagged_servers[tag].append(server_obj)

        return self.tagged_servers

    def get_servers_by_tag(self, tag: str):
        if tag in self.tagged_servers:
            names = ', '.join([s.name for s in self.tagged_servers[tag]])
            return f"Servers with tag '{tag}': {names}"
        else:
            return f"Tag '{tag}' not found."

    def remove_server(self, name: str, tag: str):
        if tag in self.tagged_servers:
            target_server = None
            for s in self.tagged_servers[tag]:
                if s.name == name:
                    target_server = s
                    break

            if target_server != None:
                self.tagged_servers[tag].remove(target_server)

    def save_to_json(self, filename):
        try:
            data_to_save = {}
            for tag, servers in self.tagged_servers.items():
                list_of_servers_as_dicts = []

                for s in servers:
                    list_of_servers_as_dicts.append(s.to_dict())

                data_to_save[tag] = list_of_servers_as_dicts

            logs_dir.mkdir(parents=True, exist_ok=True)
            with open(logs_dir/filename, "w") as file:
                json.dump(data_to_save, file, indent=4)
            print(f"✅ Data persisted to {filename}\n")

        except Exception as e:
            print(f"❌ Critical Error saving file: {e}")

    def load_from_json(self, filename):
        try: 
            with open(logs_dir/filename, "r") as file:
                content = file.read().strip()
                if not content:
                        print("⚠️ Warning: File is empty.")
                        return
                json_file = json.loads(content)

                for tag, dicts_list in json_file.items():
                    for server_dict in dicts_list:
                        new_srv = Server(server_dict["name"], server_dict["ip"])
                        self.add_server(new_srv, tag)

                print("✅ Data loaded successfully from JSON.")

        except FileNotFoundError:
            print(f"❌ Error: {filename} not found.")

    def create_log(self, content):
        try:
            logs_dir.mkdir(parents=True, exist_ok=True)
            with open(file_path, "a", encoding="utf-8") as file:
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                file.write(f"\n====== LOG: {timestamp} ======\n")
                file.write(content)
                file.write("\n" + "="*30 + "\n")
                print(f"✅ Success: Report saved to {file_path}\n")
        except Exception as e:
                print(f"❌ Critical Error saving file: {e}")

    def read_log(self):
        try:
            with open(file_path, "r") as file:
                print(
                    f"LOG FILE ---->"
                    f"{file.read()}\n"
                )
        except FileNotFoundError:
            return f"File not found"

    def __str__(self):
        if not self.tagged_servers:
            return "Infrastructure is empty."

        output = "=== Infrastructure Report ===\n"
        for tag, servers in self.tagged_servers.items():
            clean_names = ", ".join([s.name for s in servers])
            output += f"Tag: [{tag}] -> Servers: {clean_names}\n"

        output += "=============================="
        return output



class Server():
    def __init__(self, name: str, ip: str):
        self.name = name
        self.ip = ip
    
    def to_dict(self):
        return {
            "name": self.name,
            "ip": self.ip
        }

    def __str__(self):
        return f"- {self.name} (IP: {self.ip})\n"



if __name__ == "__main__":
        manager = InfrastructureManager()

        print("--- Loading from disk ---")
        manager.load_from_json("infrastructure.json")

        print(manager)
