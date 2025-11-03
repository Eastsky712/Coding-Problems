from random import randint
class Dice:
    def __init__(self, sides=6):
        self.sides = sides
    
    def roll_die(self):
        return randint(1, self.sides)
    
normal_dice = Dice(6)
for i in range(10):
    print(normal_dice.roll_die())
print("\n")
ten_dice = Dice(10)
for i in range(10):
    print(ten_dice.roll_die())

print("\n")
twenty_dice = Dice(20)
for i in range(20):
    print(twenty_dice.roll_die())