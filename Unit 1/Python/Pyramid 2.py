for i in range(1, 6):
    output = ""
    for x in range(1, i):
        output += str("_")
    print(output + "#")


###############################
for i in range(1, 6):
    output = ""
    for x in range(1, 11):
        output += str(i * x) + " "
    print(output)
###############################
letters = "ABCDE"
for i in range(len(letters)):
    letter = letters[i]
    line = ""
    for x in range(0, i + 1):
        line += letter
    print(line)
###############################
for i in range(1, 6):
    output = ""
    for x in range(0, 5-i):
        output += "."
    for y in range(0, i):
        output += str(i)
    print(output)
