# filename = "TextFiles/studentdata.txt"
# file = open(filename)
# content = file.readlines()
# sum = 0
# for line in content:
#     line = line.strip("\n")
#     line.split()
#     name = line.pop(0)
#     mark = []
#     for i in range(1, len(line)):
#         sum =+ i
#     print(sum)
#     average_score = sum/len(line[1:])
#     total_score = len(line[1:])
#     print("Name is", name, "got", total_score, "with average of", average_score)

file = open("../TextFiles/studentdata.txt")
content = file.readlines()
name = []
Total_scores = 0
average = 0
for line in content:
    line = line.strip('\n')
    line = line.split()
    name = line.pop(0)
    Total_scores = len(line)
    for i in range(1, len(line)):
        Total_scores += i
    average = Total_scores // len(line)
    print(name.title(), "got", Total_scores, "grades and their average grades were", average)