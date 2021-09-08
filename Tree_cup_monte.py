from random import shuffle


def shuffled_list():
    my_list = ['O', ' ', ' ']
    return shuffle(my_list)


def player_guess():
    guess = ''

    while guess not in ('1', '2', '3'):
        guess = input('Selecciones un numero (1, 2 o 3): ')
        return int(guess) - 1


def check_guess(my_list, guess):
    if my_list[guess] == 'O':
        print('You are right!')
    else:
        print('Wrong pick :c')
        print(my_list)


my_list = shuffled_list()
guess = player_guess()
check_guess(my_list, guess)

