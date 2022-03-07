filename = "../TextFiles/results-1line.txt"
file = open(filename)
contents = file.readlines()
nA = 0
nB = 0
nC = 0
nFail = 0


for line in contents:
    line = line.strip("\n")
    values = line.split(", ")
    name = values[0]
    mark = values[1]
    if int(mark) > 79:
        grade = "A"
        nA += 1
    elif int(mark) > 69:
        grade = "B"
        nB += 1
    elif int(mark) > 49:
        grade = "C"
        nC += 1
    else:
        grade = "Fail"
        nFail += 1
    print(name + ", got a mark of", str(mark) + ", resulting in the grade of", grade)
print("\n")
print("Summary")
print("Number of A:", nA)
print("Number of B:", nB)
print("Number of C:", nC)
print("Number of Fail:", nFail)