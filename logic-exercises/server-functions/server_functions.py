def check_server_status(name, is_up, environment):
    if is_up:
        return f"[{environment.upper()}] Server {name} is UP"
    else:
        return f"[{environment.upper()}] Server {name} is DOWN"


status_report = check_server_status("web-01", True, "prod")
print(status_report)
