# amount sold
# more than 10000 10%
# less than 5% commission

sales = input('How much product did you sell: $ ')
if sales.isdigit():

    if int(sales) >= 10000:
        print('You receive 10% commission.')
        commission = int(sales) * 0.10
        print(commission)

    else:
        print("You get 5% commission.")
        commission = int(sales) * 0.5
        print('$', commission)
else:
    print('Enter a number.')