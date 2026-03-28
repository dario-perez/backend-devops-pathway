import json
import ipaddress
from pathlib import Path

script_dir = Path(__file__).resolve().parent
file_path = script_dir

class Server:
    def __init__(self, name: str, ip: str):
      self.name = name
      self.ip = ipaddress.ip_address(ip)

class InfrastructureManager:
    def __init__(self):
      self.servers_by_tag = {}

    def add_server(self, name: str, ip: str, tag: str):
      """
      Creates a new Server instance and adds it to the infrastructure under a specific tag.
        
        Args:
            name (str): The hostname or identifier for the server.
            ip (str): The IP address string (will be validated by ipaddress module).
            tag (str): The category or group (e.g., 'Web', 'DB') to assign the server.
      """
      try:
        if not isinstance(ip, str):
          raise ValueError(f"IP must be a string, received '{ip}'\n")

        new_server = Server(name, ip)
        if tag not in self.servers_by_tag:
          self.servers_by_tag[tag] = []
        self.servers_by_tag[tag].append(new_server)

      except ValueError as e:
        print(f"Error adding server '{name}': {e}\n")

    def remove_server(self, name, tag):
      """
      Removes an existing Server from the infrastructure under a specific tag and name.
        
        Args:
            name (str): The hostname or identifier for the server.
            tag (str): The category or group (e.g., 'Web', 'DB') to assign the server.
      """
      if tag in self.servers_by_tag:
        for s in self.servers_by_tag[tag]:
          if s.name == name:
            self.servers_by_tag[tag].remove(s)
            break

        if not self.servers_by_tag[tag]:
          del self.servers_by_tag[tag]

    def load_file(self, filename):
      try:
        with open(file_path/filename, "r") as file:
          for line in file:
            parts = line.strip().split(",")

            if len(parts) != 3:
              print(f"Skipping invalid line: {line.strip()}")
              continue

            name, ip, tag = parts
            self.add_server(name, ip, tag)

          if not file:
            print("⚠️ Warning: File is empty.")

      except FileNotFoundError:
        print(f"❌ Error: {filename} not found.")
    
    def __str__(self):
      """Returns a formatted report of all registered servers grouped by tag."""
      report = []
      if not self.servers_by_tag:
        return "No servers registered."

      for tag, servers in self.servers_by_tag.items():
        names = ", ".join(s.name for s in servers)
        report.append(f"'{tag}': {names}")

      formated_report = "\n".join(report)
      return (
         f"=== Servers Infrastructure ===\n"
         "------------------------------\n"
         f"{formated_report}\n"
         "------------------------------\n"
      )



if __name__ == "__main__":
    manager = InfrastructureManager()

    manager.add_server("srv-01", "192,168.1.1", "Web")
    manager.add_server("srv-02", "192.168.1.2", "DB")
    manager.add_server("srv-03", "192.168.1.3", "Web")

    print(manager)

    manager.remove_server("srv-03", "Web")

    print(manager)

    manager.load_file("servers.txt")

    print(manager)