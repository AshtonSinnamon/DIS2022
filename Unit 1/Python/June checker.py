# The date 10 June 1960 is special because the day times the month equals the year. Create a program that asks the
# user to enter a date in the format dd/mm/yy and output whether it is a magic date or not.

date = str(input("Enter a year in a dd/mm/yy format: "))
day = date[:2]
month = date[2:4]
year = date[-2:]

# print(day)
# print(month)
# print(year)

magic_date = False
if int(day) * int(month) == int(year):
    magic_date = True
    print('Your date is magic')
else:
    print('Your date in not magic')
