a = int(input("Početna vrijednost: "))
n = 0

if a < 1:
    print("Pogreška")
else:
    while a > 1:
        if a % 2 == 0:
            a = int(a/2)
            n += 1
        else:
            a = a*3+1
            n += 1
        if a != 1:
            print("Slijedeća vrijednost: {0}".format(a))
    else:
        print("Krajnja vrijednost: {0}, broj koraka: {1}".format(a,n))
