gracz1_nazwa = input('Podaj nazwe pierwszego gracza: ')
gracz2_nazwa = input('Podaj nazwe drugiego gracza: ')
gracz1_nazwa = gracz1_nazwa.capitalize()
gracz2_nazwa = gracz2_nazwa.capitalize()

# papier > kamien
# kamien > nozyce
# nozyce > papier

def porownanie (gracz1_ruch, gracz2_ruch, gracz1_nazwa, gracz2_nazwa):
    if gracz1_ruch == gracz2_ruch:
        print('Remis')
    elif gracz1_ruch == 'papier':
        if gracz2_ruch == 'kamien':
            gracz1_wygrywa(gracz1_nazwa)
        elif gracz2_ruch == 'nozyczki':
            gracz2_wygrywa(gracz2_nazwa)
        else:
            print('Taki ruch {gracz2_nazwa} nie istnieje \n')

    elif gracz1_ruch == 'kamien':
        if gracz2_ruch == 'nozyce':
            gracz1_wygrywa(gracz1_nazwa)
        elif gracz2_ruch == 'papier':
            gracz2_wygrywa(gracz2_nazwa)
        else:
            print('Taki ruch {gracz2_nazwa} nie istnieje \n')

    elif gracz1_ruch == 'nozyce':
        if gracz2_ruch == 'papier':
            gracz1_wygrywa(gracz1_nazwa)
        elif gracz2_ruch == 'kamien':
            gracz2_wygrywa(gracz2_nazwa)
        else:
            print('Taki ruch {gracz2_nazwa} nie istnieje \n')
    else:
        print(f'Taki ruch {gracz1_nazwa} nie istnieje \n')

def gracz1_wygrywa(gracz1_nazwa):
    print(f'Gracz {gracz1_nazwa} wygrywa \n')
    
def gracz2_wygrywa(gracz2_nazwa):
    print(f'Gracz {gracz2_nazwa} wygrywa \n')

while True:
    gracz1_ruch = input(f'{gracz1_nazwa} jaki wykonujesz ruch? (papier, kamien, nozyce): ')
    gracz2_ruch = input(f'{gracz2_nazwa} jaki wykonujesz ruch? (papier, kamien, nozyce): ')
    
    porownanie(gracz1_ruch, gracz2_ruch, gracz1_nazwa, gracz2_nazwa)
    
    komenda = input('Gramy dalej? (Tak, Nie): ')
    if komenda.lower() == 'tak':
        continue
    else:
        break