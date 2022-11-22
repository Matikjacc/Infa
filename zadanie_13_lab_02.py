import random
#Exit code -1 - Wybór niepoprawny
#Exit code -2 - Tablice nie są tej samej długości

table_1 = [1,2,3,4,5]
table_2 = [2,3,4,5,6]
dictionary = {}

while True:
    print("Wybierz typ operacji na liście, słowniku")
    print("1.Zapełnij listę/Dopisz elementy do niej")
    print("2.Połącz obie listy w słownik")
    print("3.Połącz obie listy w słownik losowo")
    print("4.Zamień słownik na listy")
    print("5.Wyczyść listy")
    print("6.Wyjdź z programu")
    print(f"Obecny stan listy1 = {table_1}, długość = {len(table_1)} , obecny stan listy2 = {table_2}, długość = {len(table_2)}")
    print(f"Obecny stan słownika = {dictionary}")
    wybór = input()
    if not wybór.isdigit():
        exit(-1)

    #Wczytywanie list lub dodawanie elementów do listy
    if int(wybór) == 1:
        print("Aby wyczyścić listy wpisz '0', aby kontynnuować '1'")
        print(f"Obecny stan listy1 = {table_1}, długość = {len(table_1)} , obecny stan listy2 = {table_2}, długość = {len(table_2)}")
        czy_wyczyścic = input()
        if not czy_wyczyścic.isdigit():
            exit(-1)
        if int(czy_wyczyścic) == 0:
            table_1 = []
            table_2 = []
        print("Aby zacząć wpisywać wpisz 'S' ,aby przejść do następnej listy wpisz 'Next', aby zakończyć wpisywanie wpisz 'Exit'")
        wej = input()
        ignorowanie_długości: bool = True
        nast_lis = False
        if wej == 'S' or wej == 's':
            while ignorowanie_długości:
                while True:
                    print(f"Obecny stan listy1 = {table_1}, długość = {len(table_1)} , obecny stan listy2 = {table_2}, długość = {len(table_2)}")
                    if not nast_lis:
                        print("Obecnie edytujesz listę pierwszą, aby przejść do następnej listy wpisz 'Next'")
                    else:
                        print("Obecnie edytujesz listę drugą, aby zakończyć wpisywanie wpisz 'Exit'")
                    wej = input()
                    if wej.lower() == 'exit':
                        break
                    if wej.lower() == 'next':
                        nast_lis = True
                        continue
                    if not wej.isdigit():
                        if not nast_lis:
                            table_1.append(wej)
                            continue
                        else:
                            table_2.append(wej)
                            continue
                    if not nast_lis:
                        table_1.append(int(wej))
                    else:
                        table_2.append(int(wej))
                if len(table_1) != len(table_2):
                    print("Listy nie są tej samej długośći. Czy chcesz kontynnuować?(Tak/Nie)")
                    odpowiedź = input()
                    if(odpowiedź.lower() == 'tak'):
                        ignorowanie_długości = False
                else:
                    break


    #łączenie list w słownik


    if int(wybór) == 2:
        if (len(table_1) != len(table_2)):
            print("Tablice muszą być tej samej długości aby połączyć je w słowniki, dopisz lub usuń elementy z jednej z list")
        else:
            for i in range(len(table_1)):
                dictionary[table_1[i]] = table_2[i]

    #łaczenie losowo list w słownik
    if int(wybór) == 3:
        if (len(table_1) != len(table_2)):
            print("Tablice muszą być tej samej długości aby połączyć je w słowniki, dopisz lub usuń elementy z jednej z list")
        else:
            print(len(table_1))
            for i in range(len(table_1)):
                rand = random.randint(0,10)
                if rand <=5:
                    dictionary[table_1[i]] = table_2[i]
                else:
                    dictionary[table_2[i]] = table_1[i]

    #zamień słownik w listę

    if int(wybór) == 4:
        table_1 = []
        table_2 = []
        for element in dictionary:
            table_1.append(element)
            table_2.append(dictionary[element])

    # czyszczenie list

    if int(wybór) == 5:
        table_1 = []
        table_2 = []

    #wyjdź z programu
    if int(wybór) == 6:
        exit(0)