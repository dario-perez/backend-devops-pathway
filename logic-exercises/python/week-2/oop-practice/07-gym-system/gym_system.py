class Member:
    def __init__(self, name: str, weight: float):
        self.name = name
        self.weight = weight
        self.is_training = False

    def status(self):
        if self.is_training:
            print("Member is training!")
        else:
            print("Member is resting")


class Boxer(Member):
    def __init__(self, name: str, weight: float, category):
        super().__init__(name, weight)
        self.category = category

    def punch_bag(self):
        if self.is_training:
            print(f"{self.name} is hitting the bag with power!")
        else:
            print(f"{self.name} needs to start training first!")


class Coach(Member):
    def __init__(self, name: str, weight: float, specialty):
        super().__init__(name, weight)
        self.specialty = specialty

    def motivate(self):
        print(f"Coach {self.name} is screaming: 'GET UP, YOU SON OF A BI$%@! BECAUSE MICKEY LOVES YA!'")


if __name__ == "__main__":
    member = Member("Creed", 214)
    member.status()

    boxer = Boxer("Rocky", 212, "Heavyweight")
    boxer.punch_bag()
    boxer.is_training = True
    boxer.punch_bag()

    coach = Coach("Mickey", 155, "Technique")
    coach.motivate()