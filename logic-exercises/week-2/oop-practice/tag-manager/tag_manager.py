def tag_manager(server_list):
  '''Groups server names by their specific tags dynamically.'''
  tagged = {}

  for name, tag in server_list:
    if tag not in tagged:
      tagged[tag] = []
    if name not in tagged[tag]:
      tagged[tag].append(name)

  return tagged



if __name__ == "__main__":
  server_tags = [
    ("Srv1", "Web"), 
    ("Srv2", "DB"),
    ("Srv3", "Storage"), 
    ("Srv4", "Web"), 
    ("Srv5", "Storage")
  ]

  result = tag_manager(server_tags)
  print("=== Servers Grouped by Tag ===")
  print(result)