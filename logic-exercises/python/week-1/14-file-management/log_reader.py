try:
    with open("system.log", "r") as file:
        print(f"System.log: \n{file.read()}")
except FileNotFoundError:
    print("⚠️ Error: The log file does not exist yet.")
except Exception as e:
    print(f"❌ Unexpected error: {e}")
