# Put all your logic in here to start with!
from pyglet.window import key

from GameBoard import GameBoard
from GamePiece import GamePiece


class GameRules:
    def __init__(self, game_board: GameBoard):
        self.game_board = game_board

    def setup(self):
        self.game_board.set_grid_cell(0, 0, GamePiece.Player)
        self.game_board.set_grid_cell(10, 10, GamePiece.Wall)
        self.game_board.set_grid_cell(5, 5, GamePiece.Box)

    def on_key_press(self, symbol, modifiers):
        if self.game_board.get_grid_cell(0, 0) == GamePiece.Player and symbol == key.UP:
            self.game_board.set_grid_cell(0, 0, GamePiece.Floor)
            self.game_board.set_grid_cell(0, 1, GamePiece.Player)

        if self.game_board.get_grid_cell(0, 0) == GamePiece.Player and symbol == key.RIGHT:
            self.game_board.set_grid_cell(0, 0, GamePiece.Floor)
            self.game_board.set_grid_cell(1, 0, GamePiece.Player)

        if self.game_board.get_grid_cell(1, 0) == GamePiece.Player and symbol == key.LEFT:
            self.game_board.set_grid_cell(1, 0, GamePiece.Floor)
            self.game_board.set_grid_cell(0, 0, GamePiece.Player)

        if self.game_board.get_grid_cell(0, 1) == GamePiece.Player and symbol == key.DOWN:
            self.game_board.set_grid_cell(0, 1, GamePiece.Floor)
            self.game_board.set_grid_cell(0, 0, GamePiece.Player)

        # This can't possibly be the right way to do this... please help!