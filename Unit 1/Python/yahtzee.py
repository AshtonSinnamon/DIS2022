# Simulate the rolling of dice in Yahtzee, by getting 5 random numbers between 1 and 6. Display each number on a line

import random

for i in range(5):
    num = random.randint(1, 6)
    print(num)
