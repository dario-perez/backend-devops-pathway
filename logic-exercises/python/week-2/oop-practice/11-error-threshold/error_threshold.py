def error_monitor(errors):
    counts = {}

    for err in errors:
        if err in counts:
            counts[err] += 1
        else:
            counts[err] = 1

    critical_errors = []

    for error_name, frequency in counts.items():
        if frequency > 2:
            critical_errors.append(error_name)

    return critical_errors



if __name__ == "__main__":
    error_logs = ["Timeout", "404", "Timeout", "500", "Timeout"]
    critical_list = error_monitor(error_logs)

    for error in critical_list:
        print(f"\n⚠️ ALERT: Critical failure count for {error}\n")