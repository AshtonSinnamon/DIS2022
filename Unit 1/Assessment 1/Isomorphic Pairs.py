# Isomorphic Pairs
file = (open("task3_test_data.txt"))
contents = file.readlines()


def Isomorphic(word):
    pattern = ""
    for x in range(0, len(word)):
        count = 1
        j = x + 1
        Found = False
        while not Found and j < len(word):
            if word[x] == word[j]:
                pattern += " +" + str(count)
                x += 1
                Found = True
            else:
                j += 1
                count += 1
                Found = False
            if j + 1 > len(word):
                pattern += " 0"
    return pattern

for line in contents:
    word = line.strip("\n")
    words = word.split()
    word1 = words[0]
    word2 = words[1]

    length1 = len(word1)
    length2 = len(word2)

    if length1 == length2:
        word1_pattern1 = Isomorphic(word1) + " 0"
        word2_pattern2 = Isomorphic(word2) + " 0"

        if word1_pattern1 == word2_pattern2:
            print(word1, word2, "are isomorphs with repetition pattern", word1_pattern1)
        else:
            print(word1, word2, "are not isomorphs")
    else:
        print(word1, word2, "have different lengths")