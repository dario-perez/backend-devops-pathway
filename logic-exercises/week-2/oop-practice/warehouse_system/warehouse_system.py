from products_data import products_data



class Product:
  def __init__(self, name: str, price: float, quantity: int):
    self.name = name
    self.price = price
    self.quantity = quantity

  def get_total_value(self):
    return self.price * self.quantity
  
  def __str__(self):
    return f"{self.name} (${self.price}) x {self.quantity}"
  


class Warehouse:
  def __init__(self, location: str):
    self.location = location
    self.products = []
  
  def add_product(self, product_obj):
    self.products.append(product_obj)

  def inventory_report(self):
    print(f"--- Inventory Report: {self.location} ---")
    for p in self.products:
      print(f"📦 {p} | Total Value: ${p.get_total_value()}")

  def get_warehouse_value(self):
    return sum(p.get_total_value() for p in self.products)



if __name__ == '__main__':
  warehouse = Warehouse("Myeongdong, Seoul")
  for name, price, quantity in products_data:
    p = Product(name, price, quantity)
    warehouse.add_product(p)
  warehouse.inventory_report()
  print(f"Total Warehouse Value: {warehouse.get_warehouse_value()}")