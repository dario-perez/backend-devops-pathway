networks = [
    {"zone": "Seoul-North", "users": 5000, "nodes": 10},
    {"zone": "Seoul-South", "users": 2500, "nodes": 0},
    {"zone": "Busan-Central", "users": 3000, "nodes": 5},
]


def calculate_load(total_users, active_servers):
    try:
        load = total_users / active_servers
        return f"Load: {load:.2f} users/server"
    except ZeroDivisionError:
        return "⚠️ Alert: No active servers!"
    except Exception as e:
        return f"❌ Unexpected error: {e}"


for network in networks:
    print(
        f"Zone: {network['zone']} | {calculate_load(network['users'], network['nodes'])}"
    )
