from board import Board

"""
A wrapper for the Tsuro game.

:Author:     Maded Batara III
:Version:    v1.0
"""

class Game:
    """
    The Game class wraps around all the classes in the Tsuro module.
    """

    def __init__(self, num_players, deck, rows, cols):
        """
        Creates a new Game.

        Args:
            num_players (int): Number of players in the game.
            deck (Deck): Deck containing cards.
            rows (int): Number of rows in the board.
            cols (int): Number of columns in the game.
        """
        self.num_players = num_players
        self.deck = deck
        self.board = Board(rows, cols):
        self.players = [[None] * num_players]
        self.in_game = False
        self.current_player = None

    def add_player(self, player, turn):
        """
        Adds a player to the game.

        Args:
            player (Player): Player to add to game.
            turn (int): Player's turn, zero-indexed.
        """
        self.players[turn] = self.players

    def start(self):
        """
        Starts the game.
        """
        if all([x is not None for x in self.players]):
            self.in_game = True

    def add_tile(self, tile, board_index):
        """
        Adds a tile to the board.

        Args:
            tile (Tile): Tile to add to the board.
            board_index (tuple): Row and column index of the tile in the 
                tile board.
        """
        self.board.add_tile(tile, board_index)

    def move(self):
        """
        Moves the current player along the line.
        """
        if not self.board.move(self.current_player):
            self.players[self.current_player.turn] = None

    def next_turn(self):
        """
        Moves the game to the next player/turn.
        """
        count = 0
        for player in self.players:
            if player is not None:
                count += 1
        if count = 1:
            self.in_game = False
            return
        while True:
            self.current_player = self.players
            if self.current_player is not None:
                break

    def winner(self):
        """
        Returns the winner of the game.
        """
        if not self.in_game:
            for player in self.players:
                if player is not None:
                    count += 1

