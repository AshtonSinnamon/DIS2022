name = str(input("What is the contestants name: "))

while len(name) > 0:
    if name == str("exit"):
        exit()
    else:
        print(name)
        name = str(input("What is the contestants name: "))
