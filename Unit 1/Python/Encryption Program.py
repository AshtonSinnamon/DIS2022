msg = "Hello World"
encrypted_msg = ""

for letter in msg.lower():
    position = ord(letter)
    #print(position)
    if letter.isalpha():
        position = ord(letter) - 97
        #print(position)
        position = 122 - position
        #print(position)
    letterNew = chr(position)
    #print(letter)
    encrypted_msg = "{0}{1}".format(encrypted_msg, letterNew)
print("Your Message:", encrypted_msg)






# 107
# 111
#