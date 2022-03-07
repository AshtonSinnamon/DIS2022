# Begin Program RomanNumerals
# 	Store values 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1
# 	Store roman: "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"
# 	Initialise numerals to empty string
# 	ask user for number between 1 and 3999
# 	If number in correct range
# 		For i = 0 to 12
# 			while number >= values[i]
# 				number = number – values[i]
# 				append corresponding roman to numerals
# 			End while
# 			increment i
# 		End for
# 	Else:
# 		Display error
# 	End If
# End Program RomanNumerals
#roman = {1000: M"", 900: "CM", 500: "D", 400: "CD", 100: "C", 90: "XC", 50: "L", 40: "XL", 10: "X", 9: "IX", 5: "V", 4: \
#    "IV", 1: "I"}
values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
roman = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
numerals = ""
number = int(input("Enter a number from 1 to 3999: "))
if number >= 1 and number <= 3999:
    for i in range(13):
        while number >= values[i]:
            number = number - values[i]
            numerals += roman[i]
        i += 1
    print(numerals)
else:
    print("Invalid Number")