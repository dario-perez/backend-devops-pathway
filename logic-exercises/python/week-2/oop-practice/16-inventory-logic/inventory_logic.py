#!/usr/bin/env python3
def calc_total(sell_list):
    total = {}

    for sell in sell_list:
        try:
            product = sell["product"]
            price = sell["price"]
            quantity = sell["quantity"]
            subtotal = price * quantity

            if product in total:
                total[product] += subtotal 
            else:
                total[product] = subtotal

        except TypeError:
            print(f"Error in '{sell.get('product', 'Unknown')}': Invalid numeric data.")
        except KeyError as e:
            print(f"Error: Missing data {e} in one of the sells.")
    
    return total



dirty_sells = [
    {"product": "monitor", "price": 100, "quantity": 2},
    {"product": "teclado", "price": "50", "quantity": 1},
    {"product": "monitor", "price": 100, "quantity": 1},
    {"product": "mouse", "quantity": 5}
]



if __name__ == "__main__":
    result = calc_total(dirty_sells)
    print("\n Final resume:")
    for p, t in result.items():
        print(f"{p}: ${t}")