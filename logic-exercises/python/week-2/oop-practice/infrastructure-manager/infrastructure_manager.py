import ipaddress

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
      new_server = Server(name, ip)
      if tag not in self.servers_by_tag:
        self.servers_by_tag[tag] = []
      self.servers_by_tag[tag].append(new_server)

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
    my_manager = InfrastructureManager()

    my_manager.add_server("srv-01", "192.168.1.1", "Web")
    my_manager.add_server("srv-02", "192.168.1.2", "DB")
    my_manager.add_server("srv-03", "192.168.1.3", "Web")

    print(my_manager)

    my_manager.remove_server("srv-03", "Web")

    print(my_manager)
