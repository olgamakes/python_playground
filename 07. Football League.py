fan_sector = ""
all_fans_in_sector_A = 0
all_fans_in_sector_B = 0
all_fans_in_sector_V = 0
all_fans_in_sector_G = 0

percentage_all_fans_in_sector_A = 0
percentage_all_fans_in_sector_B = 0
percentage_all_fans_in_sector_V = 0
percentage_all_fans_in_sector_G = 0

capacity = int(input())
all_fans = int(input())
for i in range(all_fans):
    fan_sector = input()
    if fan_sector == "A":
        all_fans_in_sector_A += 1
    elif fan_sector == "B":
        all_fans_in_sector_B += 1
    elif fan_sector == "V":
        all_fans_in_sector_V += 1
    elif fan_sector == "G":
        all_fans_in_sector_G += 1

percentage_all_fans_in_sector_A = (all_fans_in_sector_A / all_fans) * 100
percentage_all_fans_in_sector_B = (all_fans_in_sector_B / all_fans) * 100
percentage_all_fans_in_sector_V = (all_fans_in_sector_V / all_fans) * 100
percentage_all_fans_in_sector_G = (all_fans_in_sector_G / all_fans) * 100
fans_capacity_ration = (all_fans / capacity) * 100

print(f"{percentage_all_fans_in_sector_A:.2f}%")
print(f"{percentage_all_fans_in_sector_B:.2f}%")
print(f"{percentage_all_fans_in_sector_V:.2f}%")
print(f"{percentage_all_fans_in_sector_G:.2f}%")
print(f"{fans_capacity_ration:.2f}%")