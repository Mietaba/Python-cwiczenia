definicje = {1:'Marek', 2:'Jacek', 3:'Bartek'}
print(definicje)
while True:
    komenda = input('Powiedz co chcesz zrobic: \n1-dodac (imie, numer), 2-szukac (numer), 3-usuwac (numer), 4-wyswietlic liste, 9-END: ')
    if komenda == '1':
        definicje[int(input())] = input()
        print()
    elif komenda == '2':
        szukac = input('ktora pozycje chcesz szukac? ')
        print(definicje[int(szukac)])
        print()
    elif komenda == '3':
        usunac = input('ktora pozycje chcesz usunac? ')
        del definicje[int(usunac)]
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
