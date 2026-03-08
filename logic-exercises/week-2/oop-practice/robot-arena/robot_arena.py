import random
import time
import sys
from pathlib import Path

script_dir = Path(__file__).resolve().parent
project_root = script_dir.parent

if str(project_root) not in sys.path:
  sys.path.append(str(project_root))

from cleanbot_simulator.cleanbot_system import CleanBot



class Arena:
  def __init__(self, bot_1: str, bot_2: str):
    self.bot_1 = CleanBot(bot_1)
    self.bot_2 = CleanBot(bot_2)
    self.size = 30

    self.bot_1.position = 0
    self.bot_2.position = self.size - 1

  def bot_move(self):
    if self.bot_1.battery <= 20 or self.bot_2.battery <= 20:
      self.bot_1.recharge()
      self.bot_2.recharge()
      return "⚡ Low battery! Emergency recharge initiated..."
    
    distance = self.bot_2.position - self.bot_1.position

    if distance > 1:
      self.bot_1.move()
      self.bot_2.position -= 1
      self.bot_2.battery -= 10
      return "The robots are approaching! ⚔️"
    else:
      winner = random.choice([self.bot_1, self.bot_2])
      return (f"The winner is : {winner.name}!")
    
  def __str__(self):
    arena = ["_"] * self.size
    arena[self.bot_1.position] = "🤖"
    arena[self.bot_2.position] = "🤖"

    return (
      f"Today's Match:\n"
      f"🥊 {self.bot_1.name} ({self.bot_1.battery}%) VS "
      f"{self.bot_2.name} ({self.bot_2.battery}%) 🥊\n"
      f"[{' '.join(arena)}]"
    )



if __name__ == "__main__":
  arena = Arena("Dustminator", "Dirtminator")
  for i in range(20):
    print("\033[H\033[J", end="")
    print(arena)
    result = arena.bot_move()
    print(result)
    if "winner" in result.lower():
      print("\n🏆 MATCH FINISHED 🏆")
      break
    time.sleep(0.5)