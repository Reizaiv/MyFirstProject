from random import shuffle
# from typing import List

'''

st = 'Print only the words that start with s in this sentence'

splitted = st.split(' ')
for _ in splitted:
    if not _.startswith('s'):
        continue
    print(_)

for _ in range(11):
    if _ % 2:
        continue
    print(_)

my_list = [x for x in range(1, 51) if x % 3 == 0]
print(my_list)

for _ in range(1, 101):
    if _ % 3 == 0 and _ % 5 == 0:
        print('FizBuzz')
    elif _ % 3 == 0:
        print('Fizz')
    elif _ % 5 == 0:
        print('Buzz')
    else:
        print(_)


def say_hello(name):
    print('Hello ' + name)


name = input('Inserte su nombre: ')
say_hello(name)
'''


def shuffled_list():
    initial_cup_list: list[str] = ['O', ' ', ' ']
    shuffle(initial_cup_list)
    return initial_cup_list


def player_guess():
    guess_ = ''

    while guess_ not in ['1', '2', '3']:
        guess_ = input('Selecciones un numero (1, 2 o 3): ')
    return int(guess_) - 1


def check_guess(tree_cup_list_, guess_):
    if tree_cup_list[guess_] == 'O':
        print('You are right!')
        print(tree_cup_list_)
    else:
        print('Wrong pick :c')
        print(tree_cup_list_)


tree_cup_list = shuffled_list()
guess = player_guess()
check_guess(tree_cup_list, guess)
