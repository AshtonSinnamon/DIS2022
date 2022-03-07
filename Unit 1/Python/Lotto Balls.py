import random

ballsNum = []

for i in range(6):
    num = random.randint(1, 45)
    while num in ballsNum:
        num = random.randint(1, 45)
    ballsNum.append(num)

ballsNum.sort()
print(ballsNum)
print("*" * 5)
for balls in ballsNum:
    print(balls)
