def fleet_grouper(server_list):
  status = {}
  
  for name, state in server_list:
    state = state.upper()

    if state not in status:
      status[state] = []
    status[state].append(name)
    
  return status



if __name__ == "__main__":
  servers_statuses = [
    ("Web1", "ONLINE"), 
    ("DB1", "OFFLINE"), 
    ("Web2", "ONLINE"), 
    ("Cache1", "OFFLINE")
  ]

  server = fleet_grouper(servers_statuses)
  print("=== Servers Statuses ===")
  print(f"Online: {server['ONLINE']}")
  print(f"Offline: {server['OFFLINE']}")