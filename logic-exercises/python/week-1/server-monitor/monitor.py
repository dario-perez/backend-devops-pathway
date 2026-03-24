# Servers and Statuses lists
servers = ["web01", "db01", "app01", "backup01"]
statuses = [True, False, True, True]

for i in range(len(servers)):
    server_name = servers[i]
    is_online = statuses[i]

    if is_online:
        print(f"Server {server_name} is UP")
    else:
        print(f"Server {server_name} is DOWN")
