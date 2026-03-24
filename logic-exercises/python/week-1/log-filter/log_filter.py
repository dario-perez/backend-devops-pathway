# List of server logs
logs = [
    "INFO: User logged in",
    "ERROR: Disk full",
    "INFO: Backup done",
    "ERROR: Connection failed",
]

# Iterate through each log in the list
for log in logs:
    # Check if the keyword "ERROR" exists in the current string
    if "ERROR" in log.upper():
        print(f"Status: {log}")
