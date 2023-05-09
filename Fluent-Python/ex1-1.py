import collections
from random import choice

x = {
    "number": 2,
    "word": "help!"
}

# these are both equivalent --> obj[key] is supported by the underlying __getitem__ special method
# aka magic method aka "dunder" methods
print(x["number"])
print(x.__getitem__("number"))

# ex1 A Pythonic Card Deck

# collections.namedtuple to construct a simple class to represent individual cards
# namedtuple can be used to build classes of objects that are just bundles of attributes with
# no custom methods, like a database record

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suites = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suites
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, postion):
        return self._cards[postion]


deck = FrenchDeck()
print(len(deck))

# for card in deck:
#     print(card)

print(choice(deck))

print(deck[:3])
print(deck[12::13])

# sorting based on rank
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


for card in sorted(deck, key=spades_high):
    print(card)
