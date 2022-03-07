names = []
name = input("Enter a name or quit: ").strip()

run = True
while run:
    if name.lower() == "quit":
        run = False
        if len(names) > 0:
            names.sort()
            for names in names:
                print(names)
        else:
            print("There are no names")
    else:
        if name.title() not in names:
            names.append(name.title())
            name = input("Enter a name: ").strip()
        else:
            print(name.upper(), "is already taken.")
            name = input("Enter a name: ").strip()

##################
# names = []
#
# username = input("Enter a name or quit: ").strip()
# while username.lower() != "quit":
#     if username.title() not in names:
#         names.append(username.title())
#     else:
#         print(name, "already exists")
#     username = input("Enter a name or quit: ").strip()
#
# if len(names) > 0:
#     names.sort()
#     for names in names:
#         print(names)
# else:
#     print("There are no names")