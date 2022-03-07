n1 = float(input("What is your first number: "))
n2 = float(input("What is your second number: "))

choice = input("What is your Choice 1-4: ")

if choice in "1234":
    if choice == "1":
        print(n1 + n2)
    elif choice == "2":
        print(float(n1 - n2))

    elif choice == "3":
        print(n1 * n2)

    elif choice == "4":
        print(n1 / n2)

else:
    print("Enter a Valid choice")
