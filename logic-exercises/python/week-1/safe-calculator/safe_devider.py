def calculate_load(total_users, active_servers):
    try:
        load = total_users / active_servers
        return f"Load: {load:.2f} users/server"
    except ZeroDivisionError:
        return "⚠️ Alert: No active servers!"


print(calculate_load(1000, 5))
print(calculate_load(1000, 0))
