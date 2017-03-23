"""
A board of players for the Tsuro game.

:Author:     Maded Batara III
:Version:    v1.0
"""

class PlayerBoard:
    """
    A PlayerBoard is a representation of the Tsuro board as a 2D list.
    An R*C board in the game is represented by a 2D list with 2*R rows
    and (3*C)+1 columns. The R*C board will be referred to as the tile
    board; the grid graph will be referred to as the graph board.
    """

    def __init__(self, rows, cols):
        """
        Creates a new PlayerBoard.

        Args:
            rows (int): Number of rows in the board.
            cols (int): Number of columns in the board.
        """
        self.rows = rows
        self.cols = cols
        self.graph_rows = 2 * rows
        self.graph_cols = 3 * cols + 1 
        self.grid = [[[None] * self.graph_cols] * self.graph_rows]
        self.positions = {}

    def place(self, player, graph_index):
        """
        Places a player in the board.

        Args:
            player (Player): Player to place in the board.
            graph_index (tuple): Row and column of node to place player in.
        """
        self.grid[graph_index[0]][graph_index[1]] = player.turn
        self.positions[player.turn] = graph_index

    def move(self, player, graph_index):
        """
        Places a player in the board.

        Args:
            player (Player): Player to place in the board.
            graph_index (tuple): Row and column of node to place player in.
        """
        self.grid[self.positions[player.turn[0]]][self.positions[player.turn[1]]] = None
        self.grid[graph_index[0]][graph_index[1]] = player.turn
        self.positions[player.turn] = graph_index

    def remove(self, player):
        """
        Removes a player from the game.

        Args:
            player (Player): Player to remove from the board.
        """
        self.grid[self.positions[player.turn[0]]][self.positions[player.turn[1]]] = None
        self.positions[player.turn] = None

    def current_position(self, player):
        """
        Gets the current position of the player.
        """
        return self.positions[player.turn]
