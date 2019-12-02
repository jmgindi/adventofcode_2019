f = open("12_01_01.txt", "r")

total = 0

for mass in f.readlines():
    fuel = (int(mass) // 3) - 2
    total += fuel

print(total)
