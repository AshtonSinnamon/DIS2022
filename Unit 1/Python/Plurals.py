file = open("../TextFiles/Plurals")
contents = file.readlines()
contents.pop(0)

vowels = "aeiouy"

for line in contents:
    val = line.split()
    # print(line)
    num = val[0]
    word = val[1]
    if num == "0":
        num = "no"
    elif num == "1":
        num = "one"
    if num != "one":
        if word[-1] in ("s", "x", "z"):
            word += "es"
        elif word[-2] in ("ch", "sh"):
            word += "es"
        elif word[-1] == "o" and word[-2] not in vowels:
            word += "es"
        elif word[-1] == "y" and word[-2] not in vowels:
            word = word[0:-1] + "ies"
        elif word[-2:] == "fe" and word[-3] != "f":
            word = word[0:-2] + "ves"
        elif word[-1] == "f" and word[-2] != "f":
            word = word[0:-1] + "ves"
        else:
            word += "s"
    print(num, word)
