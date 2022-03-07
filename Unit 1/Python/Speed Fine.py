speed = 100
speed_of_vehicle = int(input('What was the speed of the vehicle: '))


extra_cost = (speed_of_vehicle - speed) * 5
int(extra_cost)

final_cost = 50 + extra_cost
extra_fine = 200


if speed_of_vehicle > 100 and speed_of_vehicle < 120:
    print('The ticket will cost $', 50 + extra_cost)
elif speed_of_vehicle > 120:
    cost2 = 250 + extra_cost
    final_cost_over_120 = 250 + extra_cost
    print('The ticket will cost $', cost2)

else:
    print('No Fine')
