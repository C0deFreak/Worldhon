from turtle import *


def color_legend():
    colors = ['white', 'red', 'orange', 'yellow', '#808000', 'green', 'cyan', 'blue', 'magenta', 'purple']
    for col in range(10):
        begin_fill()
        penup()
        goto(-350, (((col + 1) * 25)+5))
        pendown()
        for cube in range(4):
            fillcolor(colors[col])
            forward(10)
            left(90)
        end_fill()


def txt_legend():
    for txt in range(10):
        penup()
        goto(-300, ((txt + 1) * 25))
        pendown()
        write(f'{txt * 10}% - {(txt+1)*10}', align='center', font=('Arial', 10, 'bold'))


def graph(pe, mf):
    forward(35)
    left(90)
    forward(mf)
    left(90)
    forward(11)
    write(f'{round(pe, 1)}%', align='center', font=('Arial', 8, 'bold'))
    forward(14)
    left(90)
    forward(mf)
    left(90)
    forward(25)


def ending():
    end_program = input('Type anything to quit the program: ')
    if end_program == end_program:
        print('Bye!')


def graph_color(def_percentage, def_move_formula):

    if def_percentage <= 10:
        fillcolor('white')
        begin_fill()
        graph(mf=def_move_formula, pe=def_percentage)
        end_fill()

    elif def_percentage <= 20:
        fillcolor('red')
        begin_fill()
        graph(mf=def_move_formula, pe=def_percentage)
        end_fill()

    elif def_percentage <= 30:
        fillcolor('orange')
        begin_fill()
        graph(mf=def_move_formula, pe=def_percentage)
        end_fill()

    elif def_percentage <= 40:
        fillcolor('yellow')
        begin_fill()
        graph(mf=def_move_formula, pe=def_percentage)
        end_fill()

    elif def_percentage <= 50:
        fillcolor('#808000')
        begin_fill()
        graph(mf=def_move_formula, pe=def_percentage)
        end_fill()

    elif def_percentage <= 60:
        fillcolor('green')
        begin_fill()
        graph(mf=def_move_formula, pe=def_percentage)
        end_fill()

    elif def_percentage <= 70:
        fillcolor('cyan')
        begin_fill()
        graph(mf=def_move_formula, pe=def_percentage)
        end_fill()

    elif def_percentage <= 80:
        fillcolor('blue')
        begin_fill()
        graph(mf=def_move_formula, pe=def_percentage)
        end_fill()

    elif def_percentage <= 90:
        fillcolor('magenta')
        begin_fill()
        graph(mf=def_move_formula, pe=def_percentage)
        end_fill()

    elif def_percentage <= 100:
        fillcolor('purple')
        begin_fill()
        graph(mf=def_move_formula, pe=def_percentage)
        end_fill()

    else:
        print('Error: wrong input')


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
    graph_color(def_percentage=percentage, def_move_formula=move_formula)

txt_legend()
color_legend()
ending()
