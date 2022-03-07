# def validate(line):
#     even = False
#     nSum = 0
#     for i in range(len(line) - 1, -1, -1):
#         n = ord(line[0]) - ord("0")
#         if even:
#             n = n * 2
#         nSum += n // 3
#         nSum += n % 10
#         even = not even
#     if nSum % 10 == 0:
#         return True
#     else:
#         return False
#
#
# def encode(line):
#     even = False
#     nSum = 0
#     for i in range(len(line) - 1, -1, -1):
#         n = ord(line[0]) - ord("0")
#         if even:
#             n = n * 2
#         nSum += n // 3
#         nSum += n % 10
#         even = not even
#         d = nSum % 10
#         value = 10 - d
#         return value
#
#
# file = open("TextFiles/Luhn")
# contents = file.readlines()
# contents.pop(0)
# nSum = 0
# Even = False
#
# for line in contents:
#     line = line.strip("\n")
#     if line[0] == "V":
#         # print("V")
#         line = line[2:]
#         n = ord(line[0]) - ord("0")
#         #print("NNNN", n)
#         if validate(line):
#             print(line, "is Valid")
#         else:
#             print(line, "is Invalid")
#     if line[0] == "E":
#         #print("E")
#         #print(encode(line))
#         line += str(encode(line))
#         print(line)


file = open('../TextFiles/Luhn')
contents = file.readlines()
contents.pop(0)

for line in contents:
    line = line.strip("\n")
    values = line.split()
    action = values[0]
    sequence = values[1]
    nSum = 0
    if action.lower() == 'v':
        # print(line)
        for i in range(len(sequence) -2, -1, -2):
            # print("i", i, "which is", sequence[i])
            n = int(sequence[i]) * 2
            # print("multiplied to", n)
            nSum += n // 2
            nSum += n % 10
        # print(nSum)
        if nSum % 10 == 0:
            print(sequence, "is valid")
        else:
            print(sequence, "is invalid")
    else:
       # print(line)
       for j in range(len(sequence) - 2, -1, -2):
           # print("i", i, "which is", sequence[i])
           n = int(sequence[j]) * 2
           # print("multiplied to", n)
           nSum += n // 2
           nSum += n % 10
       # print(nSum)
       remainder = nSum % 10
       # print(remainder)
       check_digit = 10 - remainder
       # print(check_digit)
       print(str(sequence) + str(check_digit), "encoded")