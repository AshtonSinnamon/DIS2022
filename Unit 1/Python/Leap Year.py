# A year is a leap year if it is divisible by 4, and if it is a century,
# it must also be divisible by 400. (1800 and 1900 are not leap years while 1600 and 2000 are).
# Write a program that calculates whether a year is a leap year.

year = int(input('What is the year: '))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(year, 'is a leap year')
        else:
            print('This is not a leap year')
    else:
        print("This is a leap year")
else:
    print('This is not a leap year')
