# for every number between 1 + 100 inclusive, print number or if multiple of 3 =fizz, if multiple of 5 = buz,
# if both print fizz buzz

for i in range(1, 101):
    if i % 3 == 0 or i % 5 == 0:
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
    else:
        print(i)


