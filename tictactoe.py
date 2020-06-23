# write your code here
def convertir_coords(x, y):
    return int(x) - 1 + (3 - int(y)) * 3


def compteur_cases(cells):
    x_counter = 0
    o_counter = 0
    for char in cells:
        if char == 'X':
            x_counter += 1
        if char == 'O':
            o_counter += 1
    if abs(x_counter - o_counter) >= 2:
        return "trop de XO"
    if x_counter + o_counter == 9:
        return "complet"


endgame = False
winner = '-'
two_winners = False
cells = '_________'
tour_X = True

while not endgame:
    case_valide = False
    case_x = -1
    case_y = -1

    while not case_valide:
        case_x, case_y = input("Enter the coordinates: ").split()
        if not case_x.isdigit() or not case_y.isdigit():
            print("You should enter numbers!")
        elif not 0 <= int(case_x) <= 3 or not 0 <= int(case_y) <= 3:
            print("Coordinates should be from 1 to 3!")
        elif cells[convertir_coords(int(case_x), int(case_y))] != '_':
            print("This cell is occupied! Choose another one!")

        else:
            case_valide = True

    if tour_X:
        cells = cells[:convertir_coords(case_x, case_y)] + 'X' + cells[convertir_coords(case_x, case_y) + 1:]
    elif not tour_X:
        cells = cells[:convertir_coords(case_x, case_y)] + 'O' + cells[convertir_coords(case_x, case_y) + 1:]
    print("---------")
    print("| " + cells[0] + " " + cells[1] + " " + cells[2] + " |")
    print("| " + cells[3] + " " + cells[4] + " " + cells[5] + " |")
    print("| " + cells[6] + " " + cells[7] + " " + cells[8] + " |")
    print("---------")

    if cells[0] == cells[1] and cells[1] == cells[2]:
        if winner != '-':
            two_winners = True
        if cells[0] == 'X':
            endgame = True
            winner = 'X'
        elif cells[0] == 'O':
            endgame = True
            winner = 'O'
    if cells[3] == cells[4] and cells[4] == cells[5]:
        if winner != '-':
            two_winners = True
        if cells[3] == 'X':
            endgame = True
            winner = 'X'
        elif cells[3] == 'O':
            endgame = True
            winner = 'O'
    if cells[6] == cells[7] and cells[7] == cells[8]:
        if winner != '-':
            two_winners = True
        if cells[6] == 'X':
            endgame = True
            winner = 'X'
        elif cells[6] == 'O':
            endgame = True
            winner = 'O'
    if cells[0] == cells[3] and cells[3] == cells[6]:
        if winner != '-':
            two_winners = True
        if cells[0] == 'X':
            endgame = True
            winner = 'X'
        elif cells[0] == 'O':
            endgame = True
            winner = 'O'
    if cells[1] == cells[4] and cells[4] == cells[7]:
        if winner != '-':
            two_winners = True
        if cells[1] == 'X':
            endgame = True
            winner = 'X'
        elif cells[1] == 'O':
            endgame = True
            winner = 'O'
    if cells[2] == cells[5] and cells[5] == cells[8]:
        if winner != '-':
            two_winners = True
        if cells[2] == 'X':
            endgame = True
            winner = 'X'
        elif cells[2] == 'O':
            endgame = True
            winner = 'O'
    if cells[0] == cells[4] and cells[4] == cells[8]:
        if winner != '-':
            two_winners = True
        if cells[0] == 'X':
            endgame = True
            winner = 'X'
        elif cells[0] == 'O':
            endgame = True
            winner = 'O'
    if cells[2] == cells[4] and cells[4] == cells[6]:
        if winner != '-':
            two_winners = True
        if cells[2] == 'X':
            endgame = True
            winner = 'X'
        elif cells[2] == 'O':
            endgame = True
            winner = 'O'

    if compteur_cases(cells) == "trop de XO" or two_winners:
        print('Impossible')
    elif compteur_cases(cells) == "complet" and winner == '-':
        endgame = True
        print('Draw')
    elif winner == 'X':
        print('X wins')
    elif winner == 'O':
        print('O wins')
    elif winner == '-':
        print('Game not finished')

    tour_X = not tour_X
