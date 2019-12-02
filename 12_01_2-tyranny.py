f = open("12_01_01.txt", "r")

total = 0

for mass in f.readlines():
    fuel = (int(mass) // 3) - 2
    fuelextra = fuel // 3 - 2
    while fuelextra >= 0:
        print(f"fuel before addition is: {fuel}")
        print(f"extra fuel to be added is: {fuelextra}")
        fuel += fuelextra
        print(f"total fuel is now: {fuel}")
        fuelextra = fuelextra // 3 - 2

        
    total += fuel

print(f"total fuel is: {total}")
