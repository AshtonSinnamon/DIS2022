filename = "../TextFiles/SelfDivisible"
file = open(filename)
contents = file.readlines()
for line in contents:
    line = line.strip("\n")
    values = line.split()
    first = int(values[0])
    last = int(values[1]) + 1

    count = 0
    for i in range(first, last):
        x = str(i)
        valid = True

        if first % last == 0:
            valid = True
            if "0" not in x:
                if len(x) > 0:
                    for j in range(len(x)):
                        if int(x[:j+1]) % int(x[j]) != 0:
                            valid = False
            else:
                valid = False

            if valid is True:
                count = count + 1

    print("Number of self-divisble numbers between,", first, "and", last - 1, "is", count)
