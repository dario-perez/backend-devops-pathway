import json


def log_calculation(num1, num2, result, file_name="operation.json"):
    try:
        try:
            with open(file_name, "r") as file:
                history = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            history = []

        history.append({"Number 1": num1, "Number 2": num2, "Result": result})

        with open(file_name, "w") as file:
            json.dump(history, file, indent=4)
        print("✅ Data calculation run correctly.")

    except Exception as e:
        print(f"❌ Failed to save log: {e}")


log_calculation(5, 10, 15)
log_calculation(10, 10, 20)
log_calculation(20, 20, 40)
log_calculation(30, 30, 60)
