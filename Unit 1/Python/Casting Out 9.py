filename = "../TextFiles/Casting9"
file = open(filename)
contents = file.readlines()
for line in contents:
    line = line.strip("\n")
    total = 0
    for n in line:
        total += int(n)
        if total >= 9:
            total -= 9
    print(total)