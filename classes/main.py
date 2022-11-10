from classes.card import Card
from classes.deck import Deck
from classes.hand import Hand


d = Deck()

h1 = Hand("Player 1")
h2 = Hand("Player 2")
h3 = Hand("Player 3")
h4 = Hand("Player 4")

d.shuffle()

while len (d):
    h1.add_card(d.pop_card())
    h2.add_card(d.pop_card())
    h3.add_card(d.pop_card())
    h4.add_card(d.pop_card())
    players = [h1, h2, h3, h4]


print(h1)
print(h2)
print(h3)
print(h4)
  

for i in range(13):
    round = [h1.pop_card(), h2.pop_card(), h3.pop_card(), h4.pop_card()]
    index = round.index(max(round))
    players[index].round_winner()

print(h1.get_win_count())
print(h2.get_win_count())
print(h3.get_win_count())
print(h4.get_win_count())
   