import time


class TrafficLights:
    def __init__(self, color: str = "red"):
        self.color = color

    def change(self):
        if self.color == "red":
            self.color = "green"
        elif self.color == "green":
            self.color = "yellow"
        else:
            self.color = "red"

    def show(self):
        print(self)
    
    def __str__(self):
        mapping = {
                        "red": "🔴 STOP",
                        "green": "🟢 GO",
                        "yellow": "🟡 CAUTION"
                }
        return mapping.get(self.color)



if __name__ == "__main__":
    traffic_light = TrafficLights()
    traffic_light.change()
    traffic_light.show()

    print("--- 🚦 Simulator Starting ---")
    for i in range(10):
        print("\033[H\033[J", end="")
        traffic_light.show()
        traffic_light.change()
        time.sleep(1)