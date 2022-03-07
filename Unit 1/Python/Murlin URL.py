file = open("../TextFiles/Murlin")
url = file.readlines()
num = url.pop(0).strip("\n")
for i in range(1, len(url)):
    url = url[i]
    decoded = ""
    j = 0
    while j < len(url):
        char = url[j]
        #print("c1", char)
        if char != "%":
            decoded += char
            j += 1

        else:
            letters = {
                "A" or "a": 10,
                "B" or "b": 11,
                "C" or "c": 12,
                "D" or "d": 13,
                "E" or "e": 14,
                "F" or "f": 15
            }
            murlin = url[j + 1: j + 3]
            m1 = murlin[0]
            m2 = murlin[1]
            if m1 in letters:
                m1 = letters[m1]
                val = m1 * 16
            else:
                val = m1 * 16

            val += m2
            char = ord(val)
            decoded += char
            j += 3
    print(decoded)
    #
    #             hexadecimal = val + m2
    #             char = ord(hexadecimal)
    #             j += 3
    #
    #         print("C", char, decoded, j)
    # print("Decoded", decoded)





















    # print(decoded)

# letters = {
#     "A" or "a": 10,
#     "B" or "b": 11,
#     "C" or "c": 12,
#     "D" or "d": 13,
#     "E" or "e": 14,
#     "F" or "f": 15
# }
#
# file = open("TextFiles/Murlin")
# urls = file.readlines()
# num = urls.pop(0).strip("\n")
# for url in urls:
#     print("Url", url)
#     url = url.strip("\n")
#     decoded = ""
#     j = 0
#     while j < len(url):
#         char = url[j]
#         if char != "%":
#             decoded += char
#             print("C", char, decoded)
#             j += 1
#         else:
#             murlin = url[j + 1: j + 3]
#             m1 = murlin[0]
#             m2 = murlin[1]
#             if m1.isdigit():
#                 val = m1 * 16
#             else:
#                 if m1 in letters:
#                     m1 = letters[m1]
#                     # print(m1)
#                     val = m1 * 16
#
#                 hexa = val + m2
#                 # print(hexa)
#                 char = ord(hexa)
#                 j += 3
#             decoded += char
#             j += 3
    # print(decoded)

# msg = "http://%77%77%77%2E%6D%61%6C%77%61%72%65%52%75%73%2E%63%6F%6D/www.furrykittens.com"
# msg2 = msg.split("%")
# decoded = ""
# print(msg2)
# for line in contents:
#     for x in line.split("%"):
#         if x.isalnum():
#             # print(toDecimal(x))
#             char = toDecimal(x)
#             print(char)
#             if char <= 92 and char >= 65:
#                 new = char - 65
#                 print("L", char, new)
#                 letterNew = chr(new)
#                 print("LN", letterNew)
#                 decoded = decoded + letterNew
#             elif char >= 97 and char <= 122:
#                 new = char - 97
#                 print("C", char, new)
#                 letterNew = chr(new)
#                 print("LN", letterNew)
#                 decoded = decoded + letterNew
#             else:
#                 new = char - 46
#                 print("P", char, new)
#                 letterNew = chr(new)
#                 print("LN", letterNew)
#                 decoded = decoded + letterNew
#         else:
#             decoded = decoded + x
#
# print(decoded)

# "1": 1,
# "2": 2,
# "3": 3,
# "4": 4,
# "5": 5,
# "6": 6,
# "7": 7,
# "8": 8,
# "9": 9,
