"""
A tile for the Tsuro game.

:Author:     Maded Batara III
:Version:    v1.0
"""

FACES = {
    "A": 1,
    "B": 2,
    "C": 3,
    "D": 4
}

FACES_ORDER = ["A", "B", "C", "D"]

class Tile:
    """
    In the Tsuro board game, a Tile is composed of segments of paths;
    multiple tiles, arranged and rotated in various ways, create a 
    Board with an overall path system.

    In Python, a Tile is represented by an eight-node graph, where
    two nodes are located at each side of the tile. Each side/pair of
    nodes are grouped based on letter.

               A
        |--(0)---(1)--|
        |             |
       (7)           (2)
     D  |             |  B
       (6)           (3)
        |             |
        |--(5)---(4)--|
               C

    An edge between two of these paths means that there is a path
    that passes by these points. The orientation of the tiles is
    stored through indicating which side is facing the top
    of the board (A by default).

    An empty tile represents a Dragon Tile.
    """

    def __init__(self, connected_pairs):
        """
        Creates a new Tile.

        Args:
            connected_pairs (list): A list of tuples (x, y) such that
                node x is connected to node y in the tile, where
                1 <= x, y <= 8.
        """
        self.north = "A"
        self.graph = {}
        self.connected_pairs = connected_pairs
        self.is_dragon_tile = len(self.connected_pairs) == 0

    def rotate_left():
        """
        Rotates the tile left (-90 degrees).
        """
        self.north = FACES_ORDER[FACES[self.north] - 1]

    def rotate_right():
        """
        Rotates the tile right (90 degrees).
        """
        self.north = FACES_ORDER[(FACES[self.north] + 1) % 4]

    def flip():
        """
        Flips the tile (rotates it 180 degrees).
        """
        self.north = FACES_ORDER[(FACES[self.north] + 2) % 4]

    def transform():
        """
        Transforms a rotated tile's graph.
        """
        self.north = "A"
        offset = (FACES[self.north] * 2) - 2
        new_connected_pairs = []
        for pair in connected_pairs:
            new_connected_pairs.append((
                (pair[0] + offset % 8), (pair[1] + offset % 8)
            ))
        self.connected_pairs = new_connected_pairs
        