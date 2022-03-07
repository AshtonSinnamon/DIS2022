password = input('Please input a password: ').strip()
passed = 0
valid_password = True

LC = False
UC = False
SC = False
numbers = False

if len(password) < 6 or len(password) > 20:
    valid_password = False
    print("Must be at least 6 characters and not exceed 20")


for character in password:
    if character.isupper():
        UC = True
    if character.islower():
        LC = True
    if not character.isalnum():
        SC = True
    if character.isnumeric():
        numbers = True


if LC == True:
    passed = passed + 1
if UC == True:
    passed = passed + 1
if SC == True:
    passed = passed + 1
if numbers == True:
    passed = passed + 1


if valid_password == True and passed >= 3:
    print('Your password is valid')


if (LC == False or UC == False or SC == False or numbers == False) and passed <= 2 and valid_password == True:
    print('Make sure that you have 3 of the following: A lowercase letter, and uppercase letter, a number or '
          '1 special character.')
