iznos = int(input("Unesi iznos: "))

broj_novcanica_od_50kn = int(iznos / 50)
broj_novcanica_od_20kn = int(iznos % 50 / 20)
broj_kovanica_od_5kn = int(iznos % 50 % 20 / 5)
broj_kovanica_od_2kn = int(iznos % 50 % 20 % 5 / 2)
broj_kovanica_od_1kn = int(iznos % 50 % 20 % 5 % 2)

print(f"""Broj novčanica od 50 kn: {broj_novcanica_od_50kn}
Broj novčanica od 20 kn: {broj_novcanica_od_20kn}
Broj kovanica od 5 kn: {broj_kovanica_od_5kn}
Broj kovanica od 2 kn: {broj_kovanica_od_2kn}
Broj kovanica od 1 kn: {broj_kovanica_od_1kn}""")
