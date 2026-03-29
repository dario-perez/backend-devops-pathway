import json
import ipaddress
from typing import Any
from pathlib import Path

script_dir = Path(__file__).resolve().parent
file_path = script_dir



# --- SERVER CLASSES ---

class Server:
  def __init__(self, name: str, ip: str):
    self.name = name
    self.ip = ipaddress.ip_address(ip)

  def to_dict(self) -> dict[str, Any]:
    return {"name": self.name, "ip": str(self.ip)}

  def get_info(self):
    return f"Server: {self.name} | {self.ip}"



class WebServer(Server):
  def __init__(self, name: str, ip: str, port: int):
    super().__init__(name, ip)
    self.port = int(port)

  def to_dict(self):
    data = super().to_dict()
    data["port"] = self.port
    return data

  def get_info(self):
    return f"{super().get_info()} | Port: {self.port}"



class DatabaseServer(Server):
  def __init__(self, name: str, ip: str, db_engine: str):
    super().__init__(name, ip)
    self.db_engine = db_engine

  def to_dict(self):
    data = super().to_dict()
    data["db_engine"] = self.db_engine
    return data

  def get_info(self):
    return f"{super().get_info()} | Engine: {self.db_engine}"



# --- INFRASTRUCTURE MANAGER ---

class InfrastructureManager:
  def __init__(self):
    self.servers_by_tag = {}

  def add_server(self, name: str, ip: str, tag: str, **kwargs):
    """
    Supports extra arguments using **kwargs to decide which type of server to create.
    """
    try:
      if "port" in kwargs:
          new_server = WebServer(name, ip, kwargs["port"])
      elif "db_engine" in kwargs:
          new_server = DatabaseServer(name, ip, kwargs["db_engine"])
      else:
          new_server = Server(name, ip)

      if tag not in self.servers_by_tag:
          self.servers_by_tag[tag] = []
      self.servers_by_tag[tag].append(new_server)
    except Exception as e:
        print(f"❌ Error adding server '{name}': {e}")

  def json_load(self, filename):
    try:
      with open(filename, "r") as file:
        content = json.load(file)
        for tag, servers in content.items():
          for s in servers:
            self.add_server(s["name"], s["ip"], tag, **s)
    
    except Exception as e:
      print(f"Load error: {e}")

  def __str__(self) -> str:
    report = ["=== Infrastructure Report ==="]
    for tag, servers in self.servers_by_tag.items():
      report.append(f"\n[{tag}]")
      for s in servers:
        report.append(f" - {s.get_info()}")

    return "\n".join(report)



# --- SYSTEM TESTING ---

if __name__ == "__main__":
  manager = InfrastructureManager()

  manager.add_server("Web-Srv", "1.1.1.1", "Prod", port=443)
  manager.add_server("DB-Srv", "2.2.2.2", "Data", db_engine="PostgreSQL")
  manager.add_server("Generic", "3.3.3.3", "Test")
  
  print(manager)