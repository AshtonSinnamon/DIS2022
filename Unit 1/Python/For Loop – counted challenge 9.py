# Ask the user to enter the number of numbers they will enter. Prompt the user for each of the numbers. Display the
# total, average, maximum and minimum number, the number of odd numbers and the number of even numbers.

n = int(input("how many numbers number: "))
total = 0
average = 0
max = -1
min = 101
odd = 0
even = 0

for i  in range(1, n+1):
    num = int(input("enter number: " + str(i) + ":"))
    total += num
    if num > max:
        max = num
    if num < min:
        min = num
    if num % 2 == 0:
        even += 1
    else:
        odd += 1
average = total/n
print("Total:", total)
print("Average", average)
print("max", max)
print("min", min)
print("even", even)
print("odd", odd)