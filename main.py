import random


def players_choice():
    char = ''
    player1_choice, player2_choice = '', ' '

    while char != 'X' and char != 'O':
        # os.system('cls')
        player1_choice = input("Seleccione con que figura desea jugar 'X' o 'O': ")
        char = player1_choice.upper()
        if char != 'X' and char != 'O':
            # os.system('cls')
            print('Opcion no valida, intente de nuevo.')
        else:
            player1_choice = char

    if char == 'X':
        player2_choice = 'O'
    elif char == 'O':
        player2_choice = 'X'

    return player1_choice, player2_choice


def player_turn(player1, player2):
    i = int(random.randint(0, 1))
    if i == 0:
        print(f'Jugador {player1}, inicia.')
        marker = player1
    else:
        print(f'Jugador {player2}, inicia.')
        marker = player2

    initial_board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    display_board(initial_board, marker)
    return marker


def display_board(board, marker):
    # board[option-1] = player_turn
    # print(f'Jugador {marker}, su turno...')
    print('     |     |    ')
    print(f'  {board[6]}  |  {board[7]}  |  {board[8]} ')
    print('-----|-----|----')
    print(f'  {board[3]}  |  {board[4]}  |  {board[5]} ')
    print('-----|-----|----')
    print(f'  {board[0]}  |  {board[1]}  |  {board[2]} ')
    print('     |     |    ')

    return board


def place_holder(marker, position):
    board = []

    return board, marker


def player_input(marker):
    num = ''
    print(f'Jugador {marker}, su turno...')
    while num not in range(1, 10):
        option = input('Seleccione una celda de 0-9: ')
        # print(option.isdigit())
        if option.isdigit():
            num = int(option)
            if num not in range(1, 10):
                print('Opcion no valida, por favor seleccione un numero entre 1-9.')
            else:
                continue
        else:
            print('Opcion no valida, por favor seleccione un numero entre 1-9.')
        # else:
            # num = int(option)
    return marker, num


player1, player2 = players_choice()
player_turn(player1, player2)

# print(f'{player1}, {player2}')

# num = player_input()
# display_board(num, 'X')

# place_holder('x', 0)
# print(place_holder('o',1))

# player_turn()