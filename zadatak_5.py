početna_vrijednost = int(input("Početna vrijednost: "))
brojač = 0

if početna_vrijednost < 1:
    print("Pogreška")
else:
    while početna_vrijednost > 1:
        if početna_vrijednost % 2 == 0:
            početna_vrijednost = int(početna_vrijednost / 2)
            brojač += 1
        else:
            početna_vrijednost = početna_vrijednost * 3 + 1
            brojač += 1
        if početna_vrijednost != 1:
            print(f"Slijedeća vrijednost: {početna_vrijednost}")
    else:
        print(f"Krajnja vrijednost: {početna_vrijednost}, broj koraka: {brojač}")
