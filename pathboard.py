"""
A board of paths for the Tsuro game.

:Author:     Maded Batara III
:Version:    v1.0
"""

from helper import path_to_board_index

class PathBoard:
    """
    A PathBoard is a representation of the Tsuro board as a graph.
    An R*C board in the game is represented by a grid graph with
    2*R rows and (3*C)+1 columns. The R*C board will be referred to as
    the tile board; the grid graph will be referred to as the graph board.
    """

    def __init__(self, rows, cols):
        """
        Creates a new PathBoard.

        Args:
            rows (int): Number of rows in the board.
            cols (int): Number of columns in the board.
        """
        self.rows = rows
        self.cols = cols
        self.graph_rows = 2 * rows
        self.graph_cols = 3 * cols + 1 
        self.graph = {}
        self.dragon_tile_locations = None

    def add_tile(self, tile, board_index):
        """
        Adds a tile to the board.

        Args:
            tile (Tile): Tile to add to the board.
            board_index (tuple): Row and column index of the tile in the 
                tile board.
        """
        if tile.is_dragon_tile:
            self.dragon_tile_locations = []
            for i in range(8):
                self.dragon_tile_locations.append(
                    tile_to_board_index(i, board_index)
                )
            return
        tile.transform()
        for pair in tile.connected_pairs:
            one = tile_to_board_index(pair[0], board_index)
            two = tile_to_board_index(pair[1], board_index)
            self.graph[one] = two
            self.graph[two] = one

    def adj(self, graph_index, visited):
        """
        Gets the tiles adjacent to the graph index.

        Args:
            graph_index (tuple): Row and column index of the node in the
                graph board.
            visited (list): List of already visited graph indices.
        """
        adj = []
        for node in self.graph[graph_index]:
            if node not in visited:
                adj.append(node)
        return adj