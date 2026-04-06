import sys
import time
import random
import datetime
from pathlib import Path


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
        try:
            self.load = float(cpu_percentage)
            print(f"\n📊 [MONITOR] {self.hostname} load updated to {self.load}%.\n")

        except:
            print(f"❌ Error in {self.hostname}. Invalid load value: '{cpu_percentage}'")

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


def save_report_to_file(content):
        '''Saves the final execution summary to a txt file in a logs folder.'''
        script_dir = Path(__file__).resolve().parent
        logs_dir = script_dir / "logs"
        file_path = logs_dir / "server_report.txt"

        try:
                logs_dir.mkdir(parents=True, exist_ok=True)
                with open(file_path, "a", encoding="utf-8") as file:
                        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        file.write(f"\n=== REPORT LOG: {timestamp} ===\n")
                        file.write(content)
                        file.write("\n" + "="*30 + "\n")
                print(f"✅ Success: Report saved to {file_path}")
        except Exception as e:
                print(f"❌ Critical Error saving file: {e}")



if __name__ == "__main__":
        servers_farm = [
                Server("WEB_PROD_01", "132.0.0.10", "Coupang Frontend"),
                DatabaseServer("DB_SQL_01", "132.0.0.20", "User Data", "PostgreSQL"),
                StorageServer("S3_BACKUP", "132.0.0.30", "Cloud Storage", 500),
                DatabaseServer("DB_REDIS", "132.0.0.40", "Cache System", "Redis"),
                Server("GATEWAY_LB", "132.0.0.50", "Load Balancer")
        ]
    
        print(f"📊 Initializing infrastructure for {len(servers_farm)} servers...\n")
    
        for i, server in enumerate(servers_farm, 1):
                print(f"--- Processing Server {i}/{len(servers_farm)} ---")
                
                # Optimización: Carga condicional en una sola línea
                server.set_load(45.5 if i % 2 != 0 else "ERROR_DATA")
                
                server.startup()
                server.get_info()
                print(f"\n{'#' * 40}\n")
                time.sleep(0.3)

        # Optimización: Conteo elegante usando generadores
        online_count = sum(1 for s in servers_farm if s.status.upper() == "ONLINE")
        
        final_summary = (
                f"Number of Servers: {len(servers_farm)}\n"
                f"Online Servers: {online_count}\n"
                f"Offline Servers: {len(servers_farm) - online_count}"
        )

        print(final_summary)
        save_report_to_file(final_summary)