import math
def pole_kwadratu(a):
    return a * a

def pole_prostokata(a, b):
    return a * b

def pole_trojkata(a, h):
    return 0.5 * a * h

def pole_trapezu(a, b, h):
    return (a + b) / 2 * h

def pole_kola(r):
    return math.pi * r ** 2

while True:
    print('Mozesz policzyc powierzchnie figur: \nkwadrat, prostokat, trojkat, trapez, kolo')
    decyzja = input('Jakiej figury policzyc pole? ')
    
    if decyzja == 'kwadrat':
        bok_kwadratu = input('Podaj bok kwadratu ')
        
        try:
            print(pole_kwadratu(int(bok_kwadratu)))
        except:
            print('Taka dlugosc nie istnieje!')

    if decyzja == 'prostokat':
        bok_prostokata1 = input('Podaj bok prostokata 1 ')
        bok_prostokata2 = input('Podaj bok prostokata 2 ')
        
        try:
            print(pole_prostokata(int(bok_prostokata1), int(bok_prostokata2)))
        except:
            print('Taka dlugosc nie istnieje!')

    if decyzja == 'trojkat':
        podstawa_trojkata = input('Podaj podstawe trojkata ')
        wysokosc_trojkata = input('Podaj wysokosc trojkata ')
        
        try:
            print(pole_trojkata(int(podstawa_trojkata), int(wysokosc_trojkata)))
        except:
            print('Taka dlugosc nie istnieje!')

    if decyzja == 'trapez':
        dol_trapezu = input('Podaj podstawe trapezu ')
        gora_trapezu = input('Podaj gore trapezu ')
        wysokosc_trapezu = input('Podaj wysokosc trapezu ')
        
        try:
            print(pole_trapezu(int(dol_trapezu), int(gora_trapezu), int(wysokosc_trapezu)))
        except:
            print('Taka dlugosc nie istnieje!')

    if decyzja == 'kolo':
        promien_kola = input('Podaj promien kola ')
        
        try:
            print(pole_kola(int(promien_kola)))
        except:
            print('Taka dlugosc nie istnieje!')
    print()
