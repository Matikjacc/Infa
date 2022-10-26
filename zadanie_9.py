saldo = 6000
ostop = False
while True:
    if ostop == True:
        print("Co chcesz zrobić w kolejnym kroku?")
    print("1.Wpłata")
    print("2.Wypłata")
    print("3.Sprawdż saldo")
    print("4.Wyjdź")
    wyb = int(input())
    if wyb == 1:
        print("Podaj PIN")
        pin = int(input())
        if pin != 2137:
            exit()
        print("Ile chcesz wpłacić?")
        il_p = int(input())
        saldo+=il_p
    if wyb == 2:
        print("Podaj PIN")
        pin = int(input())
        if pin != 2137:
            exit()
        print("Ile chcesz wypłacić?")
        il_p = int(input())
        if saldo-il_p < 0:
            print("niewystarczająca ilość środków na koncie")
        else:
            saldo-=il_p
    if wyb == 3:
        print("Podaj PIN")
        pin = int(input())
        if pin != 2137:
            exit()
        print("Saldo: %d" %(saldo))
    if wyb == 4:
        exit()
    ostop = True
