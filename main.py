"""

Este programa es la plantilla principal de ejecucion.

"""

from WarGame import wargame as wg


new_deck = wg.Deck()


print(new_deck)
print(new_deck.all_cards)

for i in range(0, len(new_deck.all_cards)):
    print(new_deck.all_cards[i])

new_deck.shuffle()

for i in range(0, len(new_deck.all_cards)):
    print(new_deck.all_cards[i])

my_card = new_deck.pop_card()
print(len(new_deck.all_cards))


new_player = wg.Player('Javier')
print(new_player)

new_player.add_card(my_card)
print(new_player)