import random

rolls = int(input("How many rolls: "))
craps = 0
under = 0
over = 0


for i in range(rolls):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    total = dice1 + dice2
    if total == 7:
        craps = + 1
    elif total > 7:
        over = + 1
    else:
        under = + 1

print("Craps:", craps)
print("Over:", over)
print("Under:", under)