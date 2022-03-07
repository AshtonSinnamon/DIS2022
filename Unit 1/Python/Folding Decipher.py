msg = "II*REOA*LAI*NYWLRVMD"
# new_msg = ""
#
#
# def FirstLetter():
#     FL = ord(msg[0]) - 64
#     return FL
#
#
# print(FirstLetter())
# # print(20 % 3)
# # print((20 % 3) % 3)
#

# rows = len(msg) // coloumns
#
# if coloumns % 3 < 0:
#     rows += 1
# print(coloumns, rows)
#
# for i in range(1, coloumns):
#     for char in msg:
#         if char.isalpha():
#             new_msg = new_msg + msg + coloumns
#         else:
#             new_msg = new_msg + " "
# print(new_msg)
key = ((ord(msg[0]) - 64) % 3) + 3
# coloumns = (key % 3) + 3
rows = len(msg) // 3
if len(msg) % 3 > 0:
    rows += 1
cleanMsg = ""
for j in range(0, rows):
    cleanMsg += msg[j]
    for i in range(1, key):
        cleanMsg += msg[j + (rows * i)]
print(cleanMsg)
