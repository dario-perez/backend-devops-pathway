# List of servers and statuses
servers = [
    {"name": "web-01", "online": True},
    {"name": "db-01", "online": False},
    {"name": "cache-01", "online": True},
]


def get_status_icon(is_up):
    """
    Returns a human-readable status icon based on server availability.
    """
    if is_up:
        return "✅ UP"
    else:
        return "❌ DOWN"


for server in servers:
    print(f"Server: {server['name']} | Status: {get_status_icon(server['online'])}")
