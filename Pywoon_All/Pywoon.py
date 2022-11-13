import random
from WordList import spliting_words
from turtle import *


def eachletter(color_of_holder):
    pendown()
    letter_holder(letter_write=guess_letters[answer_index], write_color=color_of_holder)


def textdraw():
    penup()
    color('white')
    goto(0, 0)
    pendown()
    clear()


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
    end_program.upper()


secret_word = spliting_words()

tries = 0

guess_limit = 6

secret_word_letters = []

secret_number = random.randint(0, 2499)

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


for letters in secret_word[secret_number]:
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
    if guess in secret_word:
        for answers in guess_letters:

            if answers == secret_word_letters[answer_index]:
                eachletter('green')

            elif answers in secret_word_letters and guess_letters[answer_index] != secret_word_letters[answer_index]:
                eachletter('yellow')

            else:
                eachletter('darkgray')

            answer_index += 1

        if guess == secret_word[secret_number]:
            textdraw()
            write(f'You won in {tries + 1} tries!', align='center', font=('MS Sans Serif', 35, 'bold'))
            ending()
            break

        tries += 1
        print(answer_mark)
    else:
        pass

else:
    textdraw()
    write(f'Failed, the word was "{secret_word[secret_number]}"!', align='center', font=('MS Sans Serif', 35, 'bold'))
    ending()
