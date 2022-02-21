from errno import EILSEQ


definicje = {1:'Marek', 2:'Jacek', 3:'Bartek'}
print(definicje)
while True:
    komenda = input('Powiedz co chcesz zrobic: \n'
    '1-dodac (imie, numer), 2-szukac (numer), 3-usuwac (numer), 4-wyswietlic liste, 9-END: ')
    if komenda == '1':
        definicje[int(input())] = input()
        print()
    elif komenda == '2':
        szukac = input('ktora pozycje chcesz szukac? ')
        szukac = int(szukac)
        if int(szukac) in definicje:
            print(definicje[szukac])
        else:
            print('Pozycja not exist')
        print()
    elif komenda == '3':
        usunac = input('ktora pozycje chcesz usunac? ')
        usunac = int(usunac)
        if usunac in definicje:
            del definicje[usunac]
        else:
            print('Pozycja not exist')
        print()
    elif komenda == '4':
        for d in definicje:
            print(d, definicje[d])
        print()
    elif komenda == '9':
        break

    else:
        print('zly numer!')

print()
for d in definicje:
    print(d, definicje[d])
