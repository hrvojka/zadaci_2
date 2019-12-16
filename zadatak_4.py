num = 0
n = 0
n1 = 0
n2 = 0

while num % 3 == 0 or num % 5 == 0:
    num=float(input("Unesi broj: "))
    if num % 3 == 0 and num % 5 == 0:
        n += 1
    if num % 5 == 0:
        n1 += 1
    if num % 3 == 0:
        n2 += 1

print("Unesena su {0} broja djeljiva sa 3 i 5".format(n,n1,n2))
print("Unesena su {1} broja djeljiva sa 5".format(n,n1,n2))
print("Unesena su {2} broja djeljiva sa 3".format(n,n1,n2))