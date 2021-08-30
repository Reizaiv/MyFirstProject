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


def player_input():
    pass


def display_board():
    pass


print(players_choice())
