def happyNumbers(n):
    number = str(n)
    check = []
    # print("Number:", number)
    while True:
        nSum = 0
        for digit in number:
            nSum += int(digit) ** 2
            # print("Sum", nSum)
        if nSum == 1:
            return True
        elif nSum in check:
            return False
        else:
            check.append(nSum)
            number = str(nSum)


for i in range(1, 1000):
    n = i
    if happyNumbers(n):
        print(i, "is a happy number!")
    else:
        print(i, "is not a happy number")
