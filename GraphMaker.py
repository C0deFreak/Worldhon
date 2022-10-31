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
for i in range(10):
    forward(4)
    left(180)
    forward(4)
    left(90)
    forward(25)
    left(90)

tests_answers = int(input('How many possibilities did you have >> '))
subject_number = int(input('How many tests did you have >> '))

same_test_answers = 0

while same_test_answers < tests_answers:
    same_test_answers += 1
    answer_results = int(input(f'How many tests were positive for {same_test_answers}. possibility >> '))
    move_formula = 25 * ((answer_results / subject_number) * 10)
    percentage = ((answer_results / subject_number) * 100)
    forward(35)
    left(90)
    forward(move_formula)
    left(90)
    forward(11)
    write(f'{round(percentage, 1)}%', align='center', font=('Arial', 8, 'bold'))
    forward(14)
    left(90)
    forward(move_formula)
    left(90)
    forward(25)

ending()
