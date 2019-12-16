a = int(input("Početna vrijednost: "))
n = 0

if a < 1:
    print("Pogreška")
else:
    while a > 1:
        if a % 2 == 0:
            x = int(a/2)
            n += 1
        else:
            x = a*3+1
            n += 1
        print("Slijedeća vrijednost: {0}".format(x))
        a = x
    print("Krajnja vrijednost: {0}, broj koraka: {1}".format(a,n))
