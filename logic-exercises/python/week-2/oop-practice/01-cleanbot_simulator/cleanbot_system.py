import time


class CleanBot:
    def __init__(self, name: str, battery: int = 100, position: int = 0):
        self.name = name
        self.battery = battery
        self.position = position
        self.path_size = 20

    def move(self):
        if self.position < self.path_size:
            if self.battery > 0:
                self.battery -= 10
                self.position += 1
            else:
                print(f"🪫 {self.name} is out of juice!")
        else:
            print(f"✅ {self.name}'s finished the job!")

    def recharge(self):
        self.battery = 100

    def __str__(self):
        path = ["_"] * self.path_size
        if self.position < self.path_size:
                path[self.position] = "🤖"
        
        return f"[Robot: {self.name}\n{' '.join(path)}] Battery: {self.battery}%"
    

if __name__ == "__main__":
    my_bot = CleanBot("Dustminator Model 101")
    for i in range(21):
        print("\033[H\033[J", end="")
        print(my_bot)
        my_bot.move()
        time.sleep(0.2)
        if my_bot.battery <= 20:
            my_bot.recharge()