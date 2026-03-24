class InfrastructureManager():
  def __init__(self):
    self.tagged_servers = {}

  def add_server(self, name: str, tag: str):
    if tag not in self.tagged_servers:
      self.tagged_servers[tag] = []
    if name not in self.tagged_servers[tag]:
      self.tagged_servers[tag].append(name)
  
  def get_servers_by_tag(self, tag: str):
    if tag in self.tagged_servers:
      return f"Servers with tag '{tag}': {", ".join(self.tagged_servers[tag])}"
    else:
      return f"Tag '{tag}' not found."
    
  def remove_server(self, name: str, tag: str):
    if tag in self.tagged_servers:
      self.tagged_servers[tag].remove(name)
    if not self.tagged_servers[tag]:
      del self.tagged_servers[tag]

  def __str__(self):
    if not self.tagged_servers:
      return "Infrastructure is empty."

    output = "=== Infrastructure Report ===\n"
    for tag, server in self.tagged_servers.items():
      clean_servers = ", ".join(server)
      output += f"Tag: [{tag}] -> Servers: {clean_servers}\n"
    
    output += "============================="
    return output



if __name__ == "__main__":
    manager = InfrastructureManager()
    manager.add_server("Srv1", "Web")
    manager.add_server("Srv2", "DB")
    manager.add_server("Srv3", "Web")
    print(manager)
    print(f"{manager.get_servers_by_tag("DB")}\n")
    manager.remove_server("Srv2", "DB")
    print(manager)