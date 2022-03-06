# This file need not concern you. Feel free to poke around and understand it,
# but you can probably get by without changing anything here!
from pyglet import shapes

from GamePiece import GamePiece, piece_colors


class GameBoard:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[GamePiece.Floor for _ in range(height)] for _ in range(width)]
        self.grid_shapes = []

    def draw(self, grid_cell_size):
        for row_index, row in enumerate(self.grid):
            for column_index, cell in enumerate(row):
                if cell == GamePiece.Floor:
                    continue

                x = row_index
                y = column_index
                w = grid_cell_size

                shape = shapes.Rectangle(x*w, y*w, w, w, color=piece_colors[cell])
                shape.draw()
                self.grid_shapes.append(shape)

    def set_grid_cell(self, x, y, game_piece: GamePiece) -> None:
        self.grid[x][y] = game_piece

    def get_grid_cell(self, x, y) -> GamePiece:
        return self.grid[x][y]
