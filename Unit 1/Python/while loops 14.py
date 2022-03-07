import random

mypot = int(input("Enter your price for the pot: "))
print("Max amount in the pot $" + str(mypot))
rolls = 0
while mypot > 0:
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    myroll = die1 + die2
    rolls = rolls + 1

    #print(myroll)
    if myroll == 7:
        mypot = mypot + 4
        print("Currently in the pot $" + str(mypot))
    else:
        mypot = mypot - 1
        print("Currently in the pot $" + str(mypot))
print("It will take", rolls, "rolls till your out of money!")
