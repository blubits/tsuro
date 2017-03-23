from helper import on_edge
from pathboard import PathBoard
from playerboard import PlayerBoard

"""
A board for the Tsuro game.

:Author:     Maded Batara III
:Version:    v1.0
"""

class Board:
    """
    The Board class wraps around the PathBoard and PlayerBoard classes,
    allowing them to interact with each other.
    """

    def __init__(self, rows, cols):
        """
        Creates a Board.

        Args:
            rows (int): Number of rows in the board.
            cols (int): Number of columns in the board.
        """
        self.rows = rows
        self.cols = cols
        self.graph_rows = 2 * rows
        self.graph_cols = 3 * cols + 1 
        self.path_board = PathBoard(rows, cols)
        self.player_board = PlayerBoard(rows, cols)

    def add_tile(self, tile, board_index):
        """
        Adds a tile to the board.

        Args:
            tile (Tile): Tile to add to the board.
            board_index (tuple): Row and column index of the tile in the 
                tile board.
        """
        self.path_board.add_tile(tile, board_index)

    def move(self, player):
        """
        Moves a player along the board.

        Args:
            player (Player): Player to move.

        Returns:
            False if player was removed from game, True otherwise.
        """
        current_position = self.player_board.current_position(player)
        while True:
            adj = self.path_board.adj(current_position)
            if len(adj) == 0:
                break
            current_position = adj[0]
            player.add_to_visited(current_position)
        if current_position in self.path_board.dragon_tile_locations or on_edge(current_position, self.graph_rows, self.graph_cols): 
            self.player_board.remove(player)
            player.in_game = False
            return False
        else:
            self.player_board.move(self, player, current_position)
            return True
