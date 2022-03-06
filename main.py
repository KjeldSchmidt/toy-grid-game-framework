# This file need not concern you. Feel free to poke around and understand it,
# but you can probably get by without changing anything here!
import pyglet as pg

from GameBoard import GameBoard
from GameRules import GameRules
from GameWindow import GameWindow

window_width = 800
window_height = 800
grid_cell_size = 20


game_board = GameBoard(window_width//grid_cell_size, window_height//grid_cell_size)
game_rules = GameRules(game_board)
window = GameWindow(window_width, window_height, grid_cell_size, game_board, game_rules)

game_rules.setup()

pg.app.run()
