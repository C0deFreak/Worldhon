from turtle import *


def ending():
    end_program = input('Type anything to quit the program: ')
    if end_program == end_program:
        print('Bye!')


title('Graph')
hideturtle()
penup()
goto(-250, 250)
pendown()
left(-90)
forward(250)
left(90)

tests_answers = int(input('How many possibilities did you have >> '))
subject_number = int(input('How many tests did you have >> '))

same_test_answers = 0

while same_test_answers < tests_answers:
    same_test_answers += 1
    answer_results = int(input(f'How many tests were positive for {same_test_answers}. possibility >> '))
    move_formula = 25 * ((answer_results / subject_number) * 10)
    forward(20)
    left(90)
    forward(move_formula)
    left(90)
    forward(15)
    left(90)
    forward(move_formula)
    left(90)
    forward(15)

ending()
