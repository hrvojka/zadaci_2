x = (input("Trenutna plaća radnika: "))
x = float(x.replace(",","."))
y = int(input("Broj godina radnog staža: "))

if y >= 10:
    x = x + (x*y/100)
    x = round(x, 2)
    print("Nova (uvećana) plaća: {0}".format(x))
else:
    print("Uvjeti za povećanje plaće nisu zadovoljeni.")