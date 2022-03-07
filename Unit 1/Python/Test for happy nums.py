#Happy numbers
def happy(n):

    number = str(n)

    #container
    container = []

    while True:
        temp = 0
        for digit in number:
            temp += int(digit) ** 2

        if temp == 1:
            return True

        elif temp in container:
            return False
        else:
            container.append(temp)
            number = str(temp)

for i in range(1, 1000):
    n = i
    if happy(n):
        print(i, "is a happy number!")
    # else:
    #     print(i, "is not a happy number")