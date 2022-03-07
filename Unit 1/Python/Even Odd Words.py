even = '24680'
odd = '13579'


def middle_char(txt):
    return txt[(len(txt) - 1) // 2:(len(txt) + 2) // 2]


word = input('What is you word: ')
last_number = (word[-1])
if word.isalpha():
    #print(len(word))

    if str(len(word)) in even or len(word) % 2 == 0:
        print('Even')
        Half1 = word[0:len(word)//2]
        Half2 = word[len(word)//2:]
        print('The first half of the word is:', Half1)
        print('The second half of the word is:', Half2)
    else:
        print('The middle value of this string is', middle_char(word) + '.')
        print('The middle value of this string is', word[len(word)//2])
else:
    print('Input a single word.')
