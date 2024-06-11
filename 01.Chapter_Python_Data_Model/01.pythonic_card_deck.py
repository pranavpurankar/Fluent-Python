#!/usr/bin/env python3


import collections


card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11) + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()]

    def __init__(self):
        self.__cards__ = [Card(rank, suit) for suit in self.suits]

