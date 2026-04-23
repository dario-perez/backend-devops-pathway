# Infrastructure Manager 🖥️

A Python-based system designed to manage different types of server entities using **Object-Oriented Programming (OOP)** principles. This project demonstrates the implementation of class inheritance, dynamic object creation, and data validation logic.

---

## 🚀 Features

* **Hierarchical Structure**: Base `Server` class with specialized `WebServer` and `DatabaseServer` subclasses.
* **Flexible Management**: An `InfrastructureManager` that handles server registration and categorization using dynamic argument handling.
* **Dual-Type Support**: 
    * **Web Servers**: Includes specific port configuration.
    * **Database Servers**: Includes storage engine specifications.
* **Health Check Logic**: Integration of a custom validation system inspired by the FizzBuzz logic to verify server integrity.

---

## 🛠️ Technical Details

### Pylance & Type Hinting
To ensure compatibility with static analysis tools like Pylance and avoid assignment errors during dynamic instantiation, certain type definitions utilize `Any`. This allows the manager to handle multiple subclasses seamlessly while maintaining code readability.

### Logic Implementation
The system includes a validation layer that categorizes server responses based on numeric identifiers:
* Identifies standard operational offsets.
* Flags specialized service requirements.
* Matches combined infrastructure protocols.

---

## 📂 Project Structure

* `infrastructure_manager.py`: Main execution logic and class definitions.
* `README.md`: Project documentation and technical overview.

---

## 📝 Usage

The manager can be initialized to add servers dynamically:

```python
manager = InfrastructureManager()
manager.add_server("Production-Web", "192.168.1.10", type="web", port=80)
manager.add_server("Main-DB", "192.168.1.20", type="db", db_engine="PostgreSQL")