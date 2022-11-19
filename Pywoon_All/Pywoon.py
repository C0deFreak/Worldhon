import random
from WordList import spliting_words
from turtle import *
import time
from datetime import datetime
import keyboard


# Logo that shows up at the beginning of the game or rules
def logo():
    penup()
    goto(-75, 100)
    pencolor('black')
    pensize(15)
    fillcolor('green yellow')
    pendown()
    begin_fill()
    for logo_num in range(2):
        forward(150)
        right(90)
        forward(200)
        right(90)
    end_fill()
    color('white')
    penup()
    goto(0, -60)
    write('P', align='center', font=('MS Sans Serif', 80, 'bold'))
    pensize(1)


# Shortcut for letter_holder()
def each_letter(color_of_holder):
    pendown()
    letter_holder(letter_write=guess_letters[answer_index], write_color=color_of_holder)


# Shortcut for writing lose/win txt
def text_draw():
    penup()
    color('white')
    goto(0, 0)
    pendown()
    clear()


# Draws a holder depending on is the letter correct
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


# Delays the program from ending too quickly
def ending():
    penup()
    goto(0, -50)
    write('Esc - EXIT', align='center', font=('MS Sans Serif', 15, 'bold'))
    while True:
        if keyboard.read_key() == 'esc':
            bye()


# Function that paints over letters if you input a word that isn't in list or when you use backspace
def removing_letter():
    color('darkgray')
    for repeat2 in range(4):
        pendown()
        begin_fill()
        forward(75)
        right(90)
        forward(100)
        right(90)
        end_fill()


def animation_main(times_draw, anim_txt, color_bool, color_of_tile, color_of_full_drawing, grid):
    if grid:
        penup()
        goto(-207.5, 140)

    if color_bool:
        color(color_of_tile)
        begin_fill()
        for anim_color_drawing in range(2):
            forward(75)
            right(90)
            forward(100)
            right(90)
        penup()
        forward(85)
        end_fill()

    color(color_of_full_drawing)
    begin_fill()
    for anim_row in range(times_draw):
        pendown()
        for anim_drawing in range(2):
            forward(75)
            right(90)
            forward(100)
            right(90)
        penup()
        forward(85)
    end_fill()

    if grid:
        goto(0, 0)
        pendown()
        color('white')
        write(f'{anim_txt}', align='center', font=('MS Sans Serif', 20, 'bold'))
        time.sleep(5)
        clear()


# Opens a turtle window and sets it up
title('Pywoon')
hideturtle()
speed(1000)
bgcolor('gray11')


# All the variables
# Adds list of words in 'WordList' to this program
secret_word = spliting_words()
# Number grows with each guess
tries = 0
# 'tries' can not be bigger than this number
guess_limit = 6
# Divides the secret word to letters
secret_word_letters = []
# Chooses a random word from the list
secret_number = random.randint(0, 2499)
# Divides guessed word to letters
guess_letters = []
# Input that gives you a choice of rules or starting the game
option = textinput('OPTIONS', 'RULES / START').upper()


# Starts the game program if your input is correct
if option == 'START':

    logo()
    time.sleep(3)
    clear()

    # Draws the play board
    for column in range(6):
        penup()
        goto(-207.5, (325 - (column * 110)))
        animation_main(5, '', False, '', 'darkgray', False)

    # Divides secret word letters and adds them to a list
    for letters in secret_word[secret_number]:
        secret_word_letters.append(letters)

    # Checks if you used all of your tries
    while tries < guess_limit:

        # Sets up the guess input
        guess = ''
        number_for_guessing = 0
        penup()
        goto(-207.5, (325 - (tries * 110)))

        # Checks if you already input the guess
        while number_for_guessing < 5:
            color('white')
            input_letters = keyboard.read_key()

            # Deletes the last letter you wrote
            if input_letters == 'backspace':
                penup()
                guess = guess[:-1]
                setx(-207.5 + (85 * (number_for_guessing - 1)))
                removing_letter()
                if number_for_guessing > 0:
                    number_for_guessing -= 1

            # Draws the letter you input
            if len(input_letters) == 1:
                penup()
                sety(325 - (tries * 110))
                forward(37.5)
                right(90)
                forward(70)
                write(f'{input_letters.upper()}', align='center', font=('Arial', 20, 'bold'))
                back(70)
                left(90)
                forward(47.5)
                guess += str(input_letters)
                time.sleep(0.125)
                number_for_guessing += 1

        number_for_guessing = 0

        answer_mark = ''

        answer_index = 0

        guess_letters.clear()

        # Divides guess letters and adds them to a list
        for letters_of_guess in guess:
            guess_letters.append(letters_of_guess)

        penup()
        goto(-207.5, (325 - (tries * 110)))

        # Gives you the answer to your guess
        if guess in secret_word:
            for answers in guess_letters:

                # Correct letter and place
                if answers == secret_word_letters[answer_index]:
                    each_letter('green')

                # Correct letter but wrong place
                elif answers in secret_word_letters and guess_letters[answer_index] != secret_word_letters[answer_index]:
                    each_letter('yellow')

                # Wrong letter
                else:
                    each_letter('gray80')

                answer_index += 1

            # Draws win text
            if guess == secret_word[secret_number]:
                text_draw()
                color('white')
                write(f'You won in {tries + 1} tries!', align='center', font=('MS Sans Serif', 35, 'bold'))
                ending()
                break

            tries += 1
            print(answer_mark)

            # Removes your guess if it is not in list
        else:
            for repeat1 in range(5):
                removing_letter()
                penup()
                forward(85)

    # Draws lose text
    else:
        text_draw()
        color('white')
        write(f'Failed, the word was "{secret_word[secret_number]}"!', align='center', font=('MS Sans Serif', 35, 'bold'))
        ending()


# Begins the rules animation if the input is correct
elif option == 'RULES':
    logo()
    time.sleep(3)
    clear()

    # Green TUTORIAL
    animation_main(4, 'GREEN - Right letter & place', True, 'green', 'gray80', True)

    # Yellow TUTORIAL
    animation_main(4, 'YELLOW - Right letter but wrong place', True, 'yellow', 'gray80', True)

    # Gray TUTORIAL
    animation_main(5, 'GRAY - Wrong letter', False, 'gray80', 'gray80', True)
    bye()

# Draws if you made a wrong input
else:
    color('white')
    write('Wrong Input!', align='center', font=('MS Sans Serif', 40, 'bold'))
    ending()
