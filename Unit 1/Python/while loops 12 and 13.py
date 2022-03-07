# 12
# pop = 26000000
# year = 0
# while pop < 50000000:
#     pop = pop * 1.03
#     year = year + 1
# print(year)

# 13
# Test: n1 = 78 and n2 = 66: Steps-66-12-6
n1 = int(input("What is the first number: "))
n2 = int(input("What is the second number: "))
if n1 >= n2:
    ln = n1
    sn = n2
else:
    ln = n2
    sn = n1
while sn != 0:
    gcd = sn
    sn = n1 % sn
    ln = gcd
    print("GCD is", gcd)
