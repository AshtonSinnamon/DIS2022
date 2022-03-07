# Task
# Jacob has been passing notes in class without a problem until his teacher intercepted one today.
# In order to prevent future embarrassment, he wants a way to encode his notes so his teacher cannot read them.
# Help him by writing a program that encrypts a string by switching every letter with alphabetical position i
# # with the letter with alphabetical position 26-i. For example the letter 'm' is letter 12, so it becomes 26-12 = 14,
# # letter 14 which is 'o'. Note counting begins at zero. Can you suggest why?
#
msg = "My secret message"
encrypted_msg = ""


for letter in msg.lower():
    position = ord(letter)
    #print(position)
    if letter.isalpha():
        position = ord(letter) - 97
        print(position)
        #print(position)
        new_position = 122 - position
        new_letter = chr(position)
        print(new_letter)
    encrypted_msg = encrypted_msg + new_letter
print(encrypted_msg)

#
# ENCODE a secret message
# Scramble the alphabet, read a secret message, encode it, print scrambled

# import random
#
#
# def main():
#     encryption()
#
#     decryption()
#
#
# def encryption():
#     encrypt = ["*"] * 26  # all letters available
#     print(encrypt)
#
#     print("Alphabet:  ", end="")
#     for numbah in range(26):
#         # converts numbah into a letter
#         letter = chr(numbah + 65)  # converts 0-25 --> 'A' = 'Z'
#
#         print(letter, end="")
#
#         # Reminder: find an empty position for that letter to be placed
#
#         notfound = True
#         while notfound:
#             possible_position = random.randint(0, 25)
#             if encrypt[possible_position] == "*":
#                 notfound = False
#         encrypt[possible_position] = letter
#
#     print("\nScrambled: ", end="")
#     for numbah in range(26):
#         print(encrypt[numbah], end="")
#
#     print("\n\n")
#
#     msg = input("Now, please type your secret message to encode: ")
#     print("Your secret message:  " + msg)
#     print("Your message encoded: ", end="")
#
#     # reminder non alphabetic characters should 'float thru' unchanged!
#
#     for alpha in msg.upper():
#         if alpha < "A" or alpha > "Z":
#             print(alpha, end="")
#         else:
#             print(encrypt[ord(alpha) - 65], end="")
#
#     print("\n")
#
#
# def decryption():
#     scram_alph = input("Input the scrambled alphabet from the early prog:  ")
#
#     scram_mess = input("Input the scrambled messgae you want decoded:  ")
#
#
# main()