num = input("Unesi broj: ")
lst = [int(i) for i in str(num)]
n=0

for i in reversed(lst):
    n += 1
    print(i**2)
print("Broj znamenki: {0}".format(n))
