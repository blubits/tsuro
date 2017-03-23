"""
A deck of tiles for the Tsuro game.

:Author:     Maded Batara III
:Version:    v1.0
"""

class Deck:
    """
    The Deck class is a helper class containing a list of tiles.
    """

    def __init__(self):
        """
        Creates a new Deck.
        """
        self.deck = []

    def push(self, tile):
        """
        Adds a tile to the deck.

        Args:
            tile (Tile): Tile to add to the deck.
        """
        self.deck.append(tile)

    def pop(self):
        """
        Gets and returns a tile from the deck.
        """
        return self.deck.pop()

    def shuffle(self):
        from random import shuffle
        shuffle(self.deck)