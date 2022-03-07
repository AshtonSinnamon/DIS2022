english = input("Please input a sentence: ")
words = english.split()
pigLatin = ""
for word in words:
    if len(word) == 1:
        latinWord += "ay"
    else:
        latinWord = word[1:]+word[0]+"ay"
    pigLatin = pigLatin + latinWord + " "
print(pigLatin.upper())