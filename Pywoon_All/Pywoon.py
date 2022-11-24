import random
from WordList import spliting_words
from turtle import *
import time
import keyboard


# Logo that shows up at the beginning of the game or rules
def logo():
    clear()
    color_list = ['#6CA965', '#C8B653', '#787C7F', 'gray30']
    penup()
    goto(-75, 100)
    pendown()
    pencolor('gray11')
    color_vari = 0
    for inside_logo in range(4):
        pensize(15)
        fillcolor(color_list[color_vari])
        begin_fill()
        pendown()
        for logo_num in range(4):
            forward(75)
            right(90)
        end_fill()
        penup()
        forward(150)
        right(90)
        color_vari += 1
    pensize(1)


# Shortcut for letter_holder()
def each_letter(color_of_holder):
    pendown()
    letter_holder(letter_write=guess_letters[answer_index], write_color=color_of_holder)


# Shortcut for writing lose/win txt
def text_draw():
    penup()
    color('white')
    goto(0, -50)
    pendown()
    clear()


# Draws a holder depending on is the letter correct
def letter_holder(letter_write, write_color):
    pendown()
    color(write_color)
    begin_fill()
    for x in range(4):
        forward(75)
        right(90)
    end_fill()
    penup()
    forward(37)
    right(90)
    forward(58)
    color('white')
    write(f'{letter_write.upper()}', align='center', font=('Arial', 20, 'bold'))
    back(58)
    left(90)
    forward(48)


# Delays the program from ending too quickly
def ending():
    penup()
    goto(0, -100)
    write('Esc - EXIT', align='center', font=('MS Sans Serif', 15, 'bold'))


# Function that paints over letters if you input a word that isn't in list or when you use backspace
def removing_letter():
    color('gray30')
    pendown()
    begin_fill()
    for repeat2 in range(4):
        forward(75)
        right(90)
    end_fill()


# Rules Animation
def animation_main(times_draw, anim_txt, first_tile, color_of_tile, color_of_full_drawing, not_grid, anim_pos):
    if not_grid:
        penup()
        goto(-207, anim_pos)

    if first_tile:
        color(color_of_tile)
        begin_fill()
        for anim_color_drawing in range(4):
            forward(75)
            right(90)
        penup()
        forward(85)
        end_fill()

    color(color_of_full_drawing)
    begin_fill()
    for anim_row in range(times_draw):
        pendown()
        for anim_drawing in range(4):
            forward(75)
            right(90)
        penup()
        forward(85)
    end_fill()

    if not_grid:
        goto(0, anim_pos - 105)
        pendown()
        color('white')
        write(f'{anim_txt}', align='center', font=('MS Sans Serif', 20, 'bold'))


# Graph that shows you your results
def end_graph():
    first_try = 0
    second_try = 0
    third_try = 0
    fort_try = 0
    fifth_try = 0
    sixth_try = 0
    fail = 0
    all_tries = 0

    with open('UserResult.txt') as f:
        result = f.read()
        str(result)
    result_list = result.split()

    for graph_check in result_list:
        if graph_check == '1':
            first_try += 1
            all_tries += 1

        elif graph_check == '2':
            second_try += 1
            all_tries += 1

        elif graph_check == '3':
            third_try += 1
            all_tries += 1

        elif graph_check == '4':
            fort_try += 1
            all_tries += 1

        elif graph_check == '5':
            fifth_try += 1
            all_tries += 1

        elif graph_check == '6':
            sixth_try += 1
            all_tries += 1

        else:
            fail += 1
            all_tries += 1

    tries_list = [first_try, second_try, third_try, fort_try, fifth_try, sixth_try, fail]
    list_of_names = ['1', '2', '3', '4', '5', '6', 'X']
    number_graph = 0
    penup()
    goto(-175, 50)
    pencolor('white')
    fillcolor('#6CA965')
    for one_graph in tries_list:
        begin_fill()
        pendown()
        forward(50)
        left(90)
        forward(round((tries_list[number_graph] / all_tries) * 100) * 3)
        left(90)
        forward(20)
        write(f'{list_of_names[number_graph]}', align='center', font=('MS Sans Serif', 8, 'bold'))
        forward(20)
        left(90)
        forward(round((tries_list[number_graph] / all_tries) * 100) * 3)
        left(90)
        forward(40)
        end_fill()
        number_graph += 1

    penup()
    goto(0, 315)
    write('Result Graph', align='center', font=('MS Sans Serif', 15, 'bold'))


