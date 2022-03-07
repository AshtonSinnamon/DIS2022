students_ages = {}

students_ages["Elliot"] = 16
students_ages["Ronan"] = 17
students_ages["Matthew"] = 17
students_ages["Louis"] = 18
print(len(students_ages))

# for name, age in students_ages.items():
#     print(name, "is", age)


# ask user to enter name, and if name is not in dict ask and
# add age to dict


name = input("Enter name: ")
if name not in students_ages:
    age = int(input("Enter age: "))
    students_ages[name] = age
    for name, age in students_ages.items():
        print(name, "is", age)


# how do you loop through a dic and get both age and name; eg elliot is 16, louis is 18
# for name, age in students_ages.items():
#     print(name, "is", age)