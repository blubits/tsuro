"""
Helper functions for the Tsuro game.

:Author:     Maded Batara III
:Version:    v1.0
"""

def tile_to_board_index(tile_index, board_index):
    """
    Converts a 0-7 tile node index to an (r, c) graph board index.

    Args:
        tile_index (int): Index of node in tile.
        board_index (tuple): Row and column index of the tile in the 
            tile board.
    Returns:
        A 2-tuple indicating the node's position in the graph board.
    """
    if 4 <= tile_index <= 7:
        row_offset = 1
    else:
        row_offset = 0
    if tile_index in [1, 6]:
        column_offset = 1
    elif tile_index in [2, 5]:
        column_offset = 2
    elif tile_index in [3, 4]:
        column_offset = 3
    else:
        column_offset = 0
    return (board_index[0] * 2 + row_offset, board_index[0] * 3 + column_offset)

def on_edge(graph_index, rows, cols):
    """
    Checks if the index is at the edge of the board.

    Args:
        graph_index (tuple): Index of node in the graph.
        rows (int): Number of rows in the grid graph.
        cols (int): Number of columns in the grid graph.
    """
    return graph_index[0] == 0 or graph_index[0] == rows - 1 or graph_index[1] == 0 or graph_index[1] == cols - 1