
from random import randint


class Die():

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        return randint(1, self.sides)

results =[]
die_six_sides = Die(6)
for i in range(die_six_sides.sides):
    results.append(die_six_sides.roll_die())

print(f'\nWe simulated 10 times od rolling die, scors are:')
print(results)