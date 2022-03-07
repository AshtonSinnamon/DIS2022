Weight = float(input('What is your weight in kilograms: '))
Height = float(input('What is your height in meters: '))

square_height = Height * Height

BMI = Weight / square_height
print(BMI)

if BMI >= 18.5 and BMI <= 24.9:
    message = 'You are healthy'
elif BMI >= 25:
    message = 'You are above the healthy range'
else:
    message = 'You are below the healthy range'
print(message)
