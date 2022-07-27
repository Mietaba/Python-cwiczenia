import random
import string

password = []
characters_left = -1

def update_characters_left(number_of_characters):
    global characters_left
    
    while True:
        if number_of_characters < 0 or number_of_characters > characters_left:
            print('Liczba znakow spoza przedzialu 0,', characters_left)
            number_of_characters = int(input('Podaj liczbe jeszcze raz: '))
        else:
            characters_left -= number_of_characters
            print('Pozostalo znakow', characters_left)
            return number_of_characters

while True:
    password_lenght = int(input('Jak dlugie ma byc haslo? '))
    if password_lenght < 5:
        print('Haslo musi miec minimum 5 znakow, sprobuj jeszcze raz.')
    else:
        characters_left = password_lenght
        break

lowercase_letters = int(input('Ile malych liter ma miec haslo? '))
lowercase_letters = update_characters_left(lowercase_letters)

uppercase_letters = int(input('Ile duzych liter ma miec haslo? '))
uppercase_letters = update_characters_left(uppercase_letters)

special_characters = int(input('Ile znakow specjalnych ma miec haslo? '))
special_characters = update_characters_left(special_characters)

digits = int(input('Ile cyfr ma miec haslo? '))
digits = update_characters_left(digits)

if characters_left > 0 :
    print('Nie wszystkie znaki zosyaly wykorzystane, zostana one uzupelnione malymi literami')
    lowercase_letters += characters_left

print()
print('Dlugosc hasla:', password_lenght)
print('Male litery:', lowercase_letters)
print('Duze litery:', uppercase_letters)
print('Znake specjalne:', special_characters)
print('Cyfry:', digits)

for _ in range(password_lenght):
    if lowercase_letters > 0:
        password.append(random.choice(string.ascii_lowercase))
        lowercase_letters -= 1
    if uppercase_letters > 0:
        password.append(random.choice(string.ascii_uppercase))
        uppercase_letters -= 1
    if special_characters > 0:
        password.append(random.choice(string.punctuation))
        special_characters -= 1
    if digits > 0:
        password.append(random.choice(string.digits))
        digits -= 1

random.shuffle(password)
print('Wygenerowane haslo:', ''.join(password))
