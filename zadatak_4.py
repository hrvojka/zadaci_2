broj = 0
brojač_1 = 0
brojač_2 = 0
brojač_3 = 0

while broj % 3 == 0 or broj % 5 == 0:
    broj = float(input("Unesi broj: "))
    if broj % 3 == 0 and broj % 5 == 0:
        brojač_1 += 1
    if broj % 5 == 0:
        brojač_2 += 1
    if broj % 3 == 0:
        brojač_3 += 1

print(f"Unesena su {brojač_1} broja djeljiva sa 3 i 5")
print(f"Unesena su {brojač_2} broja djeljiva sa 5")
print(f"Unesena su {brojač_3} broja djeljiva sa 3")