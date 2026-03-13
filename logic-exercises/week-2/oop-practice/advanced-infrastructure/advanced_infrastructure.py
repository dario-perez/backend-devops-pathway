import datetime
from pathlib import Path



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

  def create_log(self, content):
    script_dir = Path(__file__).resolve().parent
    logs_dir = script_dir / "logs"
    file_path = logs_dir / "logs.txt"

    try:
      logs_dir.mkdir(parents=True, exist_ok=True)
      with open(file_path, "a", encoding="utf-8") as file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"\n====== LOG: {timestamp} ======\n")
        file.write(content)
        file.write("\n" + "="*30 + "\n")
        print(f"✅ Success: Report saved to {file_path}")
    except Exception as e:
        print(f"❌ Critical Error saving file: {e}")

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

  def __str__(self):
    return f"- {self.name} (IP: {self.ip})\n"



if __name__ == "__main__":
  manager = InfrastructureManager()
  srv1 = Server("Srv1", "192.168.1.1")
  srv2 = Server("Srv2", "192.168.1.2")

  manager.add_server(srv1, "Web")
  manager.add_server(srv2, "Web")

  print(manager.get_servers_by_tag("Web"))
  print(manager)

  final_summary = (
    f"{manager}\n"
    f"Tagged Servers: {manager.get_servers_by_tag("Web")}"
  )

  manager.create_log(final_summary)