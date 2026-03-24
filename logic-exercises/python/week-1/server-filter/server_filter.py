servers = [
    {"id": "KR-01", "load": 45},
    {"id": "KR-02", "load": 87},
    {"id": "KR-03", "load": 12},
    {"id": "US-01", "load": 92},
]

for server in servers:
    if server["load"] > 80:
        print(
            f"⚠️ Alert: Server {server['id']} is overloaded! | Load status: {server['load']}%"
        )
    else:
        print(f"✅ Server {server['id']} is stable.")
