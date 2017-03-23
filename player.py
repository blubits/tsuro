"""
A player for the Tsuro game.

:Author:     Maded Batara III
:Version:    v1.0
"""

class Player:
    """
    The Player class is a helper class for the Tsuro player.
    """

    def __init__(self, name, turn):
        """
        Creates a new Player.

        Args:
            name (str): Name of player.
            turn (int): Zero-based index indicating player turn.
        """
        self.name = name
        self.player = player
        self.turn = turn
        self.hand = []
        self.visited = []
        self.in_game = False

    def add_to_visited(self, graph_index):
        """
        Adds a graph node to the list of visited nodes.

        Args:
            graph_index (tuple): Row and column index of node to add.
        """
        self.visited.append(graph_index)

    def add_to_hand(self, tile):
        """
        Adds a tile to the Player's hand.

        Args:
            tile (Tile): Tile to add to hand.
        """
        self.hand.append(tile)
