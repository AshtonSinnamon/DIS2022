# ask the user to enter a sentence. count the number of each word in the sentence. i.e. The quick brown fox jumped over
# the lazy fox which was also brown due to the brown rain. 3 'The', 3'brown' etc.

words = {}
sentence = input("Enter a sentence: ").lower()
word_list = sentence.split()

for word in word_list:
    if word in words:
        words[word] += 1
    else:
        words[word] = 1
for k, v in words.items():
    print("The word,", k, "occurs", v, "times.")
