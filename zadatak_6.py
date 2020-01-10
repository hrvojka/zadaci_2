# Za znamenku u unesenom broju program ispisuje kvadrat svake znamenke (polazeći od posljednje) i ukupan broj znamenki..

broj = input("Unesi broj: ")
lista = [int(znamenka) for znamenka in str(broj)]
brojač = 0

for znamenka in reversed(lista):
    brojač += 1
    print(znamenka**2)
print(f"Broj znamenki: {brojač}")
