import sys
import os

no_of_tries = 5
used_letters = []
user_word = []

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def find_indexes(word, letter):
    indexes = []

    for index, letter_in_word in enumerate(word):
        if letter == letter_in_word:
            indexes.append(index)
    return indexes

def show_state_of_game():
    print()
    print(user_word)
    print('Pozostalo prob :', no_of_tries)
    print('Uzyte litery', used_letters)
    print()

word = input('Podaj hasło dla drugiego gracza: ').lower()
while word.isalpha() != True:
    print('To co wpisałeś nie jest słowem!')
    word = input('Podaj hasło dla drugiego gracza: ').lower()
cls()

for letter in word:
    user_word.append('_')

while True:
    show_state_of_game()
    
    letter = input('Podaj litere: ').lower()
    while (len(letter) != 1 or letter.isalpha() != True):
        print('To co wpisałeś nie jest litera!')
        letter = input('Podaj litere: ').lower()

    used_letters.append(letter)

    found_indexes = find_indexes(word, letter)
    if len(found_indexes) == 0:
        print('Nie ma takiej litery') 
        no_of_tries -=1

        if no_of_tries == 0:
            print('Koniec gry!')
            sys.exit(0)
    else:
        for index in found_indexes:
            user_word[index] = letter

        if ''.join(user_word) == word:
            cls()
            show_state_of_game()
            print('Brawo! To jest to slowo')
            sys.exit(0)

