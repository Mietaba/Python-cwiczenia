gracz1_nazwa = input('Podaj nazwe pierwszego gracza: ')
gracz2_nazwa = input('Podaj nazwe drugiego gracza: ')
gracz1_nazwa = gracz1_nazwa.capitalize()
gracz2_nazwa = gracz2_nazwa.capitalize()
gracz1_punkty = 0
gracz2_punkty = 0

# papier > kamien
# kamien > nozyce
# nozyce > papier

def porownanie (gracz1_ruch, gracz2_ruch, gracz1_nazwa, gracz2_nazwa):
    wynik = 0
    if gracz1_ruch == 'papier' or gracz1_ruch == 'kamien' or gracz1_ruch == 'nozyce':
        if gracz2_ruch == 'papier' or gracz2_ruch == 'kamien' or gracz2_ruch == 'nozyce':
            if gracz1_ruch == gracz2_ruch:
                print('Remis')
            elif gracz1_ruch == 'papier':
                if gracz2_ruch == 'kamien':
                    wynik = gracz1_wygrywa(gracz1_nazwa)
                elif gracz2_ruch == 'nozyczki':
                    wynik = gracz2_wygrywa(gracz2_nazwa)

            elif gracz1_ruch == 'kamien':
                if gracz2_ruch == 'nozyce':
                    wynik = gracz1_wygrywa(gracz1_nazwa)
                elif gracz2_ruch == 'papier':
                    wynik = gracz2_wygrywa(gracz2_nazwa)

            elif gracz1_ruch == 'nozyce':
                if gracz2_ruch == 'papier':
                    wynik = gracz1_wygrywa(gracz1_nazwa)
                elif gracz2_ruch == 'kamien':
                    wynik = gracz2_wygrywa(gracz2_nazwa)
            return wynik
        else:
            print(f'{gracz2_nazwa} taki ruch nie istnieje')
    else:
        print(f'{gracz1_nazwa} taki ruch nie istnieje')

def gracz1_wygrywa(gracz1_nazwa):
    print(f'Gracz {gracz1_nazwa} wygrywa \n')
    return 1
    
def gracz2_wygrywa(gracz2_nazwa):
    print(f'Gracz {gracz2_nazwa} wygrywa \n')
    return 2

while True:
    gracz1_ruch = input(f'{gracz1_nazwa} jaki wykonujesz ruch? (papier, kamien, nozyce): ')
    gracz2_ruch = input(f'{gracz2_nazwa} jaki wykonujesz ruch? (papier, kamien, nozyce): ')
    
    wynik = porownanie(gracz1_ruch, gracz2_ruch, gracz1_nazwa, gracz2_nazwa)
    if wynik == 1:
        gracz1_punkty += 1
    elif wynik == 2:
        gracz2_punkty += 1

    komenda = input('Gramy dalej? (Tak, Nie): ')
    if komenda.lower() == 'tak':
        continue
    else:
        print(f'{gracz1_nazwa} zdobytych punktow {gracz1_punkty}')
        print(f'{gracz2_nazwa} zdobytych punktow {gracz2_punkty}')
        break
