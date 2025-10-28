count_games = int(input())

total_points = 0

point_counter_interval_1 = 0
point_counter_interval_2 = 0
point_counter_interval_3 = 0
point_counter_interval_4 = 0
point_counter_interval_5 = 0
point_counter_invalid = 0

percentage_point_counter_interval_1 = 0
percentage_point_counter_interval_2 = 0
percentage_point_counter_interval_3 = 0
percentage_point_counter_interval_4 = 0
percentage_point_counter_interval_5 = 0
percentage_point_counter_invalid = 0

for i in range(count_games):

    number = int(input())

    if 0 <= number <= 9:
        total_points += number * 0.20
        point_counter_interval_1 += 1
    elif 10 <= number <= 19:
        total_points += number * 0.30
        point_counter_interval_2 += 1
    elif 20 <= number <= 29:
        total_points += number * 0.40
        point_counter_interval_3 += 1
    elif 30 <= number <= 39:
        total_points += 50
        point_counter_interval_4 += 1
    elif 40 <= number <= 50:
        total_points += 100
        point_counter_interval_5 += 1
    else:
        total_points /= 2
        point_counter_invalid += 1


percentage_point_counter_interval_1 = (point_counter_interval_1 / count_games) * 100
percentage_point_counter_interval_2 = (point_counter_interval_2 / count_games) * 100
percentage_point_counter_interval_3 = (point_counter_interval_3 / count_games) * 100
percentage_point_counter_interval_4 = (point_counter_interval_4 / count_games) * 100
percentage_point_counter_interval_5 = (point_counter_interval_5 / count_games) * 100
percentage_point_counter_invalid = (point_counter_invalid / count_games) * 100


print(f"{total_points:.2f}")
print(f"From 0 to 9: {percentage_point_counter_interval_1:.2f}%")
print(f"From 10 to 19: {percentage_point_counter_interval_2:.2f}%")
print(f"From 20 to 29: {percentage_point_counter_interval_3:.2f}%")
print(f"From 30 to 39: {percentage_point_counter_interval_4:.2f}%")
print(f"From 40 to 50: {percentage_point_counter_interval_5:.2f}%")
print(f"Invalid numbers: {percentage_point_counter_invalid:.2f}%")