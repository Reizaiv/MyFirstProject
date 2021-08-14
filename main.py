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
