#wprowadzanie liczb
a = float(input())
b = float(input())
"""
sprawdzanie czy obie liczby są mniejsze od zera
lub jedna z nich mniejsza od zera
"""
if a < 0 and b<0:
    print("Jedna z liczb mniejsza od zera")
    exit()
if a < 0:
    a = abs(a)
if b < 0:
    b = abs(b)
#wypisywanie wszystkich wyników
print("suma: %f" % (a+b))
print("różnica: %f" % (a-b))
print("iloczyn: %f" % (a*b))
if a*b == 10:
    print("Yay!")
print("iloraz: %f" % (a/b))
print("kwadrat pierwszej liczby: %f" % (a*a))
print("kwadrat drugiej liczby: %f" % (b*b))
print("pierwiastek drugiego stopnia pierwszej liczby: %f" %(pow(a,1/2)))
print("pierwiastek drugiego stopnia drugiej liczby: %f" %(pow(b,1/2)))