x = int(input("Unesi prvi (pozitivan jednoznamenkasti) broj: "))
y = int(input("Unesi drugi (pozitivan jednoznamenkasti) broj: "))
x1 = (int(str(x)+str(y)))
x2 = (int(str(y)+str(x)))

if x1 % 2 ==0 and x2 % 2 !=0:
    print("Parni brojevi stvoreni od znamenaka {0} i {1} su: {2}.".format(x,y,x1,x2))
elif x1 % 2 !=0 and x2 % 2 ==0:
    print("Parni brojevi stvoreni od znamenaka {0} i {1} su: {3}.".format(x,y,x1,x2))
elif x1 % 2 ==0 and x2 % 2 ==0:
    print("Parni brojevi stvoreni od znamenaka {0} i {1} su: {2} i {3}.".format(x,y,x1,x2))
else:
    print("Nema parnih brojeva.")
