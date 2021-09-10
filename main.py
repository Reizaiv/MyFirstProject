"""

Este programa es un juego de gato.

"""

import random
from Course_lectures_exercises import my_func
from MyMainPackage.SubPackage import mysubscript

mysubscript.sub_report()


def players_choice():
    """
    Definicion de la funcion
    :return:
    """

    char = ''
    player1_choice, player2_choice = '', ' '
    i = int(random.randint(0, 1))

    while char not in ('X', 'O'):
        # os.system('cls')
        player1_choice = input("\nSeleccione con que figura desea jugar 'X' o 'O': ")
        char = player1_choice.upper()
        if char not in ('X', 'O'):
            # os.system('cls')
            print('Opcion no valida, intente de nuevo.')
        else:
            player1_choice = char

    if char == 'X':
        player2_choice = 'O'
    elif char == 'O':
        player2_choice = 'X'

    if i == 1:
        print(f'Jugador {player1_choice}, inicia.')
        marker = player1_choice
    else:
        print(f'Jugador {player2_choice}, inicia.')
        marker = player2_choice

    display_board([])

    return marker


def player_turn(player):
    """
        Definicion de la funcion
        :return:
        """

    if player == 'X':
        return 'O'

    return 'X'


def display_board(board):
    """
        Definicion de la funcion
        :return:
        """
    print_board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    if 'X' in board or 'O' in board:
        for index in range(0, len(board), 2):
            if board[index] == 'X' or board[index] == 'O':
                print_board[board[index+1]-1] = board[index]
            else:
                pass
    else:
        pass

    print('     |     |    ')
    print(f'  {print_board[6]}  |  {print_board[7]}  |  {print_board[8]} ')
    print('-----|-----|----')
    print(f'  {print_board[3]}  |  {print_board[4]}  |  {print_board[5]} ')
    print('-----|-----|----')
    print(f'  {print_board[0]}  |  {print_board[1]}  |  {print_board[2]} ')
    print('     |     |    \n')

    return print_board


def place_holder(marker, position, board):
    """
        Definicion de la funcion
        :return:
    """

    if position in board:
        print('Casilla ya ocupada, vuelva a seleccionar...')
        marker, num = player_input(marker)
        place_holder(marker, num, board)
    else:
        board.append(marker)
        board.append(position)

    return board


def player_input(marker):
    """
        Definicion de la funcion
        :return:
    """

    print(f'Jugador {marker}, su turno...')
    num = 0
    while num not in range(1, 10):
        option = input('Seleccione una celda de 1-9: ')
        # print(option.isdigit())
        if option.isdigit():
            num = int(option)
            if num not in range(1, 10):
                print('Opcion no valida, por favor seleccione un numero entre 1-9.\n')
            else:
                continue
        else:
            print('Opcion no valida, por favor seleccione un numero entre 1-9.\n')
        # else:
        # num = int(option)
    return marker, num


def check_victory(board, marker):
    """
            Definicion de la funcion
            :return:
    """

    if board[0] == board[1] == board[2] == marker:
        print(f'Felicidades jugador {marker}, usted ha ganado!')
    elif board[3] == board[4] == board[5] == marker:
        print(f'Felicidades jugador {marker}, usted ha ganado!')
    elif board[6] == board[7] == board[8] == marker:
        print(f'Felicidades jugador {marker}, usted ha ganado!')
    elif board[0] == board[3] == board[6] == marker:
        print(f'Felicidades jugador {marker}, usted ha ganado!')
    elif board[1] == board[4] == board[7] == marker:
        print(f'Felicidades jugador {marker}, usted ha ganado!')
    elif board[2] == board[5] == board[8] == marker:
        print(f'Felicidades jugador {marker}, usted ha ganado!')
    elif board[0] == board[4] == board[8] == marker:
        print(f'Felicidades jugador {marker}, usted ha ganado!')
    elif board[6] == board[4] == board[2] == marker:
        print(f'Felicidades jugador {marker}, usted ha ganado!')
    elif ' ' not in board:
        print('Empate!')
        return True
    else:
        return False
    return True


def keep_playing():
    """
        Definicion de la funcion
        :return:
    """
    char = ''

    while char not in ('X', 'O'):
        # os.system('cls')
        opcion = input("\nDesea seguir jugando? Y/N: ")
        char = opcion.upper()
        if char not in ('Y', 'N'):
            # os.system('cls')
            print('Opcion no valida, intente de nuevo.')
        elif char == 'N':
            return False
        else:
            pass
    return True


my_func()

KEEP = True
while KEEP:
    MARCADOR = players_choice()
    TABLERO = []
    GANADOR = False
    while not GANADOR:
        FIGURA, posicion = player_input(MARCADOR)
        TABLERO = place_holder(FIGURA, posicion, TABLERO)
        BOARD = display_board(TABLERO)
        GANADOR = check_victory(BOARD, FIGURA)
        MARCADOR = player_turn(MARCADOR)

    KEEP = keep_playing()


'''
marcador = players_choice()
turnos = 0
while turnos < 9:
    figura, posicion = player_input(marcador)
    tablero = place_holder(figura, posicion)
    board = display_board(tablero)
    check_victory(board, figura)
    marcador = player_turn(marcador)
    turnos += 1


# figura, posicion = player_input(marcador)
# tablero = place_holder(figura, posicion)
# display_board(tablero)
# tablero = place_holder('O', 5, tablero)
# display_board(tablero)
# print(f'{player1}, {player2}')

# num = player_input()
# display_board(num, 'X')

# place_holder('x', 0)
# print(place_holder('o',1))

# player_turn()
'''