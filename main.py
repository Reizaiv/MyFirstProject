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

    display_board()

    return marker


def display_board(board=[]):
    print_board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    i = 0
    if 'X' in board or 'O' in board:
        for value in board:
            if value == 'X' or value == 'O':
                print_board[i+1] = value
            else:
                pass
            i += 1
    else:
        pass
    # board[option-1] = player_turn
    # print(f'Jugador {marker}, su turno...')
    print('     |     |    ')
    print(f'  {print_board[6]}  |  {print_board[7]}  |  {print_board[8]} ')
    print('-----|-----|----')
    print(f'  {print_board[3]}  |  {print_board[4]}  |  {print_board[5]} ')
    print('-----|-----|----')
    print(f'  {print_board[0]}  |  {print_board[1]}  |  {print_board[2]} ')
    print('     |     |    ')

    return board


def place_holder(board, marker, position):
    
    board.append(marker)
    board.append(position)

    return board


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
figura = player_turn(player1, player2)
figura, posicion = player_input(figura)
tablero = place_holder(figura, posicion)
display_board(tablero)
tablero = place_holder('O',5)
display_board(tablero)
# print(f'{player1}, {player2}')

# num = player_input()
# display_board(num, 'X')

# place_holder('x', 0)
# print(place_holder('o',1))

# player_turn()
