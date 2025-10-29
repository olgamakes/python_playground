months = int(input())
water = 20
internet = 15
others = 0
other_per_month = 0

total_electricity = 0
total_water = 0
total_internet = 0
total_other = 0
total_all = 0

for i in range(months):
    electricity = float(input())
    total_electricity += electricity
    total_water += water
    total_internet += internet
    total_other += (electricity + water + internet) + (electricity + water + internet) * 0.20


total_all = total_other + total_electricity + total_water + total_internet

average_all_costs = total_all / months

print(f"Electricity: {total_electricity:.2f} lv")
print(f"Water: {total_water:.2f} lv")
print(f"Internet: {total_internet:.2f} lv")
print(f"Other: {total_other:.2f} lv")
print(f"Average: {average_all_costs:.2f} lv")
