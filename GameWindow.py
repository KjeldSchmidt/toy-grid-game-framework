# This file need not concern you. Feel free to poke around and understand it,
# but you can probably get by without changing anything here!
import pyglet as pg
from pyglet import shapes

from GameBoard import GameBoard
from GameRules import GameRules


class GameWindow(pg.window.Window):
    def __init__(
            self,
            window_width: int,
            window_height: int,
            grid_cell_size: int,
            game_board: GameBoard,
            game_rules: GameRules
    ):
        super().__init__()
        self.window_width = window_width
        self.window_height = window_height
        self.grid_cell_size = grid_cell_size

        self.game_board = game_board
        self.game_rules = game_rules

        self.grid_batch = pg.graphics.Batch()
        self.background = shapes.Rectangle(0, 0, window_width, window_height)

        self.lines = []
        for x in range(0, window_width, grid_cell_size):
            vertical_grid_line = shapes.Line(x, 0, x, window_width, width=2, color=(0, 0, 0), batch=self.grid_batch)
            self.lines.append(vertical_grid_line)
        for y in range(0, window_height, grid_cell_size):
            horizontal_grid_line = shapes.Line(0, y, window_width, y, width=2, color=(0, 0, 0), batch=self.grid_batch)
            self.lines.append(horizontal_grid_line)

    def on_draw(self):
        self.clear()
        self.background.draw()
        self.game_board.draw(self.grid_cell_size)
        self.grid_batch.draw()

    def on_key_press(self, symbol, modifiers):
        self.game_rules.on_key_press(symbol, modifiers)



