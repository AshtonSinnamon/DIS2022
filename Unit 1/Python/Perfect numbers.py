num = int(input("What is your number: "))

for i in range(1, num + 1):
    perfect_num = 0
    for x in range(1, i):
        if i % x == 0:
            perfect_num = perfect_num + x
    if perfect_num == i:
        print(perfect_num, "is a perfect number")
    # else:
    #     print(i, "is not a perfect number")