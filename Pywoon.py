import random
from turtle import *

# Funkcija kraja
def ending():
    end_program = input('Type anything to quit the program: ')
    if end_program == end_program:
        print('Bye!')


# Tajne riječi
secret_word = ['alert', 'arise', 'actor', 'adult',
               'boost', 'brain', 'brown', 'built',
               'carry', 'child', 'close', 'count',
               'dance', 'dream', 'drive', 'drink',
               'early', 'enjoy', 'empty', 'enter',
               'fault', 'field', 'flash', 'fluid',
               'globe', 'grand', 'great', 'gross',
               'happy', 'house', 'human', 'heavy',
               'issue', 'input', 'index', 'image',
               'juice', 'joint', 'jelly', 'jeans',
               'known', 'knock', 'knife', 'kills',
               'light', 'level', 'leave', 'learn',
               'mixer', 'meals', 'marry', 'magic',
               'novel', 'noise', 'newly', 'night',
               'ought', 'other', 'order', 'offer',
               'paint', 'paper', 'round', 'royal',
               'share', 'sharp', 'shape', 'score',
               'taken', 'teach', 'thank', 'thick',
               'upset', 'usage', 'usual', 'upper',
               'value', 'video', 'viral', 'voice',
               'worst', 'whole', 'world', 'wrong',
               'xonox', 'xterm', 'xueta', 'xerox',
               'youth', 'years', 'young', 'yards',
               'zilla', 'zeros', 'zorse', 'zokor']

# Koliko si puta pokušo pogodit
tries = 0

# Max koliko možeš pogađat
guess_limit = 6

# Tajna riječ podjeljena na slova
secret_word_letters = []

# Random index na kojemu se nalazi tajna riječ
secret_word_number = random.randint(0, 95)

# Pogođena riječ rastavljena na slova
guess_letters = []

title('Pywoon')

print('''
Welcome to Pywoon!
Guess the correct word in the least amount of tries
Rules:
- Every word has 5 letters
- X = Correct letter in correct place
- O = Correct letter in wrong place
- _ = Wrong letter
- If your guess has less than 5 letters 
  add any sign at the end

Good Luck ;)
''')

# Podjeli riječi s indexa koji je secret_word_number na slova i doda ih u listu
for letters in secret_word[secret_word_number]:
    secret_word_letters.append(letters)

# Dokle su tries(pokušaji) manji od guess_limit(max pokušaja) radi slijedeće
while tries < guess_limit:
    # Unos riječi
    guess = input('Guess the word: ').lower()
    # Odgovor na koliko je stvari točno
    answer_mark = ''
    # Index na kojemu se nalazi odgovor
    answer_index = 0
    # Briše prošla pogođena slova
    guess_letters.clear()

    # Podjeli pogođenu riječ na slova
    for letters_of_guess in guess:
        guess_letters.append(letters_of_guess)

    penup()
    goto(-207.5, (325 - (tries * 110)))

    for answers in guess_letters:

        if answers == secret_word_letters[answer_index]:

            pendown()
            fillcolor('green')
            begin_fill()
            forward(75)
            right(90)
            forward(100)
            right(90)
            forward(75)
            right(90)
            forward(100)
            right(90)
            penup()
            forward(85)
            end_fill()

            if guess == secret_word[secret_word_number]:
                print(f'You won in {tries} tries!')
                ending()
                break

            # Ako je točno slovo na krivom mjestu dodaj o
        elif answers in secret_word_letters and guess_letters[answer_index] != secret_word_letters[answer_index]:
            # answer_mark += 'O'
            pendown()
            fillcolor('yellow')
            begin_fill()
            forward(75)
            right(90)
            forward(100)
            right(90)
            forward(75)
            right(90)
            forward(100)
            right(90)
            penup()
            forward(85)
            end_fill()

        else:
            # answer_mark += '_'
            pendown()
            fillcolor('gray')
            begin_fill()
            forward(75)
            right(90)
            forward(100)
            right(90)
            forward(75)
            right(90)
            forward(100)
            right(90)
            penup()
            forward(85)
            end_fill()
        answer_index += 1

    tries += 1
    print(answer_mark)

else:
    print(f'Sorry you failed, the word was "{secret_word[secret_word_number]}"!')
    ending()
