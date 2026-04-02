import random
from abc import ABC, abstractmethod

STORAGE_STANDARD = "Standard"
STORAGE_ARCHIVE = "Archive"

class Storage(ABC):
  def __init__(self, name):
    self.name = name

  @abstractmethod
  def get_usage(self):
    pass



class LocalDisk(Storage):
  def __init__(self, name, path, capacity_gb):
    super().__init__(name)
    self.path = path
    self.capacity_gb = capacity_gb

  def get_usage(self):
    usage = random.randint(0, 100)
    return usage



class CloudBucket(Storage):
  def __init__(self, name, endpoint_url, storage_class):
    super().__init__(name)
    self.endpoint_url = endpoint_url
    self.storage_class = storage_class

  @property
  def storage_class(self):
    return self._storage_class
  
  @storage_class.setter
  def storage_class(self, value):
    if value not in [STORAGE_STANDARD, STORAGE_ARCHIVE]:
      raise ValueError(f"Invalid storage class: {self.storage_class}. Must be 'Standard' or 'Archive'.")
    self._storage_class = value

  def get_usage(self):
    usage = random.randint(0, 100)
    return usage



def generate_storage_report(storage_list: list[Storage]):
    print("\n" + "=" * 40)
    print("📋 INFRASTRUCTURE STORAGE REPORT")
    print("=" * 40)
    for item in storage_list:
      print(f"[REPORT] Storage: {item.name} | Usage: {item.get_usage()}%")
    print("="*40)



if __name__ == "__main__":
  try:
    my_local_disk = LocalDisk("prod-disk", "/data/prod", 1024)
    my_cloud_bucket = CloudBucket("media-files", "https://s3.us-east-1.amazonaws.com/media-files", "Standard")
    fleet_storage = [my_local_disk, my_cloud_bucket]

    generate_storage_report(fleet_storage)
  
  except ValueError as e:
    print(f"Configuration error: '{e}'")