# Opens a turtle window and sets it up
title('Pywoon')
setup(width=1.0, height=1.0)
hideturtle()
speed(0)
bgcolor('black')

# Adds list of words in 'WordList' to this program
secret_word = spliting_words()
# 'tries' can not be bigger than this number
guess_limit = 6


# Starts the game program
while True:
    # All the variables
    # Number grows with each guess
    tries = 0
    # Divides the secret word to letters
    secret_word_letters = []
    # Chooses a random word from the list
    secret_number = random.randint(0, 5756)
    # Divides guessed word to letters
    guess_letters = []

    logo()
    time.sleep(3)
    clear()
    # Rules animation
    # Green TUTORIAL
    animation_main(4, 'GREEN - Right letter & place', True, '#6CA965', '#787C7F', True, 225)

    # Yellow TUTORIAL
    animation_main(4, 'YELLOW - Right letter but wrong place', True, '#C8B653', '#787C7F', True, 75)

    # Gray TUTORIAL
    animation_main(5, 'GRAY - Wrong letter', False, '#787C7F', '#787C7F', True, -75)

    penup()
    goto(0, -220)
    write('Enter - Continue', align='center', font=('MS Sans Serif', 15, 'bold'))

    while keyboard.read_key() != 'enter':
        pass

    else:
        clear()

    clear()

    # Draws the play board
    for column in range(6):
        penup()
        goto(-207, (250 - (column * 85)))
        animation_main(5, '', False, '', 'gray30', False, 0)

    # Divides secret word letters and adds them to a list
    for letters in secret_word[secret_number]:
        secret_word_letters.append(letters)

    # Checks if you used all of your tries
    while tries < guess_limit:

        # Sets up the guess input
        guess = ''
        number_for_guessing = 0
        penup()
        goto(-207, (250 - (tries * 85)))

        # Checks if you already input the guess
        while number_for_guessing < 6:
            color('white')
            input_letters = keyboard.read_key()

            if input_letters == 'enter' and number_for_guessing == 5:
                number_for_guessing += 1

            # Deletes the last letter you wrote
            if input_letters == 'backspace':
                if number_for_guessing > 0:
                    penup()
                    guess = guess[:-1]
                    setx(-207 + (85 * (number_for_guessing - 1)))
                    removing_letter()
                    number_for_guessing -= 1

            # Draws the letter you input
            if len(input_letters) == 1 and number_for_guessing < 5:
                penup()
                sety(250 - (tries * 85))
                forward(37.5)
                right(90)
                forward(57.5)
                write(f'{input_letters.upper()}', align='center', font=('Arial', 20, 'bold'))
                back(57.5)
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
        goto(-207, (250 - (tries * 85)))

        # Gives you the answer to your guess
        if guess in secret_word:
            for answers in guess_letters:

                # Correct letter and place
                if answers == secret_word_letters[answer_index]:
                    each_letter('#6CA965')

                # Correct letter but wrong place
                elif answers in secret_word_letters and guess_letters[answer_index] != secret_word_letters[answer_index]:
                    each_letter('#C8B653')

                # Wrong letter
                else:
                    each_letter('#787C7F')

                answer_index += 1

            # Draws win text
            if guess == secret_word[secret_number]:
                time.sleep(2.5)
                text_draw()
                color('white')
                write(f'You won in {tries + 1} tries!', align='center', font=('MS Sans Serif', 35, 'bold'))
                with open('UserResult.txt', 'a+', encoding='utf-8') as my_file:
                    my_file.write(str(tries + 1) + '\n')
                ending()
                end_graph()
                while True:
                    ending_input = keyboard.read_key()

                    if ending_input == 'esc':
                        bye()
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
        with open('UserResult.txt', 'a+', encoding='utf-8') as my_file:
            my_file.write('x\n')
        ending()
        goto(0, -125)
        write('P - Play again', align='center', font=('MS Sans Serif', 15, 'bold'))
        end_graph()
        while True:
            ending_input = keyboard.read_key()
            if ending_input in ('esc', 'p'):
                break

        if ending_input == 'p':
            continue

        if ending_input == 'esc':
            bye()
            break
