wej = int(input())
przyb = 9
delta = pow(10, -przyb)
fun = lambda xk, a: (2*xk/3)+(a/(3*pow(xk, 2)))
x2 = 1
x1 = 10000
if wej == 0:
    print(0)
else:
    while abs(x2-x1) > delta:
        x1 = x2
        x2 = fun(x1, wej)
    print(round(x2, przyb))