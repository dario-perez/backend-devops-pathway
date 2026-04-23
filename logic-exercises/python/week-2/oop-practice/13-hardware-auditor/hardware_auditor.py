def count_hardware(items):
    '''Creates a dict with items and their quantity'''
    counts = {}
    for item in items:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    
    return counts



if __name__ == "__main__":
    hardware = ["CPU", "RAM", "SSD", "CPU", "RAM", "RAM"]
    my_hardware = count_hardware(hardware)
    
    print ("\n=== ITEMS STOCK ===\n")
    print(my_hardware)
