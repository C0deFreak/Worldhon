import random

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

print('''
Welcome to Pywoon!
Guess the correct word in the least amount of tries
Rules:
- Every word has 5 letters
- x = Correct letter in correct place
- o = Correct letter in wrong place
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
    # Dodavanje pokušaja
    tries += 1
    # Odgovor na koliko je stvari točno
    answer_mark = ''
    # Index na kojemu se nalazi odgovor
    answer_index = 0
    # Briše prošla pogođena slova
    guess_letters.clear()

    # Podjeli pogođenu riječ na slova
    for letters_of_guess in guess:
        guess_letters.append(letters_of_guess)

    # Petlje za provjeravanje
    if guess == secret_word[secret_word_number]:
        print(f'You won in {tries} tries!')
        break

    else:
        # Za svako slovo u listi
        for answers in guess_letters:

            # Ako je točno slovo na točnom mjestu dodaj x
            if answers == secret_word_letters[answer_index]:
                answer_mark += 'x'
            # Ako je točno slovo na krivom mjestu dodaj o
            elif answers in secret_word_letters and guess_letters[answer_index] != \
                    secret_word_letters[answer_index]:
                answer_mark += 'o'
            # Ako je krivo slovo dodaj _
            else:
                answer_mark += '_'
            answer_index += 1

    print(answer_mark)
else:
    print(f'Sorry you failed, the word was "{secret_word[secret_word_number]}"!')
    end_program = input('Type anything to quit the program: ')
    if end_program == end_program:
        print('Bye!')
