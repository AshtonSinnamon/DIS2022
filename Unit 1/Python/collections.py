# students = []
#
# students.append("Peter")
# students.append("Paul")
# students.append("Mary")
#
# print(type(students))
# print(students)
# print(students[1])
# print(len(students))
# print(students[-1])
#
# for student in students:
#     print(student)
#
# students.append("Ashton")
# print(students)
# students.sort()
# print(students)
# students.reverse()
# print(students)
#
# x = students.pop()
# print(x, students)
#
# students.remove("Peter")
# print(students)
#
#######################################
newStudents = ["Simon", "andrew", "Martha", "Andrea"]
grades = [23, 45, 92, 32]

for i in range(len(newStudents)):
    print(newStudents[i], "got the grade,", grades[i])
#######################################
name = 'Ashton'
letters = list(name)
print(letters)
###############
name = "Ashton Sinnamon"
nameParts = name.split()
print(nameParts)
first_name = nameParts[0]
lastName = nameParts[1]
print(lastName.upper(), first_name)