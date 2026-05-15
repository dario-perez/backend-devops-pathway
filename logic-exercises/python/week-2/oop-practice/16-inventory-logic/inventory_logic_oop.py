class Sell:
    def __init__(self, product, price, quantity):
        self.product = product

        try:
            self.price = float(price)
        
        except ValueError:
            print(f"Invalid price for {product}. Setting to 0.0")
            self.price = 0.0

        if quantity < 0:
            self.quantity = 0
        else:
            self.quantity = quantity

    def calc_subtotal(self):
        try:
            return self.price * self.quantity
        
        except TypeError:
            print(f"Error: invalid product data: {self.product}")
            return 0

    def total(self, sell_list):
        total = 0

        for sell in sell_list:
            total += sell.calc_subtotal()

        return total

    def high_sales(self, sell_list):
        vip_products = []

        for p in sell_list:
            if p.calc_subtotal() > 500:
                vip_products.append(p)

        return vip_products