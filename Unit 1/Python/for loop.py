# for loops
# count to 10

# for i in range(11):
#     print(i)

# count to 5 - 36

# for i in range(5, 37, 3):
#     print(i)

#############
# num = int(input('Input a number from 1-12: '))
# for i in range(1, 13):
#     print(i, 'x', num,  '=', i*num)
##############

# ask user for two numbers, add up all numbers between
# n1 = int(input('Enter number one:'))
# n2 = int(input("Enter number 2:"))
# total = 0
#
# for i in range(n1, n2+1):
#     total = total + i
#
# print(total)
################

# find all the multiples of 7 between 1 and 50

for i in range(0, 51):
    if i % 7 == 0:
        print(i)