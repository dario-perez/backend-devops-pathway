import json
import ipaddress
from typing import Any
from pathlib import Path

script_dir = Path(__file__).resolve().parent
file_path = script_dir



# --- SERVER CLASSES ---

class Server:
  def __init__(self, name: str, ip: str, status: str = "online"):
    self.name = name
    self.ip = ipaddress.ip_address(ip)
    self.status = status

  def to_dict(self) -> dict[str, Any]:
    return {"name": self.name, "ip": str(self.ip)}

  def toggle_status(self):
    self.status = "offline" if self.status == "online" else "online"

  def get_info(self):
    return f"Server: {self.name} | {self.ip} | Status: {self.status.upper()}"
  



class WebServer(Server):
  def __init__(self, name: str, ip: str, port: int, status: str = "online"):
    super().__init__(name, ip, status)
    self.port = int(port)

  def to_dict(self):
    data = super().to_dict()
    data["port"] = self.port
    return data

  def get_info(self):
    return f"{super().get_info()} | Port: {self.port}"



class DatabaseServer(Server):
  def __init__(self, name: str, ip: str, db_engine: str, status: str = "online"):
    super().__init__(name, ip, status)
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
    status = kwargs.get("status", "online")

    try:
      if "port" in kwargs:
          new_server = WebServer(name, ip, kwargs["port"], status)
      elif "db_engine" in kwargs:
          new_server = DatabaseServer(name, ip, kwargs["db_engine"], status)
      else:
          new_server = Server(name, ip)

      if tag not in self.servers_by_tag:
          self.servers_by_tag[tag] = []
      self.servers_by_tag[tag].append(new_server)
      return new_server
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

  def get_health_report(self):
    online = 0
    offline = 0
    for server_list in self.servers_by_tag.values():
      for s in server_list:
        if s.status == "online":
          online += 1
        elif s.status == "offline":
          offline += 1

    total = online + offline
    return f"HEALTH REPORT -> Total: {total} | Online: {online} | Offline: {offline}"


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

  srv1 = manager.add_server("Web-Srv", "1.1.1.1", "Prod", port=443)
  srv2 = manager.add_server("DB-Srv", "2.2.2.2", "Data", db_engine="PostgreSQL")
  manager.add_server("Generic", "3.3.3.3", "Test")

  if srv1:
    print(f"\n Toggling status for {srv1.name}")
    srv1.toggle_status()
  
  print(manager)
  print(manager.get_health_report())