

def con(word):
    for i in range(0, len(word)-1):
        print(word[i])
        Found = False
        if (ord(word[i]) + 1) == ord(word[i + 1]):
            return False
        return True


word = "MONDAY"
if con("word"):
    print("Con")
else:
    print("Not")
