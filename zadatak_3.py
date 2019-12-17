num= int(input("Unesi iznos: "))

num1=int(num/50)
num2=int((num%50)/20)
num3=int((num%50%20)/5)
num4=int((num%50%20%5)/2)
num5=int((num%50%20%5%2)/1)

print("""Broj novčanica od 50 kn: {0}
Broj novčanica od 20 kn: {1}
Broj kovanica od 5 kn: {2}
Broj kovanica od 2 kn: {3}
Broj kovanica od 1 kn: {4}""".format(num1, num2,num3,num4,num5 ))
