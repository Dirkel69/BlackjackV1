class Card:
    value: int
    name: str
    number: int
    sign: str
    # Maybe add picture one day


class CardPack:
    def __init__(self):
        used_cards = []
        card_options = [
            "ace",
            "king",
            "queen",
            "jack",
            "diamond",
            "heart",
            "club",
            "spade"
        ]
    # def GetRandomCard(self): check limit (add to used and see if over max)

# The deck of 52 playing cards
# is broadly classified into 2 which are further divided into 2 divisions.
# Red(26 cards) and Black(26 cards).
#
# The red cards are further divided into diamonds♦ (13 cards) and hearts♥ (13 cards).
#
# The black cards are further divided into
# clubs ♣(13 cards) and spades ♠ (13 cards).
#
# In each division of 13 cards classified above, there are / is -
# 3 face cards - King, Queen, Jack
# One ace card
# 9 number cards(numbered from 2–10)
