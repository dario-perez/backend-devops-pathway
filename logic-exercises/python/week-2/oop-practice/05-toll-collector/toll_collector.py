def find_single_trips(license_plates: list):
    """
    Finds license plates that appear exactly once in the list.
    """
    counts = {}

    for plate in license_plates:
        if plate in counts:
            counts[plate] += 1
        else:
            counts[plate] = 1

    singles = []
    for plate, count in counts.items():
        if count == 1:
            singles.append(plate)
    
    return singles


if __name__ == "__main__":
    traffic_data = ["ABC-123", "XYZ-789", "ABC-123", "JKL-456", "XYZ-789"]
    single_trip = find_single_trips(traffic_data)

    print(f"single trip plates: {single_trip}")