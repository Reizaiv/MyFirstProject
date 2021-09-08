# from random import shuffle

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

'''

'''
def myfunc(message):
    lower_string = message.lower()
    num = 0
    output_string = []
    while num < len(lower_string):
        for letter in lower_string:
            if not num % 2 == 0:
                output_string.append(letter.upper())
            else:
                output_string.append(letter)
            num += 1

    return ''.join(output_string)


def master_yoda(text):
    # output_text = []
    text = text.split(' ')
    index = list(enumerate(text))
    index.sort(reverse=True)
    text = [phrase for i, phrase in index]
    # for i, phrase in index:
    # output_text.append(phrase)
    return ' '.join(text)


print(master_yoda('I am home'))
'''

'''
x = myfunc('Hola Mundo como te va!!')
print(f'el string es {x} y el tipo es {type(x)}')
'''


def my_func():
    print('Hola, estoy en otro lado')


def count_primes(num):
    count = 0

    if num == 0 or num == 1:
        return 0
    else:
        for a in range(2, num + 1):
            primo = True
            i = 2
            while i < a:
                if a % i == 0:
                    print(f'{a} No es un numero primo')
                    primo = False
                    break
                else:
                    i += 1

            if primo:
                print(f'{a} Es un numero primo')
                count += 1
        return count


# print(count_primes(100))
