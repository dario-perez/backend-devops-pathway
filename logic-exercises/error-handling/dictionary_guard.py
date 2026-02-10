server_info = {"name": "Seoul-DB-01", "status": "active"}

try:
    print(f"Server location: {server_info['location']}")
except KeyError:
    print(("⚠️ Error: Location data is missing, but the system is still running."))

print("Final report complete. ✅")
