filename = "../TextFiles/results.txt"
file = open(filename)
contents = file.readlines()
print(contents)

names = []
marks = []
for i in range(1, len(contents) + 1):
    # line = line.strip("\n")
    if i % 2 == 0:
        marks.append(contents)
    else:
        names.append(contents)
print(names)
print(marks)
# for i in range(len(names)):
#     name = names[i]
#     mark = marks[i]
#     print(mark)
#     print(name)
# if int(mark) > 79:
#     grade = "A"
#     #nA += 1
# elif int(mark) > 69:
#     grade = "B"
#     #nB += 1
# elif int(mark) > 49:
#     grade = "C"
#     #nC += 1
# else:
#     grade = "Fail"
#     #nFail += 1
# # print(name + ", got a mark of", str(mark) + ", resulting in the grade of", grade)
# print(name, mark, grade)
