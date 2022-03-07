num = int(input("Enter a number: "))
factors = 0
for i in range(2, num+1):
    if num % i == 0:
        print(i)
        factors += 1

if factors > 1:
    print(num, "Is not prime.")
else:
    print(num, "is prime")