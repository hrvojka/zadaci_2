iznos = int(input("Unesi iznos: "))

broj_novcanica_od_50kn = int(iznos / 50)
broj_novcanica_od_20kn = int(iznos % 50 / 20)
broj_kovanica_od_5kn = int(iznos % 50 % 20 / 5)
broj_kovanica_od_2kn = int(iznos % 50 % 20 % 5 / 2)
broj_kovanica_od_1kn = int(iznos % 50 % 20 % 5 % 2)

print("""Broj novčanica od 50 kn: {0}
Broj novčanica od 20 kn: {1}
Broj kovanica od 5 kn: {2}
Broj kovanica od 2 kn: {3}
Broj kovanica od 1 kn: {4}""".format(broj_novcanica_od_50kn, broj_novcanica_od_20kn, broj_kovanica_od_5kn, broj_kovanica_od_2kn, broj_kovanica_od_1kn))
