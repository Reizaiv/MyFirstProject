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


def display_board(board):
    print('     |     |    ')
    print(f'  {board[6]}  |  {board[7]}  |  {board[8]} ')
    print('-----|-----|----')
    print(f'  {board[3]}  |  {board[4]}  |  {board[5]} ')
    print('-----|-----|----')
    print(f'  {board[0]}  |  {board[1]}  |  {board[2]} ')
    print('     |     |    ')


def player_input():
    pass


print(players_choice())
board_test = ['O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O']
display_board(board_test)
