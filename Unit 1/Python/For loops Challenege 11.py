# Ask the user to enter the number of rolls of dice and then display the frequency of each number.
import random

num1 = 0
num2 = 0
num3 = 0
num4 = 0
num5 = 0
num5 = 0
num6 = 0
rolls = int(input("How many rolls: "))

for i in range(rolls):
    dice = random.randint(1, 6)
    if dice == 1:
        num1 = + 1
    elif dice == 2:
        num2 = + 1
    elif dice == 3:
        num3 = + 3
    elif dice == 4:
        num4 = + 1
    elif dice == 5:
        num5 = + 1
    elif dice == 6:
        num6 = + 1

print("There was", num1, ":1")
print("There was", num2, ":2")
print("There was", num3, ":3")
print("There was", num4, ":4")
print("There was", num5, ":5")
print("There was", num6, ":6")
