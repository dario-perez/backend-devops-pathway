import sys
import time

class Server:
  '''
  Represents a physical or virtual server in the infrastructure with reboot capabilities.

  Attributes:
    hostname (str): The unique name of the host.
    ip (str): Static IP address of the resource.
    is_online (bool): Connection status of the server.
  '''
  def __init__(self, hostname: str, ip: str):
    self.hostname = hostname
    self.ip = ip
    self.is_online = False
  
  def _print_progress_bar(self, current, total, length=40):
        '''Internal helper to render the progress bar in the console.'''
        progress = current / total
        filled_length = int(length * progress)
        # Using a solid block character and a shaded one for a better look
        bar = "█" * filled_length + "-" * (length - filled_length)
        
        # \r moves the cursor to the start of the line
        sys.stdout.write(f"\rProgress: [\033[92m{bar}\033[0m] {progress*100:.0f}%")
        sys.stdout.flush()

  def status_report(self):
    status = "ONLINE" if self.is_online else "OFFLINE"
    print(f"Status Report: Server: {self.hostname} | Status: {status}")

  def start_server(self):
    self.is_online = True
    print(f"Server: {self.hostname} | IP: {self.ip} | Status: ONLINE")

  def reboot(self):
    print(f"Rebooting server {self.hostname}")
    self.is_online = False

    # Simulation of the shutdown/startup sequence
    total_steps = 20
    for i in range(total_steps + 1):
        self._print_progress_bar(i, total_steps)
        time.sleep(0.2)  # Simulates loading services/drivers
        
    # Add a newline so the next print doesn't overwrite the bar
    print(f"\n[SUCCESS] Server {self.hostname} restarted successfully.")
    self.start_server()



class DatabaseServer(Server):
  def __init__(self, hostname: str, ip: str, db_name: str):
      super().__init__(hostname, ip)
      self.db_name = db_name

  def run_query(self, query: str):
    if self.is_online:
      print(f"✅ Executing {query} on database {self.db_name}")
    else:
      print(f"❌ Error: Cannot run query. Server {self.hostname} is OFFLINE.")


if __name__ == '__main__':
   my_db = DatabaseServer("DB-PROD", "10.0.0.5", "Sales_Data")
   my_db.run_query("SELECT * FROM users")
   my_db.reboot()
   my_db.status_report()
