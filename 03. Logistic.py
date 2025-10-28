number_of_cargos = int(input())
total_tonnage = 0
transport_type = ""
total_price_minibus = 0
total_price_truck = 0
total_price_train = 0
total_tonnage_minibus = 0
total_tonnage_truck = 0
total_tonnage_train = 0
percent_tonnage_minibus = 0
percent_tonnage_truck = 0
percent_tonnage_train = 0

for i in range(number_of_cargos):

    cargo_tonnage = int(input())
    total_tonnage += cargo_tonnage

    if cargo_tonnage <= 3:
        price_per_ton_minibus = 200
        total_price_minibus += cargo_tonnage * price_per_ton_minibus
        total_tonnage_minibus += cargo_tonnage
    elif 4 <= cargo_tonnage <= 11:
        price_per_ton_truck = 175
        total_price_truck += cargo_tonnage * price_per_ton_truck
        total_tonnage_truck += cargo_tonnage
    elif cargo_tonnage >= 12:
        price_per_ton_train = 120
        total_price_train += cargo_tonnage * price_per_ton_train
        total_tonnage_train += cargo_tonnage


average_price_per_ton = (total_price_minibus + total_price_truck + total_price_train) / total_tonnage

percent_tonnage_minibus = total_tonnage_minibus / total_tonnage * 100
percent_tonnage_truck = total_tonnage_truck / total_tonnage * 100
percent_tonnage_train = total_tonnage_train / total_tonnage * 100

print(f"{average_price_per_ton:.2f}")
print(f"{percent_tonnage_minibus:.2f}%")
print(f"{percent_tonnage_truck:.2f}%")
print(f"{percent_tonnage_train:.2f}%")



