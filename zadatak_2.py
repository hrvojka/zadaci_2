znamenka_1 = int(input("Unesi prvi (pozitivan jednoznamenkasti) broj: "))
znamenka_2 = int(input("Unesi drugi (pozitivan jednoznamenkasti) broj: "))
broj_1 = (int(str(znamenka_1) + str(znamenka_2)))
broj_2 = (int(str(znamenka_2) + str(znamenka_1)))

if broj_1 % 2 ==0 and broj_2 % 2 !=0:
    print(f"Parni brojevi stvoreni od znamenaka {znamenka_1} i {znamenka_2} su: {broj_1}.")
elif broj_1 % 2 !=0 and broj_2 % 2 ==0:
    print(f"Parni brojevi stvoreni od znamenaka {znamenka_1} i {znamenka_2} su: {broj_2}.")
elif broj_1 % 2 ==0 and broj_2 % 2 ==0:
    print(f"Parni brojevi stvoreni od znamenaka {znamenka_1} i {znamenka_2} su: {broj_1} i {broj_2}.")
else:
    print("Nema parnih brojeva.")
