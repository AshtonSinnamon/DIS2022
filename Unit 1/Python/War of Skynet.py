codedMsg = input("What is the coded message: ")
cleanMsg = ""
words = codedMsg.split()
words.reverse()
for word in words:
    if word[0].isupper():
        cleanMsg = cleanMsg + word + " "
print(cleanMsg)