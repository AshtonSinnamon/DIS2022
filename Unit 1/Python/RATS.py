def reverse(str1):
    return str1[::-1]


cycle = []
check = []
count = 0
for x in range(1, 10001):
    n = reverse(str(x))
    count += 1
    val = int(n) + int(n)
    print("val", val)
    sort = sorted(str(val))
    sort1 = ""
    sort = sort1.join(sort)
    print("Sort", sort)
    print("Cycles:", count)
    print(10 * "*")
    check.append(val)

print(sorted(check))
#print(max("Max", check))
print("Count", count)