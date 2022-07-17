import sys

no_of_tries = 5
word = 'kamila'
used_letters = []

user_word = []

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
    print('Uzyte ltery', used_letters)
    print()

for letter in word:
    user_word.append('_')

while True:
    letter = input('Podaj litere: ')
    used_letters.append(letter)

    found_indexes = find_indexes(word, letter)
    if len(found_indexes) == 0:
        print('Nie ma takiej litery') 
        no_of_tries -=1

        if no_of_tries == 0:
            print('Koniec gry')
            sys.exit(0)
    else:
        for index in found_indexes:
            user_word[index] = letter

        if ''.join(user_word) == word:
            print('Brawo! To jest to slowo')
            sys.exit(0)

    show_state_of_game()