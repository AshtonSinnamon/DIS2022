n = int(input("Enter the number: "))

while n != 1:
    print(n)
    if n % 2 == 0:
        n = int(n / 2)
    else:
        n = int(n * 3 + 1)
print(n)


