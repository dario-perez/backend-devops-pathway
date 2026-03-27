# Infrastructure Manager 🛡️

A Python-based utility to manage server inventories with built-in data integrity checks.

### Key Features
* **Encapsulation:** Uses a `Server` class to standardize server data.
* **Data Validation:** Implements `isinstance` checks to ensure input types are correct before processing.
* **Network Integrity:** Integrates Python's `ipaddress` module to validate IPv4/IPv6 formats.
* **Error Handling:** Uses `try-except` blocks to catch malformed data, preventing script crashes during bulk operations.

### How it works
The `InfrastructureManager` groups servers by tags (e.g., Web, DB) and provides methods to add or remove instances safely. If an invalid IP is provided, the system logs the error and continues processing the remaining queue.