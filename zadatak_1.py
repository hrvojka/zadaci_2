trenutna_plaća_radnika = (input("Trenutna plaća radnika: "))
trenutna_plaća_radnika = float(trenutna_plaća_radnika.replace(",", "."))
broj_godina_radnog_staža = int(input("Broj godina radnog staža: "))

if broj_godina_radnog_staža >= 10:
    uvećana_plaća_radnika = trenutna_plaća_radnika + (trenutna_plaća_radnika * broj_godina_radnog_staža / 100)
    uvećana_plaća_radnika = round(uvećana_plaća_radnika, 2)
    print(f"Nova (uvećana) plaća: {uvećana_plaća_radnika}")
else:
    print("Uvjeti za povećanje plaće nisu zadovoljeni.")