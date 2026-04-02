import ipaddress
from typing import Any
from pathlib import Path
from abc import ABC, abstractmethod

script_dir = Path(__file__).resolve().parent
file_path = script_dir



# --- SERVER CLASSES ---

class Server(ABC):
  def __init__(self, name: str, ip: str, status: str = "online"):
    self.name = name
    self.ip = ipaddress.ip_address(ip)
    self.status = status

  @abstractmethod
  def get_info(self):
    """Returns base information about the server."""
    return f"Server: {self.name} | {self.ip} | {self.status.upper()}"

  @abstractmethod
  def to_dict(self) -> dict[str, Any]:
    """Converts the instance in a base dictionary."""
    return {"name": self.name, "ip": str(self.ip), "status": self.status}

  def toggle_status(self):
    """Switches the status between online and offline."""
    self.status = "offline" if self.status == "online" else "online"

  def run_maintenance(self):
    return f"Server '{self.name}' is rebooting."



class WebServer(Server):
  def __init__(self, name: str, ip: str, port: int, status: str = "online"):
    super().__init__(name, ip, status)
    self.port = port

  def get_info(self):
    return f"{super().get_info()} | Port: {self.port}"

  def to_dict(self):
    data = super().to_dict()
    data["port"] = self.port
    return data

  def run_maintenance(self):
    return f"Rebooting Nginx Service.\n{super().run_maintenance()}"



class DatabaseServer(Server):
  def __init__(self, name: str, ip: str, db_engine: str, status: str = "online"):
    super().__init__(name, ip, status)
    self.db_engine = db_engine

  def get_info(self):
    return f"{super().get_info()} | Engine: {self.db_engine}"

  def to_dict(self):
    data = super().to_dict()
    data["db_engine"] = self.db_engine
    return data

  def run_maintenance(self):
    return f"Creating backup.\n{super().run_maintenance()}"



# --- INFRASTRUCTURE MANAGER ---

class InfrastructureManager:
  def __init__(self):
    self.servers_by_tag = {}

  def add_server(self, name: str, ip: str, tag: str, **kwargs):
    status = kwargs.get("status", "online")
    try:
      if "port" in kwargs:
          new_srv = WebServer(name, ip, kwargs["port"], status)
      elif "db_engine" in kwargs:
          new_srv = DatabaseServer(name, ip, kwargs["db_engine"], status)
      else:
          # Nota: Si intentamos crear un Server() aquí, Python lanzará el TypeError 
          # porque ahora es Abstracto. Esto nos obliga a definir el tipo.
          print(f"⚠️ Cannot create generic server for '{name}'. Must be Web or DB.")
          return None

      if tag not in self.servers_by_tag:
          self.servers_by_tag[tag] = []
      self.servers_by_tag[tag].append(new_srv)
      return new_srv
    except Exception as e:
      print(f"❌ Error: {e}")

  def get_health_report(self):
    online = sum(1 for s_list in self.servers_by_tag.values() for s in s_list if s.status == "online")
    offline = sum(1 for s_list in self.servers_by_tag.values() for s in s_list if s.status == "offline")
    return f"📊 Health: {online} Online / {offline} Offline"

  def __str__(self):
    report = ["\n=== Infrastructure Report ==="]
    for tag, s_list in self.servers_by_tag.items():
      report.append(f"[{tag}]")
      for s in s_list:
        report.append(f" - {s.get_info()}")
    return "\n".join(report)



# --- SYSTEM TESTING ---

if __name__ == "__main__":
  manager = InfrastructureManager()
  manager.add_server("Srv-Web", "1.1.1.1", "Prod", port=80)
  manager.add_server("Srv-DB", "2.2.2.2", "Prod", db_engine="MySQL")

  print(manager)

  print(manager.get_health_report())