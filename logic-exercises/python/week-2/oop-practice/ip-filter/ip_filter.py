def attack_detection(ips):
    '''Detects ip addresses that appear more than three times'''
    counts = {}

    for ip in ips:
        if ip in counts:
            counts[ip] += 1
        else:
            counts[ip] = 1
    
    singles = []
    for ip, amount in counts.items():
        if amount > 3:
            singles.append(ip)

    return singles



if __name__ == "__main__":
    ip_list = [
        "192.168.1.1", "10.0.0.5", "192.168.1.1", "192.168.1.1", "192.168.1.1", "10.0.0.5"
    ]
    attackers = attack_detection(ip_list)

    print(f"Attacking IP addresses: {attackers}")