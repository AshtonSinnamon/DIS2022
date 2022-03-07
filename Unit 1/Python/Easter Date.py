year = int(input('What is the year between and including 1982-2048: '))

a = year % 19
b = year % 4
c = year % 7
d = ((19 * a) + 24) % 30
e = ((2 * b) + (4 * c) + (6 * d) + 5) % 7
Easter = 22 + d + e
# print(Easter)
if year <= 1981 or year >= 2049:
    print('Please input a date between the years 1982 and 2048')
else:
    if Easter > 31:
        date = Easter - 31
        print('In', year, 'Easter will be on the', str(date), 'of April')
    else:
        print('In', year, 'Easter will be on the', str(Easter), 'of March')