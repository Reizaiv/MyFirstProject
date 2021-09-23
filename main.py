"""

Este programa es la plantilla principal de ejecucion.

"""
from WarGame import wargame as wg

# GAME SETUP

player_one = wg.Player("Player One")
player_two = wg.Player("Player Two")

new_deck = wg.Deck()
new_deck.shuffle()

for x in range(26):
    player_one.add_card(new_deck.pop_card())
    player_two.add_card(new_deck.pop_card())

round_num = 0
game_on = True

while game_on:
    round_num += 1
    print(f'Round {round_num}')

    if len(player_one.all_cards) == 0:
        print(f'Player: {player_one.name}, is out of cards! Player: {player_two.name} wins!')
        game_on = False
        break

    if len(player_two.all_cards) == 0:
        print(f'Player: {player_two.name}, is out of cards! Player: {player_one.name} wins!')
        game_on = False
        break

    #Start a new round
    player_one_cards = []
    player_one_cards.append(player_one.throw_card())

    player_two_cards = []
    player_two_cards.append(player_two.throw_card())

