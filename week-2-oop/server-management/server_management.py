import sys
import time
import random
import datetime



class Server:
  def __init__(self, hostname: str, ip: str, service_name: str):
    self.hostname = hostname
    self.ip = ip
    self.service_name = service_name
    self.status = "OFFLINE"
    self.load = 0
    self.last_reboot = None

  def _print_progress_bar(self, current, total, length=40):
    '''Internal helper to render the progress bar in the console.'''
    progress = current / total
    filled_length = int(length * progress)
    bar = "█" * filled_length + "-" * (length - filled_length)

    sys.stdout.write(f"\rProgress: [\033[92m{bar}\033[0m] {progress*100:.0f}%")
    sys.stdout.flush()

  def startup(self):
    '''Sets status as ONLINE and print the last reboot date and time.'''
    chance = random.randint(0, 1)
    if chance == 1:
      self.status = "ONLINE"
      total_steps = 20
      for i in range(total_steps + 1):
          self._print_progress_bar(i, total_steps)
          time.sleep(0.2)
      self.last_reboot = datetime.datetime.now().strftime("%Y/%m/%d - %H:%M:%S")
    else:
      self.status = "OFFLINE"
      print(f"⚠️ Warning: Reboot process FAILED!")

    print(f"\n\n🚀 [SYSTEM] {self.hostname} is now {self.status.upper()}\n")

  def set_load(self, cpu_percentage: float):
    '''Sets the cpu percentage.'''
    self.load = cpu_percentage
    print(f"\n📊 [MONITOR] {self.hostname} load updated to {self.load}%.\n")

  def get_info(self):
    '''Prints the Server info based on __str__ format.'''
    print(self)
  
  def _get_extra_info(self):
    '''Hook method to be overridden by subclasses.'''
    return ""

  def __str__(self):
    header = "__________________________________\n"
    base_info = (
      f"--- {self.hostname} REPORT ---\n"
      f"Status: {self.status}\n"
      f"IP Address: {self.ip}\n"
      f"Service: {self.service_name}\n"
      f"CPU Load: {self.load}%\n"
      f"Last Boot: {self.last_reboot}\n"
    )
    extra = self._get_extra_info()
    footer = "__________________________________\n"

    return header + base_info + extra + footer



class DatabaseServer(Server):
  def __init__(self, hostname: str, ip: str, service_name: str, db_engine: str):
    super().__init__(hostname, ip, service_name)
    self.db_engine = db_engine

  def _get_extra_info(self):
    return f"\nDatabase Engine: {self.db_engine}\n"



class StorageServer(Server):
  def __init__(self, hostname: str, ip: str, service_name: str, capacity_gb: int):
    super().__init__(hostname, ip, service_name)
    self.capacity_gb = capacity_gb

  def _get_extra_info(self):
    return f"\nStorage Capacity: {self.capacity_gb} GB\n"



if __name__ == "__main__":
  servers_farm = [
      Server("WEB_PROD_01", "132.0.0.10", "Coupang Frontend"),
      DatabaseServer("DB_SQL_01", "132.0.0.20", "User Data", "PostgreSQL"),
      StorageServer("S3_BACKUP", "132.0.0.30", "Cloud Storage", 500),
      DatabaseServer("DB_REDIS", "132.0.0.40", "Cache System", "Redis"),
      Server("GATEWAY_LB", "132.0.0.50", "Load Balancer")
    ]
  
  online_servers = 0
  offline_servers = 0

  print(f"📊 Initializing infrastructure for {len(servers_farm)} servers...\n")
  
  for server in servers_farm:
    server.get_info()
    server.startup()
    server.get_info()
    # time.sleep(0.5)

    if server.status.upper() == "ONLINE":
      online_servers += 1
    else:
      offline_servers += 1

  print(
    f"Number of Servers: {len(servers_farm)}\n"
    f"Online Servers: {online_servers}\n"
    f"Offline Servers: {offline_servers}"
  )