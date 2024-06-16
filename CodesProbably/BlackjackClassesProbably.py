import random


class Card:
    value: int
    name: str
    number: int
    # I don't know if number will be used, so it's just here for now
    # Maybe add picture one day

    def __init__(self, value: int, name: str, ):
        self.value = value
        self.name = name


class CardPack:
    card_options: list
    used_cards: list

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

    @staticmethod
    def get_random_card(self):
        result = self.generate_random_card()
        while result in self.used_cards:
            result = self.generate_random_card()
        self.used_cards.append(result)
        return result

    def generate_random_card(self):
        name = random.choice(self.card_options)
        value = 0
        if name == "ace":
            value = 11
            # number = 1
        elif name == "king":
            value = 10
            # number = 13
        elif name == "queen":
            value = 10
            # number = 12
        elif name == "jack":
            value = 10
            # number = 11
        elif name == "diamond":
            value = random.randint(2, 11)
            # number = 10
        elif name == "heart":
            value = random.randint(2, 11)
            # number = 9
        elif name == "club":
            value = random.randint(2, 11)
            # number = 8
        elif name == "spade":
            value = random.randint(2, 11)
            # number = random.randint(2, 10)
        return Card(value, name)
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
