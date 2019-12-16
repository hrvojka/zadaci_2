num= int(input("Unesi broj: "))
n=0
n1=0
n2=0
n3=0
n4=0
while num >= 50:
    n+=1
    num=num-50
if n>0:
    print("Broj novčanica od 50 kn: {0}".format(n))
while num >= 20:
    n1+=1
    num=num-20
if n1>0:
    print("Broj novčanica od 20 kn: {0}".format(n1))
while num >= 5:
    n2+=1
    num=num-5
if n2>0:
    print("Broj kovanica od 5 kn: {0}".format(n2))
while num >= 2:
    n3+=1
    num=num-2
if n3>0:
    print("Broj kovanica od 2 kn: {0}".format(n3))
while num >= 1:
    n4+=1
    num=num-1
if n4>0:
    print("Broj kovanica od 1 kn: {0}".format(n4))

