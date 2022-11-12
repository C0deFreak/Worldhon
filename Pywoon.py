import random
from turtle import *


def letter_holder(letter_write, write_color):
    color(write_color)
    begin_fill()
    forward(75)
    right(90)
    forward(100)
    right(90)
    forward(75)
    right(90)
    forward(30)
    penup()
    right(90)
    forward(37.5)
    color('white')
    write(f'{letter_write.upper()}', align='center', font=('Arial', 20, 'bold'))
    color(write_color)
    back(37.5)
    left(90)
    pendown()
    forward(70)
    right(90)
    penup()
    forward(85)
    end_fill()


def ending():
    end_program = textinput('End Program', 'Write anything to end program')


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
               'zilla', 'zeros', 'zorse', 'zokor',
               'phone', 'ditch', 'apple', 'green',
               'truck', 'table', 'plant', 'chair']

tries = 0

guess_limit = 6

secret_word_letters = []

secret_word_number = random.randint(0, 95)

guess_letters = []

title('Pywoon')

hideturtle()
speed(1000)

bgcolor('gray11')

for column in range(6):
    penup()
    goto(-207.5, (325 - (column * 110)))
    pendown()
    color('darkgray')
    for row in range(5):
        pendown()
        for drawing in range(2):
            forward(75)
            right(90)
            forward(100)
            right(90)
        penup()
        forward(85)


for letters in secret_word[secret_word_number]:
    secret_word_letters.append(letters)


while tries < guess_limit:

    guess = textinput('Guess your word', f'{tries + 1}. Guess')

    answer_mark = ''

    answer_index = 0

    guess_letters.clear()

    for letters_of_guess in guess:
        guess_letters.append(letters_of_guess)

    penup()
    goto(-207.5, (325 - (tries * 110)))

    for answers in guess_letters:

        if answers == secret_word_letters[answer_index]:

            pendown()
            letter_holder(letter_write=guess_letters[answer_index], write_color='green')

        elif answers in secret_word_letters and guess_letters[answer_index] != secret_word_letters[answer_index]:
            pendown()
            letter_holder(letter_write=guess_letters[answer_index], write_color='yellow')

        else:
            pendown()
            letter_holder(letter_write=guess_letters[answer_index], write_color='darkgray')

        answer_index += 1

    if guess == secret_word[secret_word_number]:
        penup()
        color('white')
        goto(0, 0)
        pendown()
        clear()
        write(f'You won in {tries + 1} tries!', align='center', font=('MS Sans Serif', 35, 'bold'))
        ending()
        break

    tries += 1
    print(answer_mark)

else:
    penup()
    color('white')
    goto(0, 0)
    pendown()
    clear()
    write(f'You failed, the word was "{secret_word[secret_word_number]}" !', align='center', font=('MS Sans Serif', 35, 'bold'))
    ending()
