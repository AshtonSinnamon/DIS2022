msg = "Digital Solutions at SPS "
vowels = "aeiou"

total = 0

for i in range(len(msg)):
    if msg[i].lower() in vowels:
        total += 1

print("Vowel total", total)