file = open("../TextFiles/Panagrams.txt")
contents = file.readlines()
contents.pop(0)

alphabet = set(list("abcdefghijklmonoprstuvwxyz"))
print(alphabet)

for line in contents:
    line.strip("\n")
    letter = set()
    for char in line:
        if char.isalpha():
            letter.add(char.lower())
    missing = alphabet.difference(letter)
    missing = sorted(list(missing))
    str1 = ""
    missing = str1.join(missing)
    print(line)
    if len(missing) == 0:

        print("    ", "Panagram")
    else:
        print("    ", "Not a panagram. Missing:" + str(missing))
