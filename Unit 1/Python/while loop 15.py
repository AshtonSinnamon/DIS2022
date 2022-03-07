user = input("What is your username: ")
password = input("What is your password: ")
tries = 3
loggedIn = False
if user == "a" and password == "b":
    loggedIn = True
    print("Welcome Back, You are logged in...")
else:
    while tries != 0 and tries > 0:
        print("Incorrect")
        tries -= 1
        print("You have", tries, "tries remaining.")
        user = input("What is your username: ")
        password = input("What is your password: ")
if not loggedIn:
    print("You are logged out for 60 minutes...")
